# -*- coding: utf-8 -*-
import requests 
from bs4 import BeautifulSoup as sp
import json
import re
import datetime

url = "https://deals.jumia.ci/abidjan/vehicules?page={}&xhr=trcrn"
hier = datetime.datetime.now() - datetime.timedelta(days=1)

cpt = 20
vehicules = []
day = ""
prix = []
while cpt<200:
	s = sp(requests.get(url.format(cpt)).text, "html.parser")
	for article in s.findAll('article'):
		articles = sp(str(article),"html.parser")
		jour = articles.time.text
		day = articles.time['datetime']
		data = articles.article['data-event']
		dt = json.loads(str(data))
		price = int(str(dt['price']).split(".")[0])
		#print(dt)
		if re.search("Hier",str(jour)) and "Véhicules/Voitures" in dt["category"]:
			print(price)
			vehicules.append(dt)
			prix.append(price)
	cpt+=1
#print(prix)
print ('Hier : ',"-".join(day.split(" ")[0].split(".")))
print("Il y a eu {} voiture(s) postée(s) sur jumia Deals".format(len(vehicules)))
print("la voiture la plus chere était une {}, elle vaut {}".format(vehicules[prix.index(max(prix))]['title'],max(prix)))
print("la voiture la moins chere était une {}, elle vaut {}".format(vehicules[prix.index(min(prix))]['title'],min(prix)))
#nombre_hier = len(vehicules)