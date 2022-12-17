# import des libraries
import sys
import os

# le repertoire courant
print(f"Vous êtes dans le répertoire: {os.getcwd()}")

try:
    quest = input("Voulez-vous initialiser un git repository dans ce répertoire? O/n: ")

    # si la réponse c'est oui
    if quest.lower() == "o" or quest.lower() == "oui":
        lien_rep = input("Veuillez coller le lien du dépôt: ")
        res_clone = os.system(f"git clone {lien_rep}")

        if res_clone == 128:
            print("pour mettre à jour le projet, supprime le repértoire déjà existant")
    # si la réponse c'est non
    elif quest.lower() == "n" or quest.lower() == "non":
        repo_git = input("Veuillez saisir le chemin de votre répertoire: ")
        os.chdir(repo_git)
        lien_rep = input("Veuillez coller le lien du dépôt: ")
        res_clone = os.system(f"git clone {lien_rep}")
        
        if res_clone == 128:
            print("pour mettre à jour le projet, supprime le repértoire déjà existant")
    # Dans tous les autres cas:
    else:
        print("La réponse doit être o, n, oui ou non!")
except KeyboardInterrupt:
    print("\nAurevoir!")
    sys.exit(1)
except FileNotFoundError:
    print("Le répertoire spécifié n'existe pas")
    sys.exit(2)
except OSError:
    print("La syntax de votre repértoire n'est pas correcte.")
    sys.exit(3)
finally:
    print("Le fichier \"desc_commandes_git.txt\" contient à utiliser si le script ne marche pas")