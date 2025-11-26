watch = True

anime =[ ]
while watch == True :
    ask = input("Enter the title of an anime ( or type 'exit' to finish) :").lower()
   
    if ask == 'exit':
        print(f"You have exited the anime entry program")
        print(f"Your anime list includes:")
        for all_anime in anime :
            print(f" - {all_anime}")
        break
        
    else: 
        print(f" '{ask}' has been added to your anime list.")
        anime.append (ask)
        continue
    
    