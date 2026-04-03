# -*- coding: utf-8 -*-
"""
Created on Mon Mar 30 12:12:29 2026

@author: ellaw
"""
efficiency = 0.4
flowrate = float(input("enter flow rate: (m^3/hour):  " ))
pollutionConcentration10 = float(input("enter PM10 concentration (micrograms / m^3):  "))
pollutionConcentration25 = float(input("enter PM2.5 concentration (micrograms / m^3 ): "))
pollutionConcentrationOzone = 54.6


desiredLevel10 = float(input("enter desired level of PM10 (micrograms / m^3): "))
desiredLevel25 = float(input("enter desired level of PM25 (micrograms / m^3): "))
desiredLevelOzone = 100

years = float(input("enter number of years: "))
percentIncrease = float(input("enter pollution increase % per year: "))


pm10ChangeGrams = (pollutionConcentration10 - desiredLevel10) / 10**6
pm25ChangeGrams = (pollutionConcentration25 - desiredLevel25) / 10**6

grams10 = pollutionConcentration10 * 10**6 * percentIncrease **years
grams25 = pollutionConcentration25 * 10**6 * percentIncrease **years

gramsRemoved10 = flowrate * 0.7 * 24 * pollutionConcentration10 / 10**6
gramsRemoved25 = flowrate * 0.7 * 24 * pollutionConcentration25 / 10**6



towers10 = grams10 * (1 / gramsRemoved10) * (1 /  (years * 365))
towers25 = grams25 * (1 / gramsRemoved25) * (1 / (years * 365))

if towers10 > towers25:
    print("towers needed: ", towers10)
else:
    print("towers needed: ", towers25)

#reductionRate = flowrate * efficiency

