# Check if two words are anagrams 
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True


def find_anagram(word, anagram):
    # [assignment] Add your code here
    if len(word)!= len(anagram):
        return False
        
    word =  sorted(word)
    anagram = sorted(anagram)
    for i in range(len(word)-1):
        if word[i]!=anagram[i]:
            return False

    return True


print(find_anagram('elephant','elehpant'))