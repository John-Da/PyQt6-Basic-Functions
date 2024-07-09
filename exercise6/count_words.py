
def count_words(words):
    lowerCase = words.lower()
    wordSplit = lowerCase.split()
    word_list = {}
    wordCount = 0
    for word in wordSplit:
        if word in word_list:
            wordCount += 1
            word_list[word] = wordCount
            return word_list
        else:
            word_list[word] = 1
        




sample_text1 = "The quick brown fox jumps over the lazy dog"
print(count_words(sample_text1))
sample_text2 = "If you believe in somthing and put it in your mind and heart, it can be realised. -Eliud Kipchoge"
print(count_words(sample_text2))