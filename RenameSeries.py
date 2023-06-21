#!/usr/bin/python3
#-*- coding: utf-8 -*-

import os
import re
import shutil
import logging
import datetime

## Variables fixes
Now = datetime.datetime.now()
TimeStamp = str(Now.strftime("%Y%m%d_%H%M%S"))
PathSeries = "D:/Telechargements/A_traiter/Series"
PathSeriesOk = "D:/Telechargements/Pret_a_regarder/Series"
LogFile = logging.basicConfig(format='%(asctime)s %(message)s', datefmt="%d-%m-%Y %I:%M:%S %p", filename="D:/Projets/Recette/Logs/MediaCenter/FinalRename_"+TimeStamp+".log", level=logging.INFO)

def ListSeries():
    LogFile
    logging.info("Voici la liste des séries présent :")    
    ## Boucle pour lister les dossiers présent dans le repertoire 'Series'
    for EachFolderSeries in os.listdir(PathSeries):
        logging.info(EachFolderSeries)

def RenameSeries():
    LogFile
    ## Boucle pour tester que ca soit bien un dossier
    for FolderName in os.listdir(PathSeries):
        if os.path.isdir(PathSeries+'/'+FolderName)==True:
            FullPath = PathSeries+'/'+FolderName
            logging.info(" ")
            logging.info("Dans le repertoire '" + FolderName + "'. Voici la liste des épisodes qui se trouve dans le dossier :")
            for EachFileSeries in os.listdir(FullPath):
                logging.info(EachFileSeries)

            logging.info(" ")
            logging.info ("Début du renommage des épisodes :") 
            ## Boucle pour renommer les fichiers avec le nom du repertoire 
            for FilesName in os.listdir(FullPath):        
                if os.path.isfile(FullPath+'/'+FilesName)==True: ## Test si c'est un fichier         
                    NumEpisode = re.search('[E]\d{2}', FilesName).group(0)     
                    SplitFile = os.path.splitext(FilesName) ## Permet de spliter le nom du fichier avec l'extension. Exemple : ['NomFichier', '.txt']
                    base_name = SplitFile[0] ## Permet de recuperer la base du nom du fichier. Exemple NomFichier.txt : [NomFichier]
                    file_extension = SplitFile[1] ## permet de recuperer l'extension du nom de fichier. Exemple NomFichier.txt : [.txt]
                    OldName = FilesName ## Variable pour le renommage (Nom actuel)
                    NewName = FolderName+NumEpisode+file_extension ## Variable pour le renommage (Nouveau nom)    
                    shutil.move(FullPath+'/'+OldName, FullPath+'/'+NewName)
                    logging.info("L'épisode de la séries " + OldName + " est renommé en " + NewName)
            shutil.move(FullPath, PathSeriesOk)

def RenameSeriesOK():
    LogFile
    logging.info(" ")
    logging.info("Voici la liste des séries déplacés :")
    for EachFolderSeriesOk in os.listdir(PathSeriesOk):
        FullPathSeriesOk = PathSeriesOk+"/"+EachFolderSeriesOk
        logging.info(" ")
        logging.info(EachFolderSeriesOk)

        for FilesNameOk in os.listdir(FullPathSeriesOk):        
            if os.path.isfile(FullPathSeriesOk+'/'+FilesNameOk)==True:
                logging.info(FilesNameOk)
