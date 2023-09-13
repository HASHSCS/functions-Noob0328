def square(number):
    """
    This function takes a number as input and returns its square.
    :param number: int or float
    :return: int or float, the square of the input number
    """
def square(number):
        square_number=number*number
        return square_number
number = int(input("Enter the number: "))
I = square(number)
print("The square of", number, "is:", I)


def reverse_string(s):
    """
    This function takes a string as input and returns its reverse.
    :param s: str
    :return: str, the reversed string
    """
def reverse_string(s):
  return s[::-1]
string = input("Enter a string:")
reverse_string = reverse_string(string)
print("Reversed string:", reverse_string)


def factorial(n):
    """
    This function takes a number as input and returns its factorial.
    :param n: int
    :return: int, the factorial of the input number
    """
def is_prime(n):
    for i in range(2,n-1):
      if n%i==0:
         return False
    else:
        return True
a=int(input("Enter a number"))
print(is_prime(a))

def find_maximum(lst):
    """
    This function takes a list of numbers lst and returns the maximum number in the list.
    :param lst: list of int
    :return: int, the maximum number in the list
    """
def find_maximum(lst):
    maximum=0
    for i in lst:
        if i>maximum or i==maximum:
            maximum=i
    return maximum
a=[1,2,3,4,5,6,7,8]
print(f"{find_maximum(a)}")


def odd_or_even(n):
    """
    This function takes a number n and returns "Odd" if the number is odd and "Even" if the number is even.
    :param n: int
    :return: str, "Odd" or "Even"
    """
def odd_or_even(n):
    if n % 2 == 0:
        print("Yes, it is an even number")
    else:
        print("It is an odd number")

a = int(input("Enter a number: "))
odd_or_even(a)

        

def is_palindrome(s):
    """
    This function takes a string `s` and returns `True` if the string is a palindrome, and `False` otherwise. 
    A palindrome is a word or phrase that reads the same backward as forward.
    
    :param s: str
    :return: bool, `True` if the string is a palindrome, `False` otherwise.
    """
def is_palindrome(s):
    return s == s[::-1]
print(is_palindrome("racecar")) 
print(is_palindrome("hello"))    
print(is_palindrome("level")) 



def find_gcd(a, b):
    """
    This function takes two positive integers `a` and `b` and returns their greatest common divisor (GCD).
    
    :param a: int
    :param b: int
    :return: int, the greatest common divisor of `a` and `b`.
    """
    divisor=0
    if a<b:
        for i in range(1,a+1,1):
            if a%i==0 and b%i==0:
                divisor=i
    if b<a:
        for i in range(1,b+1,1):
            if a%i==0 and b%i==0:
                divisor=i   
            
    return divisor



