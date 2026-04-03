s = input("Enter a string: ")

vowels = consonants = spaces = lowercase = 0

for ch in s:
    if ch.lower() in 'aeiou':
        vowels += 1
    elif ch.isalpha():
        consonants += 1
    if ch == ' ':
        spaces += 1
    if ch.islower():
        lowercase += 1

print("Vowels:", vowels)
print("Consonants:", consonants)
print("Spaces:", spaces)
print("Lowercase letters:", lowercase)