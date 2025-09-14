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
    