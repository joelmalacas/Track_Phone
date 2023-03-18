@echo off
color a
cls
winget install python
winget install pip
python -m pip install --upgrade pip
pip install folium
pip install phonenumbers
pip install figlet
pip install geocoder
pip install opencage
echo Python e Bibliotecas Instaladas Com Sucesso
exit
