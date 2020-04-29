from firstDetection import launchDetection

def main():

    choice ='0'
    while choice =='0':
        print("Reverse Finder - Recherche d'images sur Internet")
        print("1- Utilisation de la webcam")
        print("2- Envoi d'un fichier")

        choice = input ("Que voulez-vous faire: ")

        if choice == "1":
            print("Ouverture WebCam")
            webcam_menu()
        elif choice == "2":
            print("Envoi Fichier")
        else:
            print("Ce choix n'est pas possible")

def webcam_menu():
    print("Menu Webcam ---")
    launchDetection()

def file_menu():
    print("Menu Fichier ---")


main()