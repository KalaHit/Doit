message=input("enter any number")
flag= True
alphabets = "abcdefghijklmnopqrstuvwxyz"

if len(message)<=26:
     print("string is not pangram")
else:
    for c in alphabets:
        if c not in message:
            flag=False
            print("sting is not pangram")
            break

if flag == True:
    print("string is pangram")
