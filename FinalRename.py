#!/usr/bin/python3
#-*- coding: utf-8 -*-

import os
import logging
import datetime
from RenameSeries import ListSeries, RenameSeries, RenameSeriesOK
from RenameMovies import ListMovies, RenameMovies, RenameMoviesOK

## Variables fixes
Now = datetime.datetime.now()
TimeStamp = str(Now.strftime("%Y%m%d_%H%M%S"))
PathSeries = "D:/Telechargements/A_traiter/Series"
PathMovies = "D:/Telechargements/A_traiter/Movies"
LogFile = logging.basicConfig(format='%(asctime)s %(message)s', datefmt="%d-%m-%Y %I:%M:%S %p", filename="D:/Projets/Prodcution/Logs/MediaCenter/FinalRename_"+TimeStamp+".log", level=logging.info)

if len(os.listdir(PathSeries)) > 0:
    LogFile
    logging.info("-----")
    logging.info("Program RenameSeries.py starded")
    logging.info(" ")
    ListSeries()
    RenameSeries()
    RenameSeriesOK()
    logging.info(" ")
    logging.info("Le script c'est terminé correctement.")
    logging.info(" ")
    logging.info("Program RenameSeries.py finished")
    logging.info("-----")
    logging.info(" ")
else:
    logging.info("-----")
    logging.info("Program RenameSeries.py starded")
    logging.info(" ")
    logging.info("Il n'y a pas de séries à déplacer.")
    logging.info(" ")
    logging.info("Program RenameSeries.py finished")
    logging.info("-----")

if len(os.listdir(PathMovies)) > 0:
    LogFile
    logging.info(" ")
    logging.info("-----")
    logging.info("Program RenameMovies.py starded")
    logging.info(" ")
    ListMovies()
    RenameMovies()
    RenameMoviesOK()
    logging.info(" ")
    logging.info("Le script c'est terminé correctement.")
    logging.info(" ")
    logging.info("Program RenameMovies.py finished")
    logging.info("-----")
else:
    logging.info(" ")
    logging.info(" ")
    logging.info("-----")
    logging.info("Program RenameMovies.py starded")
    logging.info(" ")
    logging.info("Il n'y a pas de films à déplacer.")
    logging.info(" ")
    logging.info("Program RenameMovies.py finished")
    logging.info("-----")
