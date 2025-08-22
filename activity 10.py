#bayad sa tricycle

name = input("I-enter mo ang iyong name")
studentba = input("Ikaw ga par ay student? Yes/No")
bayadmo = eval(input("Magkano bayad mo?"))
studentdiscount = bayadmo * 0.2
babayarannalang = bayadmo - studentdiscount

if studentba.lower() == "yes" :
    print("Ang student discount toy/nene ay", studentdiscount, "Ang babayaran mo nalang ay", babayarannalang)
    
else : 
    print(" pasenya na gar, wala kang discount, ang babayaran mo padin ay", bayadmo)