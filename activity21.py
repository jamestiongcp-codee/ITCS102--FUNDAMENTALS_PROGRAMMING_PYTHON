dirty = True 
askk= input("type yes to start").lower()
if askk == "yes":
    while dirty == True:
        ask = input(" do you want to continue? (yes/no)").lower()
        if ask == "yes":
            print("Continue cycle")
            continue
        
        elif ask == "no":
            print("End cycle")
            break
    
        else:
            print("invalid input")
            continue
else: 
    print("edi don't")