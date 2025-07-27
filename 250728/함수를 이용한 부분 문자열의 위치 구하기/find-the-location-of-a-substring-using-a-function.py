def find_substring(text, pattern):
    text_len = len(text)
    pattern_len = len(pattern)

    for i in range(text_len - pattern_len + 1):
        if text[i:i+pattern_len] == pattern:
            return i
    
    return -1


text = input()
pattern = input()

print(find_substring(text, pattern))
