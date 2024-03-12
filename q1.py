def count_vowels_consonants(input_string):
    # List of all vowels
    vowels = ['a', 'e', 'i', 'o', 'u']
    
    # Initialize count of vowels to 0
    vowel_count = 0 
    
    # Loop through each vowel
    for vowel in vowels:
        # Loop through each character in the input string
        for char in input_string:
            # If the character is a vowel, increment the vowel count
            if vowel == char:
                vowel_count += 1
    
    # Count of consonants is the total length of input string minus vowel count
    consonant_count = len(input_string) - vowel_count 
    
    # Return the counts of vowels and consonants
    return vowel_count, consonant_count

if __name__ == "__main__":
    # Test the function with input "hello"
    result1, result2 = count_vowels_consonants("hello")
    
    # Print the counts of vowels and consonants
    print(f"The count of vowels is {result1} and the count of consonants is {result2}.")
