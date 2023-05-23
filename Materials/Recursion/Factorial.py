# Program to print factorial of a number recursively.
 
# Recursive function
def recursive_factorial(n):
  if n == 1:
      return n
  else:
      return n * recursive_factorial(n-1)
 

# initialise num variable
num = 0

# check if the input is valid or not, if not REPEAT input
while num <= 0:
  num = int(input("Enter the Factorial number: "))

if num > 0:
    print("")
    print("Factorial of number", num, "=", recursive_factorial(num))