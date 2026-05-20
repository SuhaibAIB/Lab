#Create a function that takes a list of numbers and returns the sum of the squares of those numbers.
def sum_of_squares(numbers):
    return sum(x**2 for x in numbers)
#Create a function that takes a string and returns the number of vowels in that string.
def count_vowels(s):
    vowels = 'aeiouAEIOU'
    return sum(1 for char in s if char in vowels)
#Create a function that takes a list of strings and returns a new list with the strings sorted in alphabetical order.
def sort_strings(strings):
    return sorted(strings)
#Create a function that takes a list of numbers and returns a new list with only the even numbers from the original list.
def filter_even_numbers(numbers):
    return [x for x in numbers if x % 2 == 0]
#Create a function that takes a list of strings and returns a new list with the strings that have more than 5 characters.
def filter_long_strings(strings):
    return [s for s in strings if len(s) > 5]
def proccess_data(data):
    # Example processing: filter even numbers and sort them
    even_numbers = filter_even_numbers(data)
    sorted_even_numbers = sorted(even_numbers)
    return sorted_even_numbers