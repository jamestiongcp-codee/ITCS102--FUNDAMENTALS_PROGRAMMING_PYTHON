def lists():
    while True:
        print("Please select:\nA - Description\nB - Sample code\nC - Result of sample code\nD - Back")
        choicee = input("Your choice-->").lower()

        if choicee == 'a':
            print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++") 
            print('list is a versatile, built-in data structure used to store an ordered collection of items that can be of different data types. Lists are defined using square brackets and their items are accessed via zero-based indexing.')
            print("\n\nCommon List Methods:\nPython provides several built-in methods to manipulate lists.\n\n.append(item): Adds a single item to the end of the list\n\n.insert(index, item): Inserts an item at a specified position.\n\n.remove(item): Removes the first occurrence of a specified value\n\n.pop(index): Removes the item at the specified position and returns it. If no index is specified, it removes and returns the last item.\n\n.sort(): Sorts the list in place (modifies the original list). The built-in sorted() function returns a new sorted list without changing the original.\n\n.reverse(): Reverses the order of elements in place.")
            print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++") 
        elif choicee == 'b':
            while True:
                print('Please select:\n1. List methods\n2. Anime Entry Program\n3. Back')
                ask = input("Enter choice-->")
                if ask == '1':
                    print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++") 
                    print("""months = ['jan','feb','mar','apr','may','jun']

months.append('jul')
print(months)

months.remove('jan')
print(months)

months.pop()
print(months)
  
for m in months:
     print(f"{m} ,2025")
     
full_name = 'James Francis M. Tiongco'

namee = list(full_name)

namee.reverse()
print(namee)""")
                    print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++") 
                elif ask == '2':
                    print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++") 
                    print("""watch = True

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
    """)
                    print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++") 
                elif ask == '3':
                    break
                else:
                    print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++") 
                    print("Invalid Choice")
                    print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++") 

        elif choicee == 'c':
            while True:
                print('Please select:\n1. List methods\n2. Anime Entry Program\n3. Back')
                ask = input("Enter choice-->")
                if ask == '1':
                    print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++") 
                    months = ['jan','feb','mar','apr','may','jun']

                    months.append('jul')
                    print(months)

                    months.remove('jan')
                    print(months)

                    months.pop()
                    print(months)
                    
                    for m in months:
                        print(f"{m} ,2025")
                        
                    full_name = 'James Francis M. Tiongco'
                    namee = list(full_name)
                    namee.reverse()
                    print(namee)
                    print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++") 
                elif ask == '2':
                    print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++") 
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
                    print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++") 
                elif ask == '3':
                    break
                else:
                    print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++") 
                    print("Invalid Choice")
                    print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++") 

        elif choicee == 'd':
            break
        else:
            print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++") 
            print("Invalid Choice")
            print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++") 
