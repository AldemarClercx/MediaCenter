#!/usr/bin/python3
#-*- coding: utf-8 -*-

import os
import re
import shutil

## Variables fixes
Path = "D:/Telechargements/Test"
PathMovies = "D:/Telechargements/Test/A_traiter/Movies"
PathMoviesOk = "D:/Telechargements/Test/Pret_a_regarder/Movies"

def RenameMovies():
    ## Boucle pour lister les dossiers présent dans le repertoire 'Films'
    for EachFolderFilms in os.listdir(PathMovies):
        print (EachFolderFilms)

        ## Boucle pour tester que ca soit bien un dossier
        for FolderName in os.listdir(PathMovies):
            if os.path.isdir(PathMovies+'/'+FolderName)==True:
                FullPath = PathMovies+'/'+FolderName
                #print ("-----")
                print ("\nDans le repertoire '" + FolderName + "' :")

                ## Boucle pour renommer les fichiers avec le nom du repertoire 
                for FilesName in os.listdir(FullPath):        
                    if os.path.isfile(FullPath+'/'+FilesName)==True: ## Test si c'est un fichier              
                        SplitFile = os.path.splitext(FilesName) ## Permet de spliter le nom du fichier avec l'extension. Exemple : ['NomFichier', '.txt']
                        base_name = SplitFile[0] ## Permet de recuperer la base du nom du fichier. Exemple NomFichier.txt : [NomFichier]
                        file_extension = SplitFile[1] ## permet de recuperer l'extension du nom de fichier. Exemple NomFichier.txt : [.txt]
                        OldName = FilesName ## Variable pour le renommage (Nom actuel)
                        NewName = FolderName+file_extension ## Variable pour le renommage (Nouveau nom)    
                        shutil.move(FullPath+'/'+OldName, PathMoviesOk+'/'+NewName)
                        print ("Le film " + OldName + " est renommé en " + NewName)
                shutil.rmtree(FullPath)      