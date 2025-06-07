def afficher_menu ():
    print("que souhaitez_vous boir ?")
    print(" 1- Café ")
    print(" 2- thé ")
    print(" 3- Eau chaude ")
    print(" 4- quitter le menu ")

def gerer_choix () :
      commandes = []
      while True:
            afficher_menu()
            choix = int(input("Entrez votre choix des  menu : "))
            if choix==1:
                  print("votre choix  est Cafe")
                  commandes.append("Café")
            elif choix==2:       
                  print ("votre choix est thé")
                  commandes.append("Thé")
            elif choix==3:
                  print ("votre choix est eau chaude")
                  commandes.append("Eau chaude")
            elif  choix==4: 
                  print (" votre choix est de quitez la menu ")
                  break
            else :
                  print("choix invalider")
            print ("\n votre toutes les commandes sont : ")

      if commandes:
            computeur = {}
            pluriel={"Café": "cafés", "Thé":"thés", "Eau chaude": "Eau chaudes"}
            historique={}
            for boissons in commandes :
                  computeur[boissons]= computeur.get(boissons, 0) + 1
            for boissons, nombre in computeur.items( ):
                    nom_boissons = boissons if nombre==1 else pluriel.get(boissons, "s")
                    historique[nom_boissons] = nombre
            print(historique)
            

      else :
            print("Aucune menu n'a été commandes .")