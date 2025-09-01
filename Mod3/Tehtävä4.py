vuosi= int(input("Syötä vuosinumeron : "))


if (vuosi % 4 == 0 and   vuosi %100!=0)  or vuosi % 400 == 0  :
    # katsoo et ei ole jakojäänosta ja että ei ole jaettava 100 eli ei vuosisata
    # sit menemme isompii lukuihin ja tarkistetaan ne vuosisata säänoillä
 #luettavuus on kivempi ja ei valita suluista
    print("On karkaus vuosi")
else :
      print(" Ei ole karkaus vuosi")
