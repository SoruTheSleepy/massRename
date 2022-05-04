# ---------------------------------------------------------------------------------------------------------------------
# Script permettant de supprimer une chaîne de caractère dans le nom de tous les fichiers présents dans le dossier
# dans lequel le script est lancé.
# ---------------------------------------------------------------------------------------------------------------------

import os
import pathlib
import tkinter as tk

class File:
	def __init__(self, path):
		self.path = os.path.abspath(path)
		self.name = os.path.splitext(path)[0]
		self.extension = os.path.splitext(path)[1]

# ---------------------------------------------------------------------------------------------------------------------
#
# ---------------------------------------------------------------------------------------------------------------------
running = True

# Boucle infinie tant que la chaîne de caractères entrée est invalide ou introuvable
while running :
	stringToRemove = str(input("Entrez la chaîne de caractères à retirer : "))
	fileExtension = str(input("Entrez le format de fichiers à affecter : ."))

	# Définition du dossier parent du script
	affectedDirectory = pathlib.Path(__file__).parent.resolve()

	originalFiles = []
	# Définition des fichiers du dossier parent
	for i in range(len(os.listdir(affectedDirectory))):
		# print(os.listdir(affectedDirectory)[i])
		print(os.path.abspath(os.listdir(affectedDirectory)[i]))
		#tmp = File(os.path.abspath(os.listdir(affectedDirectory)[i]))
		#tmp = File(os.listdir(affectedDirectory)[i])
		#print(tmp)
		# originalFiles[i] = File(os.listdir(affectedDirectory))
		# originalFiles.remove(os.path.basename(__file__))
	print("")

	# --------------------------------------------------------
	# PARCOURS DES FICHIERS DU DOSSIER
	# --------------------------------------------------------
	newFiles = []
	errors = 0
	for currentFileName in originalFiles :
		# Old file name
		fileNameBefore = currentFileName
		# print(currentFileName)
		filePathBefore = os.path.abspath(fileNameBefore)
		# if fileExtension != "" and fileExtension == getExtension(oldFile):
		if stringToRemove in fileNameBefore :
			# New file name
			newFile = currentFileName.replace(stringToRemove, "")
			newFilePath = f"{affectedDirectory}\{newFile}"
			# The "First character is space" prevention
			while newFile.startswith(" ") :
				newFile = newFile[1:]
				print(newFile)

			# Tentative de renommage
			try :
				# Changing the old file name to the new file name
				os.rename(filePathBefore, newFilePath)
				# print(oldFile)
				# print(newFile, "\n")
			except OSError :
				# Si un fichier du même nom existe déjà.
				try :
					# Suppression du fichier déjà existant et remplacement par le nouveau.
					os.remove(newFilePath)
					os.rename(filePathBefore, newFilePath)
					print(f"\"{newFile}\" existait déjà. \"{fileNameBefore}\" l'a remplacé.\n")
				except :
					# Si vraiment ça veut pas.
					print("Une erreur est survenue lors de la tentative de suppression de la chaîne de caractères \"{}\" dans \"{}\".\n".format(stringToRemove, currentFileName))
					print("Vérifiez qu'un fichier du même nom n'existe pas déjà.")
			except :
				print("Une erreur est survenue lors de la tentative de suppression de la chaîne de caractères \"{}\" dans \"{}\".\n".format(stringToRemove, currentFileName))
				os.remove()
			finally :
				running = False
		else :
			print("La chaîne de caractères \"{}\" est introuvable dans \"{}\".\n".format(stringToRemove, currentFileName))
			errors += 1
			# chaine = True
			# break
	if errors > 0 :
		print("Nombre d'erreurs : {}/{}".format(errors, len(originalFiles)))

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