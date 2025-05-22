from boissons import affiche_menu, traite_choix

def main():
    while True:
        affiche_menu()
        choix = input("Entrez votre choix des  menu : ")
        if choix == "4":
            traite_choix(choix)
            break
        dernier_choix = traite_choix(choix)
        print()  

        if dernier_choix:
           print(f"\nRésumé : Votre dernier choix était : {dernier_choix}. Merci et à bientôt !")

if __name__ == "__main__":
    main()


                                                                                      