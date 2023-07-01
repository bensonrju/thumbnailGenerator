import pandas
import math

myFrame = pandas.read_csv('electrical_budget2.csv')

URLs = []

for element in myFrame['URL (if avalilable)']:
    if str(element) != 'nan':
        print(element)
        URLs.append(element)

print(URLs)
