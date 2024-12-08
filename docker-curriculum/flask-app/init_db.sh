#!/bin/bash

# Read secrets from the Docker Secrets file
ROOT_PASSWORD=$(grep 'MYSQL_ROOT_PASSWORD' /run/secrets/db_secrets | cut -d '=' -f2)
DATABASE=$(grep 'MYSQL_DATABASE' /run/secrets/db_secrets | cut -d '=' -f2)

# Validate that required secrets are present
if [ -z "$ROOT_PASSWORD" ] || [ -z "$DATABASE" ]; then
  echo "Error: MYSQL_ROOT_PASSWORD or MYSQL_DATABASE not found in secrets."
  exit 1
fi

echo "Initializing MySQL with root password and creating database..."

# Create an SQL initialization script
cat <<EOF > /docker-entrypoint-initdb.d/init.sql
ALTER USER 'root'@'localhost' IDENTIFIED BY '$ROOT_PASSWORD';
CREATE DATABASE IF NOT EXISTS \`$DATABASE\`;
EOF

# Export the password for MySQL's entrypoint script
export MYSQL_ROOT_PASSWORD=$ROOT_PASSWORD

# Use the default MySQL entrypoint to complete setup
exec docker-entrypoint.sh mysqld