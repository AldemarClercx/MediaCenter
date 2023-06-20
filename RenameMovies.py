#!/usr/bin/python3
#-*- coding: utf-8 -*-

import os
import re
import shutil
import logging

## Variables fixes
PathMovies = "D:/Telechargements/Test/A_traiter/Movies"
PathMoviesOk = "D:/Telechargements/Test/Pret_a_regarder/Movies"

def ListMovies():
    logging.basicConfig(format='%(asctime)s %(message)s', datefmt="%d-%m-%Y %I:%M:%S %p", filename="C:/Users/ext_aclercx.D01/Documents/Script/Test/RenameMovies.log", level=logging.DEBUG)
    logging.info("-----")
    logging.info("Program Started")  
    logging.info(" ")
    logging.info("Voici la liste des films présent :")    
    ## Boucle pour lister les dossiers présent dans le repertoire 'Films'
    for EachFolderFilms in os.listdir(PathMovies):
        logging.info(EachFolderFilms)

def RenameMovies():
    logging.basicConfig(format='%(asctime)s %(message)s', datefmt="%d-%m-%Y %I:%M:%S %p", filename="C:/Users/ext_aclercx.D01/Documents/Script/Test/RenameMovies.log", level=logging.DEBUG)  

    ## Boucle pour tester que ca soit bien un dossier
    for FolderName in os.listdir(PathMovies):
        if os.path.isdir(PathMovies+'/'+FolderName)==True:
            FullPath = PathMovies+'/'+FolderName
            logging.info(" ")
            logging.info("Dans le repertoire '" + FolderName + "' :")

            ## Boucle pour renommer les fichiers avec le nom du repertoire 
            for FilesName in os.listdir(FullPath):        
                if os.path.isfile(FullPath+'/'+FilesName)==True: ## Test si c'est un fichier              
                    SplitFile = os.path.splitext(FilesName) ## Permet de spliter le nom du fichier avec l'extension. Exemple : ['NomFichier', '.txt']
                    base_name = SplitFile[0] ## Permet de recuperer la base du nom du fichier. Exemple NomFichier.txt : [NomFichier]
                    file_extension = SplitFile[1] ## permet de recuperer l'extension du nom de fichier. Exemple NomFichier.txt : [.txt]
                    OldName = FilesName ## Variable pour le renommage (Nom actuel)
                    NewName = FolderName+file_extension ## Variable pour le renommage (Nouveau nom)    
                    shutil.move(FullPath+'/'+OldName, PathMoviesOk+'/'+NewName)
                    logging.info("Le film " + OldName + " est renommé en " + NewName)
                    shutil.rmtree(FullPath)     

def RenameMoviesOK():
    logging.basicConfig(format='%(asctime)s %(message)s', datefmt="%d-%m-%Y %I:%M:%S %p", filename="C:/Users/ext_aclercx.D01/Documents/Script/Test/RenameMovies.log", level=logging.DEBUG)
    logging.info(" ")
    logging.info ("Voici la liste des films déplacés :")
    for EachFolderMoviesOk in os.listdir(PathMoviesOk):
        logging.info (EachFolderMoviesOk) 
    logging.info(" ")
    logging.info("Program finished")
    logging.info("-----\n")


if len(os.listdir(PathMovies)) > 0:
    ListMovies()
    RenameMovies()
    RenameMoviesOK()
else:
    logging.basicConfig(format='%(asctime)s %(message)s', datefmt="%d-%m-%Y %I:%M:%S %p", filename="C:/Users/ext_aclercx.D01/Documents/Script/Test/RenameMovies.log", level=logging.DEBUG)
    logging.info("-----")
    logging.info("Il n'y a pas de films à déplacer")
    logging.info("-----\n")
