def count_vowels(s):
    """
    Returns the number of vowels in the string s.
    """
    vowels = "aeiouAEIOU"
    return sum(1 for char in s if char in vowels)

# User input
text = input("Enter a string: ")
print(f"Number of vowels: {count_vowels(text)}")

# Test cases
assert count_vowels("hello") == 2
assert count_vowels("rhythm") == 0
assert count_vowels("AEIOU") == 5
