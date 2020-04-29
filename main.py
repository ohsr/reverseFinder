import argparse
from firstDetection import launchDetection

def main():
    print("Reverse Finder - Recherche d'images sur Internet")
    parser = argparse.ArgumentParser()
    parser.add_argument("-c", "--cam", action="store_true", help="Envoi d'un fichier pour une recherhe sur internet")
    parser.add_argument("-f", "--file", help="Envoi d'un fichier pour une recherhe sur internet")

    args = parser.parse_args()
    if args.cam:
        webcam_menu()
    elif args.file:
        file_menu()

def webcam_menu():
    print("-- Ouverture Webcam ---")
    launchDetection()

def file_menu():
    print("Menu Fichier ---")


if __name__ == "__main__":
    main()