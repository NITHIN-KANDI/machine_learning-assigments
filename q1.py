def count_vowels_consonants(input):
    # List of all vowels
    vowels = ['a', 'e', 'i', 'o', 'u']
    
    # Initialize count of vowels to 0
    vowels_count = 0 
    
    # Loop through each vowel
    for x in vowels:
        # Loop through each character in the input string
        for y in input:
            # If the character is a vowel, increment the vowel count
            if x == y:
                vowels_count += 1
    
    # Count of consonants is the total length of input string minus vowel count
    consonants_count = len(input) - vowels_count 
    
    # Return the counts of vowels and consonants
    return vowels_count, consonants_count

if __name__ == "__main__":
    # Test the function with input "hello"
    result1, result2 = count_vowels_consonants("hello")
    
    # Print the counts of vowels and consonants
    print(f"Vowels count is {result1} and consonants count is {result2}")
