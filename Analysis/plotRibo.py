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

	nod= ['data(17).20'] #Les noms possibles
	noms_possibles=list() #Le mix des deux
	noms_existant=list() #Ceux qui existent
	diametre=list() #Les tailles de plancton correspondantes



	for nom in nod :

		aMarche=False
		try:
			
			if os.path.exists('C:\\Users\\valentin\Desktop\\boulot_mines\\S3Recherche\\BDD\\ProtistTV9subtabs293\\'+nom):
				noms_existant = noms_existant + [nom] #On regarde si on peut ouvrir le fichire : est-ce que ça bug ?

				if '.5' in nom :
					diametre=diametre+[5]
					if not aMarche :
						aMarche=True

				if '.2000' in nom :
					diametre=diametre+[2000]
					if not aMarche :
						aMarche=True

				if '.180' in nom :
					diametre=diametre+[180]
					if not aMarche :
						aMarche=True

				if ('.20' in nom) and not ('.2000' in nom) :
					diametre=diametre+[20] #On note la taille de plancton correspondante dans une liste classee dans le meme ordre
					if not aMarche :
						aMarche=True


		except IOError: #Si ça plante, on oublie juste cet essai. 
			pass

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

	#Lecture du CSV

	for nom in nod : 

		gc.collect()
		rang=[0]*100 #Le tableau des rangs 
		abondances=[0]*100 #Le tableau des abondances binnees à recuperer
		data=list() #les donnees exportees sous forme de matrice
		indice = 1
		taille=0 #la taille des donnees
		log_data=list() #Les valeurs en echelle log
		tailleBin=[0]*100 #le nombre de points dans chaque bin
		premier = True #Est-ce qu'on lit la première ligne ? Si oui on la saute
		

		with open('C:\\Users\\valentin\Desktop\\boulot_mines\\S3Recherche\\BDD\\ProtistTV9subtabs293\\{}'.format(nom), 'r') as csvfile:
			print('binning de C:\\Users\\valentin\Desktop\\boulot_mines\\S3Recherche\\BDD\\ProtistTV9subtabs293\\{}.csv'.format(nom))
			reader = csv.reader(csvfile, delimiter=';', quotechar='|') #Ici on utilise un CSV avec des , comme separateurs
			for row in reader:
				if premier : 
					station=''
					premier=False #On saute la première ligne
					for x in row :
						station=station+x
					stationNoms=stationNoms+[station]
				else :
					for x in row:
						x=int(x) #On transforme l'abondance en entier
						
						if x>5 :
							taille=taille+1 #On s'economise un parcours en trouvant ici la taille de data
							data=data+[x]
					


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

		plt.figure(figsize=(30,20))

		while k<100: #On fait 100 bins
			
			if j<taille+1:
				indice=0
				while indice<(Decimal(10**(log_taille*Decimal(k+1)/100))-Decimal(10**(log_taille*Decimal(k)/100))): #tant qu'on est sur le bon bin
					if j+indice<taille: 
						abondances[k]=abondances[k]+Decimal(math.log10(data[j+indice])) #on somme les abondances
						rang[k]=rang[k]+math.log10(j+indice+1) #les rangs en echelle log
						scatter(j+1+indice,data[j+indice],s=120,color='red')
						tailleBin[k]=tailleBin[k]+1 #on augmente la taille du bin
						indice=indice+1
					else :
						indice=indice+1
	

			abondances[k]=Decimal(abondances[k])/Decimal(indice) #On moyennise
			j=j+indice

			rang[k]=rang[k]/indice #idem sur les rangs
			tailleBin[k]=float(Decimal(tailleBin[k])/Decimal(taille)) #et on normalise la taille des bins
			k=k+1
		plt.title('rank-abundance distribution (lin/lin)',size = 'xx-large')
		plt.legend()
		savefig('C:\\Users\\valentin\Desktop\\boulot_mines\\S3Recherche\\Python\\correlation\\RA-Silvia-linlin.png')
		plt.figure(figsize=(30,20))
		scatter(rang,abondances,s=120)
		plt.title('rank-abundance distribution (log/log)',size = 'xx-large')
		plt.legend()
		savefig('C:\\Users\\valentin\Desktop\\boulot_mines\\S3Recherche\\Python\\correlation\\RA-Silvia-loglog.png')



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
		
		if dictionnaire[stationNoms[k]][1]=='SUR' :
			a=dictionnaire[stationNoms[k]][0] 

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
		resNoms = resNoms + [dico[nom][0]]


	return(resNoms)