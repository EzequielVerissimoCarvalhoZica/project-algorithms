def is_palindrome_recursive(word, low_index, high_index):
    if word == "":
        return False

    if len(word) == 1:
        return True
    
    if high_index == 0:
        return word[low_index]
    
    newWord = word[high_index] + is_palindrome_recursive(word, low_index, high_index - 1)
    
    if newWord == word:
        return True
    elif len(newWord) == len(word):
        return False

    return newWord
