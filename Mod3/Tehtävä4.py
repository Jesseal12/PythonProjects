vuosi= float(input("Syötä vuosinumeron : "))


if vuosi % 4 == 0 and   vuosi %100!=0  or vuosi % 400 == 0 and vuosi % 100 ==0 :
    print("On karkaus vuosi")
else :
      print(" Ei ole karkaus vuosi")
      