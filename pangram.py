message=input("enter any number")
flag= True
if len(message)<=26:
     print("string is not pangram")
else:
    for c in alphabats:
        if c not in message:
            flag=false
            print("sting is not pangram")
            break

if flag ==true:
    print("string is pangram")
