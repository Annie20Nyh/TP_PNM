def affiche_menu ():
    
    print("que souhaitez_vous boir ?")
    print(" 1- Cafe ")
    print(" 2- the ")
    print(" 3- Eau chaude ")
    print(" 4- quitter ")


def traite_choix (choix) :
    if   choix == "1" :
          print("  votre choix  est Cafe ")
    elif choix == "2" :       
           print (" votre choix est the ")
    elif choix == "3" :
           print (" votre choix est eau chaude ")
    elif  choix == "4"  : 
           print (" votre choix est de quitez  ")
           return "Quitter"
    else : 
          print ( " choix invalide")
          return None



      

           

    