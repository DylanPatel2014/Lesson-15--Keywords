word=input("Please write a word to check:")
for i in word:
    if i=="a"or i=="A":
        print("A is found in your word.")
        break
    else:
        print("A is not found in your word.")