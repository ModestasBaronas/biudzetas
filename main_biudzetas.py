from katalogas.biudzetas import Biudzetas


mano_biudzetas = Biudzetas()

while True:
    print("iveskite veiksma:")
    print("1 - Gautos pajamos")
    print("2 - Ivesti išlaidas")
    print("3 - Balansas")
    print("4 - Ataskaita")
    print("0 - Exit")
    chose = input()
    if chose == "1":
        print("Iveskite pajamas: ")
        suma = int(input("Suma: "))
        siuntejas = input("Siuntejas: ")
        info = input("Informacija: ")
        mano_biudzetas.pajamos(suma, siuntejas, info)
        print("Pajamos ivestos sekmingai.")
    if chose == "2":
        print("Iveskite išlaidas: ")
        suma = int(input("Suma: "))
        atsiskaitymo_metodas = input("Atsiskaitymo budas: ")
        preke_paslauga = input("Isigyta preke/paslauga: ")
        mano_biudzetas.islaidos(suma, atsiskaitymo_metodas, preke_paslauga)
        print("Išlaidos ivestos sekmingai.")
    if chose == "3":
        print(f"Saskaitos balansas: {mano_biudzetas.biudzeto_balansas()}")
    if chose == "4":
        mano_biudzetas.ataskaita()
    if chose == "0":
        break
