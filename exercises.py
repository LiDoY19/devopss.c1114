# #1+2 
# def greet(name="Guest"):
#     return f"Hello, {name}"
# print(greet())

#3
# def add(*args):
#     return sum(args)
# print(add(1,2))

# def factorial(n):
#     if n < 0: 
#         raise ValueError("Factorial is not defined for negative numbers.")
#     result = 1
#     for i in range(1, n+1):
#         result *= i
#     return result
# print(factorial(input("Enter a number: ")))

# x = 5
# def print_g():
#     x = 20
#     y = 2
#     print(x,y)
# print_g()

# a = 5
# b = 2
# def sum_n():
#     return a + b

# result = sum_n()
# print(result)

# def stam():
#     z = 10
#     if z < 0:
#         print(f"the number is negativ!, and the number is {z}!")
#     else:
#         print(f"the number is positev! and the number is {z}!")
# stam()

#for and while loops
#1 
# count = [1, 2, 3, 4, 5]
# for n in  count:
#     print(n)

#2
# count = 0
# while count < 5:
#     print(count)
#     count += 1

#3
# lst = [10, 20, 30, 40, 50]
# sum_lst = 0 
# for n in lst:
#     sum_lst += n
#     print(sum_lst)

#4
# for i in range(1,4):
#     for j in range(1,4):
#         print(f"{i}X{j} = {i*j}" ,end="\t")
#     print()

#5
# count = 0
# while True: 
#     stop_loop = str(input("Enter a the password: ").lower)
#     count += 5
#     if stop_loop == "stop":
#         print("The programe is stopped!")
#         break
#     else:
#         print(f"You entered: {stop_loop}. Keep guessing")
# print(f"you made {count} entries befor stopping.")
