def encode(password):
    p=password
    final=""
    for letter in p:
        final+=str(int(letter)+3)
    return final
def decode(code):
    deco = ''
    for i in range(len(code)):
        if int(code[i])-3 <= 0:
            deco += str(int(code[i])-3 + 10)
        else:
            deco += str(int(code[i])-3)

while True:
    print("Menu")
    print("-------------")
    print("1. Encode")
    print("2. Decode")
    print("3. Quit")
    print("")
    choice=int(input("Please enter an option: "))
    if choice==1:
        password=input("Please enter your password to encode: ")
        final=encode(password)
        print("Your password has been encoded and stored!")
    if choice==2:
        print(f"The encoded password is {final} and the decoded password is {decode(final)} ")
    if choice==3:
        break
