#This file has many pylint issues

def add(a,b): #missing spaces
  return a+b  #bad indentation + missing spaces

def greet(name): #missing type hint
 print("Hello " + name) #wrong indentation, no docstring

def factorial(n): 
 if n==0: return 1 #inline if
 else:
    return n*factorial(n-1) #inconsistent indent

def main():  #no docstring
  for i in range(5):print(factorial(i)) #inline for-loop
  greet("luv")
  print(add(2,3))

main() #should use __main__ guard
