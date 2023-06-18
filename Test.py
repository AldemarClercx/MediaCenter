#!/usr/bin/python3
#-*- coding: utf-8 -*-

import os

## Variables fixes
Path = "D:/Telechargements/Test"
PathFilms = "D:/Telechargements/Test/Films"
PathSeries = "D:/Telechargements/Test/Series"



##################
## Partie Films ##
##################
## Condition permettant de savoir si c'est le repertoire 'Films'
if PathFilms == "D:/Telechargements/Test/Films":
    ## Condition pour savoir si il y a des films dans le dossier
    if len(os.listdir(PathFilms)) > 0:
        print ("Il y a " + str(len(os.listdir(PathFilms))) + " dossiers dans le repertoire 'Films'. Voici la liste des dossiers présent :")
    
    ## Boucle pour lister les dossiers présent dans le repertoire 'Films'
    for EachFolderFilms in os.listdir(PathFilms):
        print (EachFolderFilms)

    ## Boucle pour tester que ca soit bien un dossier
    for FolderName in os.listdir(PathFilms):
        if os.path.isdir(PathFilms+'/'+FolderName)==True:
            FullPath = PathFilms+'/'+FolderName
            #print ("-----")
            print ("\nDans le repertoire '" + FolderName + "' :")

            ## Boucle pour renommer les fichiers avec le nom du repertoire 
            for count, FilesName in enumerate (os.listdir(FullPath)):        
                if os.path.isfile(FullPath+'/'+FilesName)==True: ## Test si c'est un fichier              
                    SplitFile = os.path.splitext(FilesName) ## Permet de spliter le nom du fichier avec l'extension. Exemple : ['NomFichier', '.txt']
                    base_name = SplitFile[0] ## Permet de recuperer la base du nom du fichier. Exemple NomFichier.txt : [NomFichier]
                    file_extension = SplitFile[1] ## permet de recuperer l'extension du nom de fichier. Exemple NomFichier.txt : [.txt]
                    OldName = FilesName ## Variable pour le renommage (Nom actuel)
                    NewName = FolderName+"_"+str(count)+file_extension ## Variable pour le renommage (Nouveau nom)    
                    os.rename(FullPath+'/'+OldName, FullPath+'/'+NewName)
                    print ("Le film " + OldName + " est renommé en " + NewName)



###################
## Partie Séries ##
###################
## Condition permettant de savoir si c'est le repertoire 'Series'
if PathSeries == "D:/Telechargements/Test/Series":
    ## Condition pour savoir si il y a des films dans le dossier
    if len(os.listdir(PathSeries)) > 0:
        print ("\n\nIl y a " + str(len(os.listdir(PathSeries))) + " dossiers dans le repertoire 'Series'. Voici la liste des dossiers présent :")
    ## Boucle pour lister les dossiers présent dans le repertoire 'Series'
    for EachFolderSeries in os.listdir(PathSeries):
        print (EachFolderSeries)

    ## Boucle pour tester que ca soit bien un dossier
    for FolderName in os.listdir(PathSeries):
        if os.path.isdir(PathSeries+'/'+FolderName)==True:
            FullPath = PathSeries+'/'+FolderName
            #print ("-----")
            print ("\nDans le repertoire '" + FolderName + "'. Voici la liste des épisodes qui se trouve dans le dossier :")
            for EachFileSeries in os.listdir(FullPath):
                print (EachFileSeries)              
            print ("\nDébut du renommage des épisodes :") 
            ## Boucle pour renommer les fichiers avec le nom du repertoire 
            for count, FilesName in enumerate (os.listdir(FullPath)):        
                if os.path.isfile(FullPath+'/'+FilesName)==True: ## Test si c'est un fichier              
                    SplitFile = os.path.splitext(FilesName) ## Permet de spliter le nom du fichier avec l'extension. Exemple : ['NomFichier', '.txt']
                    base_name = SplitFile[0] ## Permet de recuperer la base du nom du fichier. Exemple NomFichier.txt : [NomFichier]
                    NumEpisode = base_name.split("E")
                    NumEpisode2 = NumEpisode[-1]
                    print (NumEpisode2)
                    file_extension = SplitFile[1] ## permet de recuperer l'extension du nom de fichier. Exemple NomFichier.txt : [.txt]
                    OldName = FilesName ## Variable pour le renommage (Nom actuel)
                    NewName = FolderName+"_"+str(count)+file_extension ## Variable pour le renommage (Nouveau nom)    
                    os.rename(FullPath+'/'+OldName, FullPath+'/'+NewName)
                    print ("L'épisode de la séries " + OldName + " est renommé en " + NewName)


else: 
    print ("Il n'y a pas de films ni de séries a renommer.")