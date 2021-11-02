#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 21 09:00:13 2021

@author: Colombiano
"""

class Question:
    def __init__(self,question,svar):
        question = question.split("\n")
        self.question = question[0]
        self.svar_alternativ = question[1:]
        self.svar = svar
    def __str__(self)->str:
        resultat =""
        resultat += f"Q {self.question} \n"
        for k, a in enumerate(self.svar_alternativ):
            resultat += f"[{k+1}]: {a}\n" 
        return resultat
    def sjekk_svar(self):
        pass
        
        
question_prompts =[

    "Hva er hovedstaden til Irak? \n Paris\n Bagdad\n Oslo",
    "Hvor ligger Kina? \n Asia\n Afrika\n Europa",
]
 
questions = [
    Question(question_prompts[0], 2),
    Question(question_prompts[1], 1),
]



def run_test(questions):
    score = 0
    for question in questions:
        print(question)
        svar = int( input("Ditt alternativ: ") )
        if svar == question.svar:
            score += 1
    print("Du fikk " + str(score) + "/" + str(len(questions)) + "Riktig")
            
run_test(questions)
