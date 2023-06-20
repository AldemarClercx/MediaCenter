#!/usr/bin/python3
#-*- coding: utf-8 -*-

import os
from RenameSeries import RenameSeries
from RenameMovies import RenameMovies

## Variables fixes
PathSeriesOk = "D:/Telechargements/Test/Pret_a_regarder/Series"
PathMoviesOk = "D:/Telechargements/Test/Pret_a_regarder/Movies"

RenameSeries()
print ("\n\n-----")
print ("Voici la liste des séries déplacés :")
for EachFolderSeriesOk in os.listdir(PathSeriesOk):
    FullPathSeriesOk = PathSeriesOk+"/"+EachFolderSeriesOk
    print ("\n"+EachFolderSeriesOk)

    for FilesNameOk in os.listdir(FullPathSeriesOk):        
        if os.path.isfile(FullPathSeriesOk+'/'+FilesNameOk)==True:
            print (FilesNameOk)


RenameMovies()
print ("\n\n-----")
print ("Voici la liste des films déplacés :\n")
for EachFolderMoviesOk in os.listdir(PathMoviesOk):
    print (EachFolderMoviesOk)