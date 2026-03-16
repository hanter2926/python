char = input("Ek letter enter : ").lower()
if len(char) == 1 and char.isalpha():
    vowels = "aeiou"
    
    if char in vowels:
        print(f"{char}  Vowel.")
    else:
        print(f"{char}  Consonant .")
else:
    print(" Enter you alphabet letter.")