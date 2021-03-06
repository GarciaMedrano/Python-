#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 22 12:11:08 2021

@author: Colombiano
"""


#Ordteller for tekstfil:
#   Les inn ei tekstfil
#   Finn alle ordene
#   Tell antall forekomster av hvert ord

ordliste = dict()
linjenummer=0
with open("oving_1_rein_tekst.txt", "r", encoding="UTF8") as fila:
    for linje in fila:
        ordene = linje.split()
        linjenummer = linjenummer + 1
        for ordet in ordene:
            ordet = ordet.lower()
            ordet = ordet.strip(",.=()*")
            if ordet not in ordliste:
                ordliste[ordet]=linjenummer
            
    for ordet in ordliste:
        print(f"Ordet {ordet} forekommer {ordliste[ordet]} linjenummer")