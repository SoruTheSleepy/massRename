# ---------------------------------------------------------------------------------------------------------------------
# Script permettant de supprimer une chaîne de caractère dans le nom de tous les fichiers présents dans le dossier
# dans lequel le script est lancé.
# ---------------------------------------------------------------------------------------------------------------------

import os
import pathlib

# --------------------------------------------------------------------------------------------------------------------- #
# ♦ - ♦ - ♦ - ♦ - ♦ - ♦ - ♦ - ♦ - ♦ - ♦ - ♦ - ♦ - ♦ - ♦ - ♦ - ♦ - ♦ - ♦ - ♦ - ♦ - ♦ - ♦ - ♦ - ♦ - ♦ - ♦ - ♦ - ♦ - ♦ - ♦ #
#												M A S S   R E N A M E													#
# ♦ - ♦ - ♦ - ♦ - ♦ - ♦ - ♦ - ♦ - ♦ - ♦ - ♦ - ♦ - ♦ - ♦ - ♦ - ♦ - ♦ - ♦ - ♦ - ♦ - ♦ - ♦ - ♦ - ♦ - ♦ - ♦ - ♦ - ♦ - ♦ - ♦ #
# --------------------------------------------------------------------------------------------------------------------- #

running = True

# Boucle infinie tant que la chaîne de caractères entrée est invalide ou introuvable
while running :
	# La chaîne de caractères à retirer
	
	stringToRemove = input("Entrez la chaîne de caractères à retirer : ")

	# Définition du dossier parent du script
	directory = pathlib.Path(__file__).parent.resolve()

	# Définition des fichiers du dossier parent
	originalFilesList = os.listdir(directory)
	originalFilesList.remove(os.path.basename(__file__))
	print("")

	# Parcours des fichiers du dossier
	newFiles = []
	erreurs = 0
	for file in originalFilesList :
		# Old file name
		oldFile = file
		oldFilePath = os.path.abspath(oldFile)

		if stringToRemove in oldFile :
			# New file name
			newFile = file.replace(stringToRemove, "")
			newFilePath = f"{directory}\{newFile}"
			# The "First character is space" prevention
			while newFile.startswith(" ") :
				newFile = newFile[1:]

			# Tentative de renommage
			try :
				# Changing the old file name to the new file name
				os.rename(oldFilePath, newFilePath)
				# print(oldFile)
				# print(newFile, "\n")
			except OSError :
				# Si un fichier du même nom existe déjà.
				try :
					# Suppression du fichier déjà existant et remplacement par le nouveau.
					os.remove(newFilePath)
					os.rename(oldFilePath, newFilePath)
					print(f"\"{newFile}\" existait déjà. \"{oldFile}\" l'a remplacé.\n")
				except :
					# Si vraiment ça veut pas.
					print("Une erreur est survenue lors de la tentative de suppression de la chaîne de caractères \"{}\" dans \"{}\".\n".format(stringToRemove, file))
					print("Vérifiez qu'un fichier du même nom n'existe pas déjà.")
			except :
				print("Une erreur est survenue lors de la tentative de suppression de la chaîne de caractères \"{}\" dans \"{}\".\n".format(stringToRemove, file))
				os.remove()
			finally :
				running = False
		else :
			print("La chaîne de caractères \"{}\" est introuvable dans \"{}\".\n".format(stringToRemove, file))
			erreurs += 1
			# chaine = True
			# break
	if erreurs > 0 :
		print("Nombre d'erreurs : {}/{}".format(erreurs, len(originalFilesList)))

# Demande de validation des modifications
# print("Le texte \"{}\" a été retiré du nom des fichiers avec succès.\n".format(chaineRetirer))
# reponse = ""
# while (reponse != "o") or (reponse != "n") :
# 	reponse = input("Souhaitez-vous conserver ces modifications ? (o/n) ")
# 	if (reponse == "o") or (reponse == "O") :
# 		break
# 	if (reponse == "n") or (reponse == "N") :
# 		for file, index in enumerate(newFiles) :
# 			file = originalFilesList[index]
# 			print(os.path.abspath(file))
# 		print("Les noms des fichiers originaux a été rétabli.")
# 	else :
# 		print("Entrez une réponse valide !")
# 		continue

print("Script exécuté avec succès.")
os.system("pause")