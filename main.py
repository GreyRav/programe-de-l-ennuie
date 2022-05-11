import time
import webbrowser

#presentation
print("Presentation du programme anti-ennui en 3 catégorie.\nLe premier sera les films.\nLe deuxieme, Les jeux vidéos.\nEt le troisieme, les reseaux sociaux (sociaux)")

#variable des categorie
game = "Read Dead; " "Need For Speed; " "CS GO; " "Call of duty; " "The Witcher; " "Dark Soul; "

film = "Titanic; " "Pianiste; " "Spider Man; "

reseaux = "TikTok; " "Youtube; " "Twitch; " "Snap; " "Instagram; "

#debut du programme

print("C'est differente catégorie sont sous trois nom: \nGame pour les jeux vidéos.\nFilm pour les fims.\nEt Reseaux pour les reseaux sociaux.\n\n")

choix = input("Que va tu choisir ce soir ?\n")


if choix == "game":
    print("Ce soir ce sera donc jeux vidéo, c'est partie...\n")
    time.sleep(2)
    print(game)
    input("Appuie sur entrée pour continuer le programme. ;)")

elif choix == "Game":
    print("Ce soir ce sera donc jeux vidéo, c'est partie...\n")
    time.sleep(2)
    print(game)
    input("Appuie sur entrée pour continuer le programme. ;)")

elif choix == "Reseaux":
    print("Ce soir ce sera donc les reseaux saociaux, c'est partie...\n")
    time.sleep(2)
    print(reseaux)
    input("Appuie sur entrée pour continuer le programme. ;)")

elif choix == "reseaux":
    print("Ce soir ce sera donc les reseaux saociaux, c'est partie...\n")
    time.sleep(2)
    print(reseaux)
    input("Appuie sur entrée pour continuer le programme. ;)")

elif choix == "film":
    print("Ce soir ce sera donc un film, c'est partie...\n")
    time.sleep(2)
    print(film)
    if input("Tu veux ouvrir netfix ? ") == "oui" or "y" or "ok":
        time.sleep(2)
        webbrowser.open("https://www.netflix.com/browse")


    else:
        input("Appuie sur entrée pour continuer le programme. ;)")

elif choix == "Film":
    print("Ce soir ce sera donc un film, c'est partie...\n")
    time.sleep(2)
    print(film)
    if input("Tu veux ouvrir netfix ? ") == "oui" or "y" or "ok":
        time.sleep(2)
        webbrowser.open("https://www.netflix.com/browse")


    else:
        input("Appuie sur entrée pour continuer le programme. ;)")

else:
    print("je n'ai pas compris, désolée.")
    input("tape entrée pour quitter.")
    time.sleep(2)

print("Pour toute demande de rajout de jeux, de film, ou de reseaux sociaux ou de nouvelle catégorie. N'hesité pas a m'ajouter sur discord: MisterRaven#5442\nEt si le code vous interesse, c'est sur mon github: https://github.com/GreyRav/Programme-De-L-ennuie.git.\n")
if input("Tu veux que j'ouvre github ?: ") == "oui" or "y" or "ok":
    print("okay je te l'ouvre...")
    time.sleep(2)
    webbrowser.open("https://github.com/GreyRav/Programme-De-L-ennuie.git")
else:
    print("okay")

print("sur ce bonne soirée ;)\n")
input("Appuie sur entrée pour quitter.")
exit()
