#!/usr/bin/env python
#-*- coding: utf-8 -*-
import gc
import csv
from pylab import*
import numpy
import matplotlib.pyplot 

def lecture_noms() : #On regarde l'ensemble des noms possibles et on selectionne les bons
	import csv
	import os

	premier=True

	noms_existant=list() #Ceux qui existent
	diametre=list() #Les tailles de plancton correspondantes
	dicoInverse = corresInverse()

	with open('C:\\Users\\valentin\Desktop\\boulot_mines\\S3Recherche\\BDD\\donneesBrutes\\Swarms.protist.abund.4frac.SUR', 'r') as csvfile:

		reader = csv.reader(csvfile, delimiter=',', quotechar='|') #Ici on utilise un CSV avec des , comme separateurs
		for row in reader:
			if premier : 
				premier = False
				for dot in row :
					print(dot[2:-2])
					num = dot[2]
					if dot[3] != '.' :
						num = num + dot[3]
						if dot[4] != '.' :
							num = num + dot[4]
					num = int(float(num))
					print(num)

					if "20.180" in dot :
						diametre = diametre + [180]
						noms_existant = noms_existant + [dicoInverse[(num,'SUR',180)]]
					elif "0.8.5" in dot :
						diametre = diametre + [5]
						noms_existant = noms_existant + [dicoInverse[(num,'SUR',5)]]
					elif "180.2000" in dot :
						diametre = diametre + [2000]
						noms_existant = noms_existant + [dicoInverse[(num,'SUR',2000)]]
					else :
						diametre = diametre + [20]
						noms_existant = noms_existant + [dicoInverse[(num,'SUR',20)]]



	return(noms_existant,diametre) #On renvoie le tout


def binning(nod,k) : #On fait le binning
	import numpy
	import csv
	from pylab import*
	import math
	import matplotlib.pyplot as plt
	csv.field_size_limit(22000000)#On allonge la taille maximale d'un csv
	import gc

	gc.collect()

	rang1=list()
	log1 = list()
	taille1 = list()
	stationNoms=list()
	indice= 0
	indice2=-1
	numeroCourbe = 0

	#Lecture du CSV

	for nom in nod : 
		indice2 = indice2 + 1 
		if nom == 'TV9_135':

			gc.collect()
			rang=[0]*100 #Le tableau des rangs 
			abondances=[0]*100 #Le tableau des abondances binnees à recuperer
			data=list() #les donnees exportees sous forme de matrice
			taille=0 #la taille des donnees
			log_data=list() #Les valeurs en echelle log
			tailleBin=[0]*100 #le nombre de points dans chaque bin
			premier = True #Est-ce qu'on lit la première ligne ? Si oui on la saute
			premier2 = True
			position = 0

			with open('C:\\Users\\valentin\Desktop\\boulot_mines\\S3Recherche\\BDD\\donneesBrutes\\Swarms.protist.abund.4frac.SUR', 'r') as csvfile:
				reader = csv.reader(csvfile, delimiter=',', quotechar='|') #Ici on utilise un CSV avec des , comme separateurs
				for row in reader:
					if premier : 
						premier=False #On saute la première ligne
						stationNoms=stationNoms+[nom]
					else :
						if int(float(row[indice2-1]))>5 :
							taille=taille+1 #On s'economise un parcours en trouvant ici la taille de data
							data=data+[int(float(row[indice2-1]))]
							#print(int(float(row[indice2-1])))

							
		#DEBUT PARTIE 2

				indice=0
				data=sorted(data) #On trie par ordre croisant
				data.reverse() #On trie par ordre decroissant
				abondance_max=data[0]


				#On va choisir les abondances à trouver
				indice=0
				k=0
				pas = taille/100


				#On ne cree pas de fonction intermediaire pour ne pas avoir à recopier data

				indice=0
				k=0

				#On fait un binning logarithmique
				from decimal import*
				getcontext().prec=20 #On augmente le nombre de decimales possibles
				log_taille=Decimal(math.log10(taille)) #on trouve la taille en log10
				indice=0
				j=0
				while k<100: #On fait 100 bins
					
					if j<taille+1:
						indice=0
						while indice<(Decimal(10**(log_taille*Decimal(k+1)/100))-Decimal(10**(log_taille*Decimal(k)/100))): #tant qu'on est sur le bon bin
							if j+indice<taille and data[j+indice]>0: 
								abondances[k]=abondances[k]+Decimal(math.log10(data[j+indice])) #on somme les abondances
								rang[k]=rang[k]+math.log10(j+indice+1) #les rangs en echelle log
								tailleBin[k]=tailleBin[k]+1 #on augmente la taille du bin
								indice=indice+1
							else :
								indice=indice+1
			

					abondances[k]=Decimal(abondances[k])/Decimal(indice) #On moyennise
					j=j+indice

					rang[k]=rang[k]/indice #idem sur les rangs
					tailleBin[k]=float(Decimal(tailleBin[k])/Decimal(taille)) #et on normalise la taille des bins

					clf()
					gc.collect()

					k=k+1

				plt.figure(figsize=(30,20))
				scatter(rang,abondances,s=120)
				plt.title('Swarms rank-abundance distribution (log/log)',size = 'xx-large')
				plt.legend()
				savefig('C:\\Users\\valentin\Desktop\\boulot_mines\\S3Recherche\\Python\\correlation\\Swarms-loglog_{}.png'.format(nom))



def lancement(k) : 
	from pylab import* #Pour le trace
	import matplotlib.pyplot as plt

	dictionnaire = corres() #On recupère la correspondance entre les noms des echantillons et les stations

	noms, diametre = lecture_noms() #les resultats de la lecture des noms de fichiers : les noms a ouvrir et les tailles de plancton correspondantes

	binning(noms,k) #On recupere le binning

def corres() :
	import csv


	with open('C:\\Users\\valentin\Desktop\\boulot_mines\\S3Recherche\\BDD\\ProtistTV9subtabs293\\correspondance.csv', 'r') as csvfile:
		echantillons = dict()
		reader = csv.reader(csvfile, delimiter=';', quotechar='|') #Ici on utilise un CSV avec des , comme separateurs
		for row in reader:
			a= row[0]
			b=row[1]
			c= row[2]

			echantillons[a] = (int(b),c)

	return(echantillons)

def corresInverse() :

	with open('C:\\Users\\valentin\Desktop\\boulot_mines\\S3Recherche\\Python\\correlation\\photic_samples.csv', 'r') as csvfile:
		echantillons = dict()
		reader = csv.reader(csvfile, delimiter=';', quotechar='|') #Ici on utilise un CSV avec des , comme separateurs
		for row in reader:
			a= row[0]
			b=row[2] #Station
			c= row[1] #Sur ou dcm
			if row[3]=='180-2000' :
				d=2000
			if row[3]=='0.8-5' :
				d=5
			if row[3]=='20-180' :
				d=180
			if row[3]=='5a20' :
				d=20

			echantillons[(int(float(b)),c,d)] = (a)

	return(echantillons)

def traitement(pentes,ok,stationNoms,dictionnaire,diametre,longueurs,poids) :

	resPentes = list() #Les pentes triees
	resOk = list() #Les statuts tries de la meme facon
	resStationNoms = list() #Les noms egalement tries de la meme facon
	resDiametre = list()
	resLongueurs=list()
	resPoids = list()
	indice = 0
	

	indice=0
	k=0

	for p in ok :
		if p>0 :
		
			a=stationNoms[k]			
			resOk=resOk+[p]
			resPentes=resPentes + [pentes[indice]]
			resPoids = resPoids + [poids[indice]]
			resDiametre = resDiametre + [diametre[indice]]
			resLongueurs = resLongueurs + [longueurs[indice]]
			j=0
			while j<p :

				resStationNoms=resStationNoms+[a]
				j=j+1
					

			indice=indice+1

		k=k+p

	return(resPentes,resOk,resStationNoms,resDiametre,resLongueurs,resPoids)

def transcription(noms,dico) :
	resNoms = list()

	for nom in noms :
		resNoms = resNoms + [nom]


	return(resNoms)

def expos(s) :

	expo = 1
	a = 0
	avant = True
	avant2 = True

	for lettre in s :

		if lettre == 'e' :
			avant = False
			expo = 0
		if lettre == '-' :
			avant2 = False
		else :
			if avant :
				a=10*a+int(float(lettre))
			else :
				if avant2 :
					expo = expo*10+int(float(lettre))
				else :
					expo = -(abs(expo*10)+int(float(lettre)))



	return(int(float(a**expo)))