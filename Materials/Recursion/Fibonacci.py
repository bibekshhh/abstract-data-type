# Program to print the fibonacci series upto n_terms
 
# Recursive function
def recursive_fibonacci(n):
  if n <= 1:
      return n
  else:
      return(recursive_fibonacci(n-1) + recursive_fibonacci(n-2))
 
# initialise n_terms variable
n_terms = 0

# check if the number of terms is valid, if not repeat Input
while n_terms <= 0:
  n_terms = int(input("Enter the nth term: "))

if (n_terms > 0):
    print("====== Fibonacci Series ======")
    print("")
    for i in range(n_terms):
        print(recursive_fibonacci(i))