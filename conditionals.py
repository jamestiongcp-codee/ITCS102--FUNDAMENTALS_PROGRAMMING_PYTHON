def cond():
    while True: 
        print("Please select:\nA - Description\nB - Sample code\nC - Result of sample code\nD - Back")
        choicee = input("Your choice-->").lower()
                        
        if choicee == 'a':
            print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
            print('\n\n')
            print('Conditional statements in Python allow for the execution of specific code blocks based on whether a given condition evaluates to True or False. This mechanism enables decision-making within a program, leading to different behaviors depending on various inputs or states.The primary conditional statements in Python are if, elif, and else.')
            print('\n1. if Statement:\n\nThe if statement is the most basic form. It executes a block of code only if its condition is True.\n2. if-else Statement:\n\nThe if-else statement provides an alternative block of code to execute when the if condition is False.\n3. if-elif-else Statement:\n\nThe if-elif-else statement allows for checking multiple conditions sequentially. If the if condition is False, the program checks the elif conditions in order. If none of the if or elif conditions are True, the else block (if present) is executed.')
            print('\n\n')
            print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")        
        elif choicee == 'b':
            while True: 
                print("Please select:\n1. Transportation fee\n2. Temperature\n3. Logging in\n4. Even or Odd Guesser\n5. Manga Recommendation\n6. Back")
                pick = input("Enter choice-->")
                                
                if pick == '1':
                    print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
                    print('name = input("I-enter mo ang iyong name")')
                    print('studentba = input("Ikaw ga par ay student? Yes/No")')
                    print('bayadmo = eval(input("Magkano bayad mo?"))')
                    print('studentdiscount = bayadmo * 0.2')
                    print('babayarannalang = bayadmo - studentdiscount')

                    print('if studentba.lower() == "yes" :')
                    print('\tprint("Ang student discount toy/nene ay", studentdiscount, "Ang babayaran mo nalang ay", babayarannalang)')
    
                    print('else :') 
                    print('\tprint(" pasenya na gar, wala kang discount, ang babayaran mo padin ay", bayadmo)')
                    print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
                                                
                elif pick == '2':
                    print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
                    print('temp = eval(input("Enter Temperature -->"))')

                    print('if temp >= 1 and temp <=20 :')
                    print('\tprint("The temperature outside is cold", "malamig")')
                    print('elif temp >=21 and temp <=30:')
                    print('\tprint("The temperature outside is lukewarm")')
                    print('elif temp >=31 and temp <=40:')
                    print('\tprint("The temperature outside is warmmm")')
                    print('elif temp >=41 and temp <=50:')
                    print('\tprint("The temperature outside is hot")')
                    print('elif temp >=51:')
                    print('\tprint("The temperatute outside is boiling hot, kumukulongg tubigg")')
                    print('else:')    
                    print('\tprint("Invalid temperature")')
                    print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
                                    
                elif pick == '3':
                    print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
                    print('username = "dragonslayer" ')
                    print('password =  "demonslayer" ')

                    print('name = input(" Enter your Username ->")')
                    print('passw = input(" Enter your password ->")')

                    print('if name == username and passw == password :')
                    print('\tprint("Acess Granted")')
    
                    print('else :')
                    print('\tprint("Acess Denied")')
                    print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
                    
                elif pick == '4':
                    print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
                    print('numb = eval(input("Enter a number"))')

                    print('if numb %2 == 0 :')
                    print('\tprint("The number is even")')
    
                    print('else :')
                    print('\tprint("The number is odd")')
                    print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")  
                elif pick == '5':
                    print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
                    print(r"""print(" Welcome to the Manga Reader Recommencation")
print(" Answer some questions to find your next read")
genre = input("What genre do you want? (Romance, Comedy, Action)").lower()
if genre == "romance" : 
    length = input("How long should the manga be? (Short, Medium, Long)").lower()
    if length == "short" :
        decade = input("what decade? (2010s, 2020s)")
        if decade == "2010s" or decade == "2010" :
            print("Here are some short romance manga in the 2010s")
            print(" 1. I Still Haven’t Experienced a Kiss Yet\n2. Midnight Coin Laundry\n3. About My Month With Aioi Wakaba")
        else :
            print("Here are some short romance manga in the 2020s")
            print("1. The Fragrant Flower Blooms with Dignity\n2.Kamibukuro-kun wa Koishiteru\n3. Lovesick Ellie")
    elif length == "medium" :
        decadee = input("what decade? (2010s,2020s)")
        if decadee == "2010s" or decadee =="2010" :
            print("Here are some medium romance manga in the 2010s ")
            print("1. Horimiya\n2.Say I Love You\n3. Kimi ni Todoke")
        else : 
             print("Here are some medium romance manga in the 2020s")
             print("1. Ao no Hako (Blue Box)\n2.Boku ga Otto ni Deau made\n3. Kimi no Yoru ni Fureru")
    else : #long
        decadeee = input("what decade? (2010s, 2020s)")
        if decadeee == "2010s" or decadeee == "2010":
            print("Here are some long romance manga in the 2010s")
            print("1.Kaguya-sama: Love is War\n2. Wolf Girl and Black Prince\n3. Ao Haru Ride")
        else : 
            print("Here are some long romance manga in the 2020s")
            print("1. Kaoru Hana wa Rin to Saku\n2. Uruwashi no Yoi no Tsuki\n3. Kimi no Koto nado Zettai ni\n4. Otonari no Tenshi-sama ni Itsunomanika Dame Ningen ni Sareteita Ken\n5. Kimi to Tsuzuru Utakata")  
elif genre == "comedy": 
    length = input("How long should the manga be? (Short, Medium, Long)").lower()
    if length == "short" :
        decade = input("what decade? (2010s, 2020s)")
        if decade == "2010s" or decade == "2010" :
            print("Here are some short comedy manga in the 2010s")
            print("1. A Silent Voice\n2. Detroit Metal City\n3. Nichijou ")
        else :
            print("Here are some short comedy manga in the 2020s")
            print("1. Sayonara Eri\n2. Look Back\n3. Goukon ni Ittara Onna ga Inakatta Hanashi")
    elif length == "medium" :
        decadee = input("what decade? (2010s,2020s)")
        if decadee == "2010s" or decadee =="2010" :
            print("Here are some medium comedy manga in the 2010s ")
            print("1. Mob Psycho 100\n2. Assassination Classroom\n3. Wotakoi: Love is Hard for Otaku")
        else : 
             print("Here are some medium comedy manga in the 2020s")
             print("1. Sakamoto Days\n2. Akane-banashi\n3. Super no Ura de Yani Suu Futari")
    else : #long
        decadeee = input("what decade? (2010s, 2020s)")
        if decadeee == "2010s" or decadeee == "2010":
            print("Here are some long comedy manga in the 2010s")
            print("1. Gintama\n2. Komi Can’t Communicate\n3. The Disastrous Life of Saiki K.")
        else : 
            print("Here are some long comedy manga in the 2020s")
            print("1. Spy x Family\n2. Dandadan\n3. Oshi no Ko")  
else : #action
    length = input("How long should the manga be? (Short, Medium, Long)").lower()
    if length == "short" :
        decade = input("what decade? (2010s, 2020s)")
        if decade == "2010s" or decade == "2010" :
            print("Here are some short action manga in the 2010s")
            print("1. Apocalypse no Toride\n2. Akame ga Kill!\n3. Imawa no Kuni no Alice")
        else :
            print("Here are some short action manga in the 2020s")
            print("1. Sayonara Eri\n2. Look Back\n3. Ayashimon\n4. Dorondororon\n5. Neru: Bugei Dogyou")
    elif length == "medium" :
        decadee = input("what decade? (2010s,2020s)")
        if decadee == "2010s" or decadee =="2010" :
            print("Here are some medium action manga in the 2010s ")
            print("1. Mob Psycho 100\n2. Tokyo Ghoul\n3. Fire Punch")
        else : 
             print("Here are some medium action manga in the 2020s")
             print("1. Mashle: Magic and Muscles\n7. Kaiju No. 8\n2. Undead Unluck\n3. Gachiakuta\n4. Gokurakugai")
    else : #long
        decadeee = input("what decade? (2010s, 2020s)")
        if decadeee == "2010s" or decadeee == "2010":
            print("Here are some long action manga in the 2010s")
            print("1. My Hero Academia\n2. Demon Slayer: Kimetsu no Yaiba\n3. Black Clover")
        else : 
            print("Here are some long action manga in the 2020s")
            print("1. Dandadan\n2. Sakamoto Days\n3. Shangri-La Frontier\n4. Wind Breaker\n5. Yomi no Tsugai")""")  
                    print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
                elif pick == '6':
                    break                                                                                
                else:
                    print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
                    print('Invalid choice')
                    print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")                             
        elif choicee == 'c':
            while True: 
                print("Please select:\n1. Transportation fee\n2. Temperature\n3. Logging in\n4. Even or Odd Guesser\n5. Manga Recommendation\n6. Back")
                pick = input("Enter choice-->")
                                
                if pick == '1':
                    print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
                    name = input("I-enter mo ang iyong name")
                    studentba = input("Ikaw ga par ay student? Yes/No")
                    bayadmo = eval(input("Magkano bayad mo?"))
                    studentdiscount = bayadmo * 0.2
                    babayarannalang = bayadmo -studentdiscount

                    if studentba.lower() == "yes" :
                        print("Ang student discount toy/nene ay", studentdiscount, "Ang babayaran mo nalang ay", babayarannalang)
    
                    else : 
                        print(" pasenya na gar, wala kang discount, ang babayaran mo padin ay", bayadmo)
                    print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")                                                                                                                                                                                                                                                                                                                                      
                elif pick == '2':
                    print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
                    temp = eval(input("Enter Temperature -->"))

                    if temp >= 1 and temp <=20 :
                        print("The temperature outside is cold", "malamig")
                    elif temp >=21 and temp <=30:
                        print("The temperature outside is lukewarm")
                    elif temp >=31 and temp <=40:
                        print("The temperature outside is warmmm")
                    elif temp >=41 and temp <=50:
                        print("The temperature outside is hot")
                    elif temp >=51:
                        print("The temperatute outside is boiling hot, kumukulongg tubigg")
                    else: 
                        print("Invalid temperature")
                    print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")            
                elif pick == '3':
                    print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
                    username = 'dragonslayer'
                    password =  'demonslayer'


                    name = input(" Enter your Username ->")
                    passw = input(" Enter your password ->")

                    if name == username and passw == password :
                        print("Acess Granted")
    
                    else :
                       print("Acess Denied")
                    print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")  
                elif pick == '4':
                    print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
                    numb = eval(input("Enter a number"))

                    if numb %2 == 0 :
                        print("The number is even")
    
                    else :
                        print("The number is odd")
                    print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")                                                                           
                elif pick == '5':
                    print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
                    print(" Welcome to the Manga Reader Recommencation")
                    print(" Answer some questions to find your next read")
                    genre = input("What genre do you want? (Romance, Comedy, Action)").lower()
                    if genre == "romance" : 
                        length = input("How long should the manga be? (Short, Medium, Long)").lower()
                        if length == "short" :
                            decade = input("what decade? (2010s, 2020s)")
                            if decade == "2010s" or decade == "2010" :
                                print("Here are some short romance manga in the 2010s")
                                print(" 1. I Still Haven’t Experienced a Kiss Yet\n2. Midnight Coin Laundry\n3. About My Month With Aioi Wakaba")
                            else :
                                print("Here are some short romance manga in the 2020s")
                                print("1. The Fragrant Flower Blooms with Dignity\n2.Kamibukuro-kun wa Koishiteru\n3. Lovesick Ellie")
                        elif length == "medium" :
                            decadee = input("what decade? (2010s,2020s)")
                            if decadee == "2010s" or decadee =="2010" :
                                print("Here are some medium romance manga in the 2010s ")
                                print("1. Horimiya\n2.Say I Love You\n3. Kimi ni Todoke")
                            else : 
                                 print("Here are some medium romance manga in the 2020s")
                                 print("1. Ao no Hako (Blue Box)\n2.Boku ga Otto ni Deau made\n3. Kimi no Yoru ni Fureru")
                        else : #long
                            decadeee = input("what decade? (2010s, 2020s)")
                            if decadeee == "2010s" or decadeee == "2010":
                                print("Here are some long romance manga in the 2010s")
                                print("1.Kaguya-sama: Love is War\n2. Wolf Girl and Black Prince\n3. Ao Haru Ride")
                            else : 
                                print("Here are some long romance manga in the 2020s")
                                print("1. Kaoru Hana wa Rin to Saku\n2. Uruwashi no Yoi no Tsuki\n3. Kimi no Koto nado Zettai ni\n4. Otonari no Tenshi-sama ni Itsunomanika Dame Ningen ni Sareteita Ken\n5. Kimi to Tsuzuru Utakata")  
                    elif genre == "comedy": 
                        length = input("How long should the manga be? (Short, Medium, Long)").lower()
                        if length == "short" :
                            decade = input("what decade? (2010s, 2020s)")
                            if decade == "2010s" or decade == "2010" :
                                print("Here are some short comedy manga in the 2010s")
                                print("1. A Silent Voice\n2. Detroit Metal City\n3. Nichijou ")
                            else :
                                print("Here are some short comedy manga in the 2020s")
                                print("1. Sayonara Eri\n2. Look Back\n3. Goukon ni Ittara Onna ga Inakatta Hanashi")
                        elif length == "medium" :
                            decadee = input("what decade? (2010s,2020s)")
                            if decadee == "2010s" or decadee =="2010" :
                                print("Here are some medium comedy manga in the 2010s ")
                                print("1. Mob Psycho 100\n2. Assassination Classroom\n3. Wotakoi: Love is Hard for Otaku")
                            else : 
                                 print("Here are some medium comedy manga in the 2020s")
                                 print("1. Sakamoto Days\n2. Akane-banashi\n3. Super no Ura de Yani Suu Futari")
                        else : #long
                            decadeee = input("what decade? (2010s, 2020s)")
                            if decadeee == "2010s" or decadeee == "2010":
                                print("Here are some long comedy manga in the 2010s")
                                print("1. Gintama\n2. Komi Can’t Communicate\n3. The Disastrous Life of Saiki K.")
                            else : 
                                print("Here are some long comedy manga in the 2020s")
                                print("1. Spy x Family\n2. Dandadan\n3. Oshi no Ko")  
                    else : #action
                        length = input("How long should the manga be? (Short, Medium, Long)").lower()
                        if length == "short" :
                            decade = input("what decade? (2010s, 2020s)")
                            if decade == "2010s" or decade == "2010" :
                                print("Here are some short action manga in the 2010s")
                                print("1. Apocalypse no Toride\n2. Akame ga Kill!\n3. Imawa no Kuni no Alice")
                            else :
                                print("Here are some short action manga in the 2020s")
                                print("1. Sayonara Eri\n2. Look Back\n3. Ayashimon\n4. Dorondororon\n5. Neru: Bugei Dogyou")
                        elif length == "medium" :
                            decadee = input("what decade? (2010s,2020s)")
                            if decadee == "2010s" or decadee =="2010" :
                                print("Here are some medium action manga in the 2010s ")
                                print("1. Mob Psycho 100\n2. Tokyo Ghoul\n3. Fire Punch")
                            else : 
                                 print("Here are some medium action manga in the 2020s")
                                 print("1. Mashle: Magic and Muscles\n7. Kaiju No. 8\n2. Undead Unluck\n3. Gachiakuta\n4. Gokurakugai")
                        else : #long
                            decadeee = input("what decade? (2010s, 2020s)")
                            if decadeee == "2010s" or decadeee == "2010":
                                print("Here are some long action manga in the 2010s")
                                print("1. My Hero Academia\n2. Demon Slayer: Kimetsu no Yaiba\n3. Black Clover")
                            else : 
                                print("Here are some long action manga in the 2020s")
                                print("1. Dandadan\n2. Sakamoto Days\n3. Shangri-La Frontier\n4. Wind Breaker\n5. Yomi no Tsugai")  
                    print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")        
                elif pick == '6':
                    break

                else:
                    print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
                    print('Invalid choice')
                    print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")                            
                                                                                        
        elif choicee == 'd':
            break
        else:
            print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
            print('Invalid choice')
            print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")                                                                                                                                                                                                                                                                                                                
                                                                                                   
           
            
      
            