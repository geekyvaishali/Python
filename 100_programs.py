"""
100 PROGRAMS - 100 Python Programs (1-85), code with output
Source list: Harshal Chauhan, "100 Python programs compulsory before you start Data Science".
Programs 1-84 are from the post; 85 (insertion sort) was hidden in the post, so it is written here.
Programs 86-100 were not available.

Run: python 100_programs.py
"""


# ============================================================
# BASICS
# ============================================================

# Program 01: Hello World.
print("Hello, World!")

# Output:
# Hello, World!

# Program 02: Swap two variables without a temporary variable.
a, b = 5, 10
a, b = b, a
print(a, b)  # 10 5

# Output:
# 10 5

# Program 03: Check even or odd.
n = 7
result = "Even" if n % 2 == 0 else "Odd"
print(result)

# Output:
# Odd

# Program 04: Find the largest of three numbers.
x, y, z = 3, 9, 6
print(max(x, y, z))

# Output:
# 9

# Program 05: Check if a number is prime.
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

print(is_prime(17))

# Output:
# True

# Program 06: Print the Fibonacci series.
def fibonacci(n):
    a, b = 0, 1
    seq = []
    for _ in range(n):
        seq.append(a)
        a, b = b, a + b
    return seq

print(fibonacci(10))

# Output:
# [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]

# Program 07: Calculate a factorial.
def factorial(n):
    return 1 if n == 0 else n * factorial(n - 1)

print(factorial(5))

# Output:
# 120

# Program 08: Check if a number is a palindrome.
def is_palindrome_num(n):
    return str(n) == str(n)[::-1]

print(is_palindrome_num(121))

# Output:
# True

# Program 09: Reverse a number.
def reverse_number(n):
    return int(str(n)[::-1])

print(reverse_number(1234))

# Output:
# 4321

# Program 10: Sum the digits of a number.
def sum_of_digits(n):
    return sum(int(d) for d in str(n))

print(sum_of_digits(12345))

# Output:
# 15

# Program 11: Check for an Armstrong number.
def is_armstrong(n):
    digits = str(n)
    power = len(digits)
    return n == sum(int(d) ** power for d in digits)

print(is_armstrong(153))

# Output:
# True

# Program 12: Convert Celsius to Fahrenheit.
def celsius_to_fahrenheit(c):
    return (c * 9 / 5) + 32

print(celsius_to_fahrenheit(100))

# Output:
# 212.0

# Program 13: Build a simple calculator.
def calculator(a, b, op):
    if op == '+': return a + b
    elif op == '-': return a - b
    elif op == '*': return a * b
    elif op == '/': return a / b

print(calculator(6, 3, '+'))

# Output:
# 9

# Program 14: Check if a year is a leap year.
def is_leap_year(y):
    return y % 4 == 0 and (y % 100 != 0 or y % 400 == 0)

print(is_leap_year(2024))

# Output:
# True

# Program 15: Find the GCD of two numbers.
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

print(gcd(48, 18))

# Output:
# 6

# Program 16: Find the LCM of two numbers.
def lcm(a, b):
    return a * b // gcd(a, b)

print(lcm(4, 6))

# Output:
# 12

# Program 17: Print a multiplication table.
def multiplication_table(n):
    return [n * i for i in range(1, 11)]

print(multiplication_table(5))

# Output:
# [5, 10, 15, 20, 25, 30, 35, 40, 45, 50]

# Program 18: Sum the first N natural numbers.
def sum_natural(n):
    return n * (n + 1) // 2

print(sum_natural(10))

# Output:
# 55

# Program 19: Count the digits in a number.
def count_digits(n):
    return len(str(abs(n)))

print(count_digits(12345))

# Output:
# 5

# Program 20: Check if a number is a perfect number.
def is_perfect(n):
    return n == sum(i for i in range(1, n) if n % i == 0)

print(is_perfect(28))

# Output:
# True

# ============================================================
# STRINGS
# ============================================================

# Program 21: Reverse a string.
def reverse_string(s):
    return s[::-1]

print(reverse_string("hello"))

# Output:
# olleh

# Program 22: Check if a string is a palindrome.
def is_palindrome_str(s):
    return s == s[::-1]

print(is_palindrome_str("madam"))

# Output:
# True

# Program 23: Count the vowels in a string.
def count_vowels(s):
    return sum(1 for c in s.lower() if c in 'aeiou')

print(count_vowels("Hello World"))

# Output:
# 3

# Program 24: Count the words in a sentence.
def count_words(s):
    return len(s.split())

print(count_words("the quick brown fox"))

# Output:
# 4

# Program 25: Check if two strings are anagrams.
def is_anagram(s1, s2):
    return sorted(s1.lower()) == sorted(s2.lower())

print(is_anagram("listen", "silent"))

# Output:
# True

# Program 26: Remove duplicate characters from a string.
def remove_duplicates_str(s):
    seen = set()
    result = []
    for c in s:
        if c not in seen:
            seen.add(c)
            result.append(c)
    return ''.join(result)

print(remove_duplicates_str("programming"))

# Output:
# progamin

# Program 27: Find the most frequent character in a string.
def most_frequent_char(s):
    return max(set(s), key=s.count)

print(most_frequent_char("aabbbcc"))

# Output:
# b

# Program 28: Convert a string to uppercase and lowercase.
def case_convert(s):
    return s.upper(), s.lower()

print(case_convert("Hello"))

# Output:
# ('HELLO', 'hello')

# Program 29: Count occurrences of a substring.
def count_substring(s, sub):
    return s.count(sub)

print(count_substring("abcabcabc", "abc"))

# Output:
# 3

# Program 30: Check if a string is a pangram.
def is_pangram(s):
    return set('abcdefghijklmnopqrstuvwxyz').issubset(set(s.lower()))

print(is_pangram("The quick brown fox jumps over the lazy dog"))

# Output:
# True

# Program 31: Title-case every word in a sentence.
def title_case(s):
    return s.title()

print(title_case("the great gatsby"))

# Output:
# The Great Gatsby

# Program 32: Replace a character throughout a string.
def replace_char(s, old, new):
    return s.replace(old, new)

print(replace_char("banana", "a", "o"))

# Output:
# bonono

# Program 33: Split a string into a list of words.
def split_words(s):
    return s.split()

print(split_words("one two three"))

# Output:
# ['one', 'two', 'three']

# Program 34: Join a list of strings into one.
def join_words(lst):
    return ' '.join(lst)

print(join_words(["one", "two", "three"]))

# Output:
# one two three

# Program 35: Check if a string contains only digits.
def only_digits(s):
    return s.isdigit()

print(only_digits("12345"))

# Output:
# True

# ============================================================
# LISTS
# ============================================================

# Program 36: Find the largest element in a list.
def largest(lst):
    return max(lst)

print(largest([3, 7, 2, 9, 4]))

# Output:
# 9

# Program 37: Find the second largest element in a list.
def second_largest(lst):
    return sorted(set(lst))[-2]

print(second_largest([3, 7, 2, 9, 4]))

# Output:
# 7

# Program 38: Reverse a list without using built-ins.
def reverse_list(lst):
    return lst[::-1]

print(reverse_list([1, 2, 3]))

# Output:
# [3, 2, 1]

# Program 39: Remove duplicates from a list.
def remove_dup_list(lst):
    return list(dict.fromkeys(lst))

print(remove_dup_list([1, 2, 2, 3, 3, 3]))

# Output:
# [1, 2, 3]

# Program 40: Sort a list without using sort().
def bubble_sort(lst):
    lst = lst.copy()
    n = len(lst)
    for i in range(n):
        for j in range(n - i - 1):
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
    return lst

print(bubble_sort([5, 2, 8, 1]))

# Output:
# [1, 2, 5, 8]

# Program 41: Find the sum of a list.
def list_sum(lst):
    return sum(lst)

print(list_sum([1, 2, 3, 4]))

# Output:
# 10

# Program 42: Find the average of a list.
def list_average(lst):
    return sum(lst) / len(lst)

print(list_average([2, 4, 6]))

# Output:
# 4.0

# Program 43: Merge two lists into one.
def merge_lists(l1, l2):
    return l1 + l2

print(merge_lists([1, 2], [3, 4]))

# Output:
# [1, 2, 3, 4]

# Program 44: Find the common elements between two lists.
def common_elements(l1, l2):
    return list(set(l1) & set(l2))

print(common_elements([1, 2, 3], [2, 3, 4]))

# Output:
# [2, 3]

# Program 45: Find the intersection of two lists.
def list_intersection(l1, l2):
    return list(set(l1) & set(l2))

print(list_intersection([1, 2], [2, 3]))

# Output:
# [2]

# Program 46: Flatten a nested list.
def flatten(nested):
    result = []
    for item in nested:
        if isinstance(item, list):
            result.extend(flatten(item))
        else:
            result.append(item)
    return result

print(flatten([1, [2, 3], [4, [5, 6]]]))

# Output:
# [1, 2, 3, 4, 5, 6]

# Program 47: Count how many times an element appears in a list.
def count_occurrences(lst, item):
    return lst.count(item)

print(count_occurrences([1, 2, 2, 3, 2], 2))

# Output:
# 3

# Program 48: Find the missing number in a list from 1 to N.
def find_missing(lst, n):
    return sum(range(1, n + 1)) - sum(lst)

print(find_missing([1, 2, 4, 5], 5))

# Output:
# 3

# Program 49: Rotate a list by k positions.
def rotate_list(lst, k):
    k = k % len(lst)
    return lst[k:] + lst[:k]

print(rotate_list([1, 2, 3, 4, 5], 2))

# Output:
# [3, 4, 5, 1, 2]

# Program 50: Check if a list is already sorted.
def is_sorted(lst):
    return lst == sorted(lst)

print(is_sorted([1, 2, 3]))

# Output:
# True

# ============================================================
# DICTIONARIES & SETS
# ============================================================

# Program 51: Count word frequency in a sentence using a dictionary.
def word_frequency(s):
    freq = {}
    for w in s.split():
        freq[w] = freq.get(w, 0) + 1
    return freq

print(word_frequency("the cat the dog the cat"))

# Output:
# {'the': 3, 'cat': 2, 'dog': 1}

# Program 52: Merge two dictionaries.
def merge_dicts(d1, d2):
    return {**d1, **d2}

print(merge_dicts({"a": 1}, {"b": 2}))

# Output:
# {'a': 1, 'b': 2}

# Program 53: Find the key with the maximum value.
def key_with_max_value(d):
    return max(d, key=d.get)

print(key_with_max_value({"a": 3, "b": 9, "c": 1}))

# Output:
# b

# Program 54: Invert a dictionary (swap keys and values).
def invert_dict(d):
    return {v: k for k, v in d.items()}

print(invert_dict({"a": 1, "b": 2}))

# Output:
# {1: 'a', 2: 'b'}

# Program 55: Remove a key from a dictionary.
def remove_key(d, key):
    d = d.copy()
    d.pop(key, None)
    return d

print(remove_key({"a": 1, "b": 2}, "a"))

# Output:
# {'b': 2}

# Program 56: Sort a dictionary by its values.
def sort_dict_by_value(d):
    return dict(sorted(d.items(), key=lambda x: x[1]))

print(sort_dict_by_value({"a": 3, "b": 1, "c": 2}))

# Output:
# {'b': 1, 'c': 2, 'a': 3}

# Program 57: Check if two sets are disjoint.
def is_disjoint(s1, s2):
    return s1.isdisjoint(s2)

print(is_disjoint({1, 2}, {3, 4}))

# Output:
# True

# Program 58: Find the union of two sets.
def set_union(s1, s2):
    return s1 | s2

print(set_union({1, 2}, {2, 3}))

# Output:
# {1, 2, 3}

# Program 59: Find the difference between two sets.
def set_difference(s1, s2):
    return s1 - s2

print(set_difference({1, 2, 3}, {2, 3}))

# Output:
# {1}

# Program 60: Convert two parallel lists into a dictionary.
def lists_to_dict(keys, values):
    return dict(zip(keys, values))

print(lists_to_dict(["a", "b"], [1, 2]))

# Output:
# {'a': 1, 'b': 2}

# ============================================================
# FUNCTIONS & RECURSION
# ============================================================

# Program 61: Write a recursive factorial function.
def factorial_recursive(n):
    return 1 if n == 0 else n * factorial_recursive(n - 1)

print(factorial_recursive(5))

# Output:
# 120

# Program 62: Write a recursive Fibonacci function.
def fib_recursive(n):
    return n if n <= 1 else fib_recursive(n - 1) + fib_recursive(n - 2)

print(fib_recursive(7))

# Output:
# 13

# Program 63: Sum a list using recursion.
def sum_recursive(lst):
    return 0 if not lst else lst[0] + sum_recursive(lst[1:])

print(sum_recursive([1, 2, 3, 4]))

# Output:
# 10

# Program 64: Find the power of a number using recursion.
def power_recursive(base, exp):
    return 1 if exp == 0 else base * power_recursive(base, exp - 1)

print(power_recursive(2, 5))

# Output:
# 32

# Program 65: Implement recursive binary search.
def binary_search_recursive(arr, target, low=0, high=None):
    if high is None:
        high = len(arr) - 1
    if low > high:
        return -1
    mid = (low + high) // 2
    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return binary_search_recursive(arr, target, mid + 1, high)
    else:
        return binary_search_recursive(arr, target, low, mid - 1)

print(binary_search_recursive([1, 3, 5, 7, 9, 11], 7))

# Output:
# 3

# Program 66: Write a function with default arguments.
def greet(name, greeting="Hello"):
    return f"{greeting}, {name}!"

print(greet("Sam"))

# Output:
# Hello, Sam!

# Program 67: Write a function using *args and **kwargs.
def flexible_args(*args, **kwargs):
    return sum(args), kwargs

print(flexible_args(1, 2, 3, x=1))

# Output:
# (6, {'x': 1})

# Program 68: Write a lambda function to square a number.
square = lambda x: x * x

print(square(5))

# Output:
# 25

# Program 69: Use map() to square every number in a list.
squared = list(map(lambda x: x**2, [1, 2, 3, 4]))

print(squared)

# Output:
# [1, 4, 9, 16]

# Program 70: Use filter() to get only the even numbers from a list.
evens = list(filter(lambda x: x % 2 == 0, [1, 2, 3, 4, 5, 6]))

print(evens)

# Output:
# [2, 4, 6]

# ============================================================
# FILE HANDLING
# ============================================================

# Program 71: Read a text file line by line.
# --- setup: create sample files used by programs 71-75 ---
with open("data.txt", "w") as f:
    f.write("line one\nline two\nline three\n")
with open("data.csv", "w") as f:
    f.write("name,age\nSam,25\nAsha,30\n")

with open("data.txt", "r") as f:
    for line in f:
        print(line.strip())

# Output:
# line one
# line two
# line three

# Program 72: Write data to a text file.
with open("output.txt", "w") as f:
    f.write("Hello, file!")

# Output:

# Program 73: Count the number of lines in a file.
with open("data.txt", "r") as f:
    count = sum(1 for _ in f)

print(count)

# Output:
# 3

# Program 74: Read a CSV file using Python.
import csv

with open("data.csv", "r") as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)

# Output:
# ['name', 'age']
# ['Sam', '25']
# ['Asha', '30']

# Program 75: Append new data to an existing file.
with open("output.txt", "a") as f:
    f.write(" More text.")

# Output:

# ============================================================
# OOP BASICS
# ============================================================

# Program 76: Create a simple class with attributes.
class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

c = Car("Toyota", "Corolla")
print(c.brand, c.model)

# Output:
# Toyota Corolla

# Program 77: Create a class with a constructor.
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

p = Person("Sam", 25)
print(p.name, p.age)

# Output:
# Sam 25

# Program 78: Implement inheritance between two classes.
class Animal:
    def speak(self):
        return "..."

class Dog(Animal):
    pass

d = Dog()
print(d.speak())

# Output:
# ...

# Program 79: Override a method in a subclass.
class Cat(Animal):
    def speak(self):
        return "Meow"

cat = Cat()
print(cat.speak())

# Output:
# Meow

# Program 80: Create a class with a static method.
class MathHelper:
    @staticmethod
    def add(a, b):
        return a + b

print(MathHelper.add(2, 3))

# Output:
# 5

# Program 81: Implement a class using a property decorator.
class Circle:
    def __init__(self, radius):
        self._radius = radius

    @property
    def area(self):
        return 3.14159 * self._radius ** 2

circ = Circle(2)
print(circ.area)

# Output:
# 12.56636

# Program 82: Build a simple Stack class.
class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def is_empty(self):
        return len(self.items) == 0

s = Stack()
s.push(1)
s.push(2)
print(s.pop())

# Output:
# 2

# ============================================================
# ALGORITHMS
# ============================================================

# Program 83: Implement bubble sort.
def bubble_sort2(arr):
    arr = arr.copy()
    for i in range(len(arr)):
        for j in range(len(arr) - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

print(bubble_sort2([5, 1, 4, 2]))

# Output:
# [1, 2, 4, 5]

# Program 84: Implement selection sort.
def selection_sort(arr):
    arr = arr.copy()
    for i in range(len(arr)):
        min_idx = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

print(selection_sort([5, 1, 4, 2]))

# Output:
# [1, 2, 4, 5]

# Program 85: Implement insertion sort.
def insertion_sort(arr):
    arr = arr.copy()
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

print(insertion_sort([5, 1, 4, 2]))

# Output:
# [1, 2, 4, 5]
