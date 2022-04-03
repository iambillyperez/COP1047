# -*- coding: utf-8 -*-
"""
Created on Sun Apr  3 16:16:58 2022

@author: iambi
"""

hotdog_pack = 10
hotdog_bun_pack = 8

numofpeople = int(input('Enter number of people attending the cookout: '))
numofhotdogseach = int(input('Enter number of hotdogs for each person: '))

hotdogs_needed = numofpeople * numofhotdogseach

hotdog_packs_needed, hotdogs_leftover = divmod(hotdogs_needed, hotdog_pack)
hotdog_bun_packs_needed, hotdog_buns_leftover = divmod(hotdogs_needed, hotdog_bun_pack)

if hotdogs_leftover:
    hotdog_packs_needed += 1
    hotdogs_leftover = hotdog_pack - hotdogs_leftover

if hotdog_buns_leftover:
    hotdog_bun_packs_needed += 1
    hotdog_buns_leftover = hotdog_bun_pack - hotdog_buns_leftover

print('Minimum packages of hot dogs needed: ', hotdog_packs_needed)
print('Minimum packages of hot dog buns needed: ', hotdog_bun_packs_needed)
print('Hot dogs left over: ', hotdogs_leftover)
print('Hot dog buns left over: ', hotdog_buns_leftover)