# -*- coding: utf-8 -*-
"""
Created on Wed Mar 25 12:40:20 2026

@author: ellaw
"""

numTowers = float(input("Number of towers: "))
power = float(input("Power consumption of each tower (in KWh): "))

totalPower = numTowers * power

coalPower = totalPower * 0.2464
oilPower = totalPower * 0.6732
renewablePower = totalPower * 0.0804

pm10CoalMax = coalPower * 0.01
pm10CoalMin = coalPower * 0.002
pm25CoalMax = coalPower*0.006
pm25CoalMin = coalPower*0.001

pm10OilMax = oilPower*0.02
pm10OilMin = oilPower*0.003
pm25OilMax = oilPower*0.01
pm25OilMin = oilPower*0.002

pm10Max = pm10CoalMax + pm10OilMax
pm10Min = pm10CoalMin + pm10OilMin
pm25Max = pm25CoalMax + pm25OilMax
pm25Min = pm25CoalMin + pm25OilMin
pm10Avg = (pm10Max + pm10Min)/2 
pm25Avg = (pm25Max + pm25Min) /2

print("Minimum total PM10 output:",pm10Min,"g" )
print("Maximum total PM10 output:",pm10Max,"g" )
print("Average total PM10 output:", pm10Avg, "g")
print("Minimum total PM2.5 output:",pm25Min,"g" )
print("Maximum total PM2.5 output:",pm25Max,"g" )
print("Average total PM2.5 output:", pm25Avg, "g")







