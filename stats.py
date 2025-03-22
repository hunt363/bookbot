def get_word_count(text):
    return len(text.split())

def get_char_count(text):
    char_count={}
    text=text.lower()
    for char in text:
        if char in char_count:
            char_count[char]+=1
        else:
            char_count[char]=1
        
    
    return dict(sorted(
        char_count.items(),
        key=lambda x: x[1],
        reverse=True
    ))
    