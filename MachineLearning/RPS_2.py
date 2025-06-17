#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 26 15:41:30 2024

@author: kennyaskelson
"""
import random

####USES ABBEY METHOD BUT LONGER#####

def player(prev_opponent_play,
          opponent_history=[],
          play_order=[
              {"RRRR": 0, "RRRP": 0, "RRRS": 0, "RRPR": 0, "RRPP": 0, "RRPS": 0, "RRSR": 0, "RRSP": 0, "RRSS": 0,
               "RPRR": 0, "RPRP": 0, "RPRS": 0, "RPPR": 0, "RPPP": 0, "RPPS": 0, "RPSR": 0, "RPSP": 0, "RPSS": 0,
               "RSRR": 0, "RSRP": 0, "RSRS": 0, "RSPR": 0, "RSPP": 0, "RSPS": 0, "RSSR": 0, "RSSP": 0, "RSSS": 0,
               "PRRR": 0, "PRRP": 0, "PRRS": 0, "PRPR": 0, "PRPP": 0, "PRPS": 0, "PRSR": 0, "PRSP": 0, "PRSS": 0,
               "PPRR": 0, "PPRP": 0, "PPRS": 0, "PPPR": 0, "PPPP": 0, "PPPS": 0, "PPSR": 0, "PPSP": 0, "PPSS": 0,
               "PSRR": 0, "PSRP": 0, "PSRS": 0, "PSPR": 0, "PSPP": 0, "PSPS": 0, "PSSR": 0, "PSSP": 0, "PSSS": 0,
               "SRRR": 0, "SRRP": 0, "SRRS": 0, "SRPR": 0, "SRPP": 0, "SRPS": 0, "SRSR": 0, "SRSP": 0, "SRSS": 0,
               "SPRR": 0, "SPRP": 0, "SPRS": 0, "SPPR": 0, "SPPP": 0, "SPPS": 0, "SPSR": 0, "SPSP": 0, "SPSS": 0,
               "SSRR": 0, "SSRP": 0, "SSRS": 0, "SSPR": 0, "SSPP": 0, "SSPS": 0, "SSSR": 0, "SSSP": 0, "SSSS": 0}
          ]): #this is all the different possible 4 combos
    
    guess = random.choice(["R", "P", "S"]) #intialize guess
    
    if not prev_opponent_play:
        prev_opponent_play = 'R' #appendR as first play
    opponent_history.append(prev_opponent_play) #append previous plats
    
    prediction = 'R'
    
    if len(opponent_history) > 3:
        last_four = "".join(opponent_history[-4:]) #grab last 4 as string
        last_three = "".join(opponent_history[-3:]) #grab las 3 as string
        if len(last_four) == 4:
            play_order[0][last_four] += 1 #updates dictionary if last 4 match

            potential_plays = [last_three + "R", last_three + "P", last_three + "S",] #different possible next moves

            sub_order = {
                k: play_order[0][k]
                for k in potential_plays if k in play_order[0]} #idk what this does

            prediction = max(sub_order, key=sub_order.get)[-1:] #gets the most likely next set

            ideal_response = {'P': 'S', 'R': 'P', 'S': 'R'} #counter moves
        
            guess = ideal_response[prediction] #grabs counter move

    return guess