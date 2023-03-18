import phonenumbers
import folium
import os
import sys
from myNumber import number
from phonenumbers import geocoder
key = '0a2fc090b1f34519a73da6f46d40d3a2'

## INTRO PROGRAMA
os.system("clear")
os.system("figlet SCRIPT TRACK")
print("\nProgramador : Joel Malacas")
print("Youtube : https://www.youtube.com/channel/UCoM6aciljCPcEWj2VZ8cAYg\n")
print("O número a localizar : " + number)

samNumber = phonenumbers.parse(number)
yourLocation = geocoder.description_for_number(samNumber, "pt")
print("País : " + yourLocation)


## OPERADORA

from phonenumbers import carrier

service_provider = phonenumbers.parse(number)
print("Operadora : " + carrier.name_for_number(service_provider, "pt"))

## CAGE CODER

from opencage.geocoder import OpenCageGeocode

geocoder = OpenCageGeocode(key)

query = str(yourLocation)
results = geocoder.geocode(query)

lat = results[0]['geometry']['lat']

lng = results[0]['geometry']['lng']

print(lat,lng, "\nNúmero Localizado Com Sucesso")

myMap = folium.Map(location=[lat,lng], zoom_start = 9)

folium.Marker([lat,lng],popup=yourLocation).add_to((myMap))

## NOTEPAD INFO SAVE
file = open('info.txt', 'w')
sys.stdout = file
print("===================================================================")
print("\t\tSCRIPT TRACKER PHONE BY JOEL MALACAS (PORTUGAL)")
print("===================================================================")
print("\n\t\t\t\tNúmero a ser Localizado : " + number)
print("\n\nPaís : " + yourLocation)
print("\nOperadora : " + carrier.name_for_number(service_provider, "pt"))
print("\nCoordenadas : ", lat,lng)
print("\n\n===================================================================\nNúmero Localizado e Guardado com Sucesso")
file.close()

## HTML SAVE

myMap.save("mylocation.html")
