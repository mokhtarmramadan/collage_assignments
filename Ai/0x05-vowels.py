#Write a Python program to test whether a passed letter is a vowel

char = input("Letter: ")
vowels = ["a", "o", "u", "e", "i"]
if char.lower() in vowels:
    print("{} is a vowel".format(char))
else:
    print("{} is not a vowel".format(char))
