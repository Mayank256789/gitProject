def check_spelling(correct_word, contestant_word):
     
     if len(correct_word) != len(contestant_word):
        
        return f"{contestant_word} IS WRONG"
    
    wrong_count = sum(1 for c1, c2 in zip(correct_word, contestant_word) if c1 != c2)
    
    if wrong_count == 0:
        return f"{contestant_word} IS CORRECT"
    elif wrong_count <= 2:
        return f"{contestant_word} IS ALMOST CORRECT"
    else:
        return f"{contestant_word} IS WRONG"

# Read input
correct_word = input().strip()
contestant_word = input().strip()

# Get result and print
result = check_spelling(correct_word, contestant_word)
print(result)
