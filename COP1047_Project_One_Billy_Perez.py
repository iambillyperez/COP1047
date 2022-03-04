# -*- coding: utf-8 -*-
"""
Created on Thu Mar  3 21:57:17 2022

@author: iambi
"""

income = float(input("Enter the annual income: "))
dependents = float(input("Enter number of dependents: "))

income = income - 10000 - (3000 * dependents)
tax = income * 0.20
print(tax)