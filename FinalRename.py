#!/usr/bin/python3
#-*- coding: utf-8 -*-

import os
from RenameSeries import RenameSeries, RenameSeriesOK
from RenameMovies import RenameMovies, RenameMoviesOK

## Variables fixes
PathSeries = "D:/Telechargements/Test/A_traiter/Series"
PathMovies = "D:/Telechargements/Test/A_traiter/Movies"

if len(os.listdir(PathSeries)) > 0:
    RenameSeries()
    RenameSeriesOK()
else:
    print ("Il n'y a pas de séries à déplacer.")


if len(os.listdir(PathMovies)) > 0:
    RenameMovies()
    RenameMoviesOK()
else:
    print ("Il n'y a pas de films à déplacer.")