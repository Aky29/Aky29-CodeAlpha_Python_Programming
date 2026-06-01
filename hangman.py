secret_word = input("Enter the secret word : ")
for _ in range(5):
    user_guess = input("Guess the word : ")
    for i in range(len(user_guess)):
        if user_guess[i] == secret_word[i]:
            print(user_guess[i],end="")
        else:
            print("_",end = "")
    print("")
