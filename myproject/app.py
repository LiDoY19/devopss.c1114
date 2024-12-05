from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

def preprocess_data(data):
    for result in data.get("result", []):
        # Ensure anilist is a dictionary
        anilist = result.get("anilist", {})
        if not isinstance(anilist, dict):
            anilist = {}  # Fallback to an empty dictionary

        # Ensure title is a dictionary
        title = anilist.get("title", {})
        if not isinstance(title, dict):
            title = {}  # Fallback to an empty dictionary

        # Assign processed fields with fallbacks
        result["anime_title"] = title.get("english") or title.get("romaji") or "Unknown Title"
        result["episode"] = result.get("episode", "Unknown")
        result["from"] = result.get("from", 0)
        result["to"] = result.get("to", 0)
        result["image"] = result.get("image", "")
    return data

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/search", methods=["GET", "POST"])
def search():
    if request.method == "GET":
        # Handle the GET request (URL provided in query parameter)
        image_url = request.args.get("image_url")
        if not image_url:
            return jsonify({"error": "No URL provided"}), 400
        api_url = f"https://api.trace.moe/search?url={image_url}"
        try:
            response = requests.get(api_url)
            response.raise_for_status()
            data = preprocess_data(response.json())  # Preprocess data here
            return render_template("results.html", data=data)
        except requests.exceptions.RequestException as e:
            return jsonify({"error": str(e)}), 500

    elif request.method == "POST":
        # Handle the POST request (File upload or URL submission)
        image_url = request.form.get("image_url")
        uploaded_file = request.files.get("image_file")

        if image_url:
            api_url = f"https://api.trace.moe/search?url={image_url}"
            try:
                response = requests.get(api_url)
                response.raise_for_status()
                data = preprocess_data(response.json())  # Preprocess data here
                return render_template("results.html", data=data)
            except requests.exceptions.RequestException as e:
                return jsonify({"error": str(e)}), 500

        elif uploaded_file:
            # Debug: Print details about the uploaded file
            print(f"Uploaded file: {uploaded_file.filename}, Content-Type: {uploaded_file.content_type}")

            # Check file size
            uploaded_file.seek(0, 2)  # Move to the end of the file
            file_size = uploaded_file.tell()
            uploaded_file.seek(0)  # Reset to the beginning
            if file_size > 10 * 1024 * 1024:  # 10 MB limit
                return jsonify({"error": "File size exceeds the limit of 10 MB"}), 400

            # Validate MIME type
            if uploaded_file.content_type not in ["image/jpeg", "image/png"]:
                return jsonify({"error": "Unsupported file type"}), 400

            # If checks pass, proceed with API request
            api_url = "https://api.trace.moe/search"
            files = {"file": uploaded_file.read()}
            headers = {"Content-Type": uploaded_file.content_type}

            try:
                response = requests.post(api_url, files=files, headers=headers)
                response.raise_for_status()
                data = preprocess_data(response.json())  # Preprocess data here
                return render_template("results.html", data=data)
            except requests.exceptions.RequestException as e:
                return jsonify({"error": str(e), "details": response.text}), 500

    else:
        return jsonify({"error": "No input provided"}), 400

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)