name = input("Zadej sve jmeno: ")
if(name == "Petr"):
    print("nebudu lhat, hrozne jmeno")

surname = input("Zadej sve prijmeni: ")
if(surname == "Grussmann"):
    print("nebudu lhat, hrozne prijmeni")

os = input("Jaky pouzivas operacni system: ")
if(os == "Linux"):
    print("arch linux lmao")

hair = int(input("Kolik mas vlasu: "))
if((name == "Petr") and (surname == "Grussmann") and (os == "Linux") and (hair == 0)):
    print("petre, odejdi")
else:
    print("bud vitan")