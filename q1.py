def count_vowels_consonants(input):
    vowels=['a','e','i','o','u'] #list of all vowels
    
    vowels_count=0 # set initile value of vowels to 0 
    for x in vowels:
        for y in input:
            if x==y:
                vowels_count+=1
    consonants_count=len(input)-vowels_count #return the count of the vowels

    return vowels_count,consonants_count
if __name__=="__main__":
    result1,result2=count_vowels_consonants("hello")
    print(f"Vowels count is {result1} and consonants count is {result2}")
    


    
    
