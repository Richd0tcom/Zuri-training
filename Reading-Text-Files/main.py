# Read text from a file, and count the occurence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!") 
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}

def read_file_content(filename):
    # [assignment] Add your code here 
        return open(filename).read()

def count_words():
    text = read_file_content("./story.txt")
    # [assignment] Add your code here
    

    counter={}
    for letter in text.split():
        if letter in counter:
            counter[letter] +=1
        else:
            counter[letter] = 1

    return counter


print(count_words())