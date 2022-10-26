# -*- coding: utf-8 -*-
"""
Created on Wed Jan  5 12:10:27 2022

@author: Z@C#3R
"""
ETH2=0
SOL2=0
BTC2=0
ETH=0.00029
SOL=0.0066
BTC=0.000023
USD=1
zcode=input('pick an output: ETH,BTC,SOL. ')
starter=input('do you want to convert to crypto or to USD')
if starter == "crypto" or "CRYPTO":
 if zcode == 'BTC' or 'btc':
  btc_code = float(input('how much USD do you want to convert >   '))

  final_btc = btc_code *  BTC
  print(final_btc,"BTC is your total, see ya") 
 

 elif zcode == 'SOL' or 'sol':
  sol_code = float(input('how much USD do you want to convert >   '))

  final_sol = sol_code *  SOL
  print(final_sol,"SOL is your total good day") 
 
 
 elif zcode == 'ETH' or 'eth':
  eth_code = float(input('how much USD do you want to convert >   '))

  final_eth = eth_code *  ETH
  print(final_eth,"ETH is your total good day") 
 
 else:
  print('wait what?????????')  
  
elif starter == "USD" or"usd":
    
 input('what will you con vert to')    
    
    
    
    
    
    
    
    
    
    
    