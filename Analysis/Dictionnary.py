#!/usr/bin/env python
#-*- coding: utf-8 -*-

import csv
from pylab import*
import numpy
import math
import matplotlib.pyplot as plt
import numbers

from allTest import k, s


def main() :
	dicoEchant = corres()
	dicoTotal = dict()


	#On va importer toutes les donnees : 
	
	#0 echantillon
	#1 u
	#2 v
	#3 Okubo Weiss
	#4 Lyapunov exp
	#5 SST_adv
	#6 SST_AMSRE
	#7 grad_SST_adv
	#8 age_from_bathy
	#9 lon_from_bathy
	#10 Shannon_Darwin_mean_all
	#11 Shannon_Darwin_month_all
	#12 Shannon_Darwin_mean_grp
	#13 Shannon_Darwin_month_grp
	#14 Shannon_Darwin_physat_month
	#15 Shannon_Darwin_physat_mean
	#16 Shannon_Darwin_retention
	#17 lon_origin_45d
	#18 lat_origin_45d
	#19 physat_type
	#20 abundance
	#21 richness
	#22 Shannon
	#23 Simpson
	#24 log(alpha)
	#25 Jevenness
	#26 S.obs  especes observees
	#27 S.chao1	indice de chao observe
	#28 se.chao1 	standard error estimee sur l'indice de chao
	#29 S.ACE abundance based coverage estimation
	#30 se.ACE standard error on the abundance based coverage estimation
	#31 distance à la powerlaw
	#32 nb de pentes
	#33 pente 1 (derniere pente, la queue)
	#34 pente 2 (avant derniere pente)
	#35 longueur de la pente 1 (derniere pente, la queue)
	#36 longueur de la pente 2 (avant derniere pente)
	#37 poids de la pente 1
	#38 poids de la pente 2

	#On commence par importer Tara_stations_multisat_extract.csv

	premier = True 

	with open('C:\\Users\\valentin\Desktop\\boulot_mines\\S3Recherche\\Python\\correlation\\Tara_stations_multisat_extract.csv', 'r') as csvfile:
		
		reader = csv.reader(csvfile, delimiter=',',quotechar='|', quoting=csv.QUOTE_MINIMAL)
		for row in reader :
			if premier :
				premier = False
				l=len(row)
				liste_param = ['echantillon']+row[1:l]
			
			elif row ==[] :
				pass

			else : 

				dicoTotal[int(float(row[0])),5] = ['nan']+row[1:l]
				dicoTotal[int(float(row[0])),20] = ['nan']+row[1:l]
				dicoTotal[int(float(row[0])),180] = ['nan']+row[1:l]
				dicoTotal[int(float(row[0])),2000] = ['nan']+row[1:l]

	dicoTotal[11,5] = ['nan']*l
	dicoTotal[11,20] = ['nan']*l
	dicoTotal[11,180] = ['nan']*l
	dicoTotal[11,2000] = ['nan']*l


	#Puis on import les echantillons mais on les ajoute en premier
	#Attention au fait qu'il y a les SUR et les DCM !

	for clef in dicoEchant :
		if dicoEchant[clef][1] == 'SUR' :
			try :
				dicoTotal[dicoEchant[clef][0],dicoEchant[clef][2]][0]=clef

			except :
				pass


	#Puis on importe les ribotypes 

	premier=True

	with open('C:\\Users\\valentin\Desktop\\boulot_mines\\S3Recherche\\Python\\correlation\\diversityProtistRibotypesORGNL', 'r') as csvfile:

		reader = csv.reader(csvfile, delimiter=',',quotechar='|', quoting=csv.QUOTE_MINIMAL)
		for row in reader :

			l= len(row)
			
			if premier :

				premier =False 

			else : 

				try :
					a=dicoEchant[row[0]]

					if a[1] == 'SUR' :
						dicoTotal[a[0],a[2]] = dicoTotal[a[0],a[2]] + row[1:l]


				except :
					pass 
						
	#A ce moment, chaque ligne du dictionnaire devrait contenir 26 elements
	#On s'en assure pour ne pas avoir de decalage. 


	l1 = 26

	for clef in dicoTotal :
		l2 = len(dicoTotal[clef])
		if l2 < 26 :
			dicoTotal[clef] = dicoTotal[clef] + ['nan']*(26-l2)

		elif l2>26 :
			print("entree {} trop longue !".format(clef[0]))
			pass
		else :
			pass

	#Puis on import les donnees de richness

	premier = True 


	with open('C:\\Users\\valentin\Desktop\\boulot_mines\\S3Recherche\\Python\\correlation\\Richness_NonParametrics', 'r') as csvfile:	

		reader = csv.reader(csvfile, delimiter=',',quotechar='|', quoting=csv.QUOTE_MINIMAL)
		for row in reader :

			if premier : 

				premier = False

			else : 

				try :

					row2 = decoupage(row) #On separe les elements de la ligne au niveau des espaces

					l=len(row2)

					if dicoEchant[row2[0]][1] == 'SUR' :
						a=dicoEchant[row2[0]]
						dicoTotal[a[0],a[2]] = dicoTotal[a[0],a[2]] + row2[1:l]
						


				except :
					pass 				


	#A ce moment, chaque ligne du dictionnaire devrait contenir 30 elements
	#On s'en assure pour ne pas avoir de decalage. 




	l1 = 31

	for clef in dicoTotal :
		l2 = len(dicoTotal[clef])

		if l2 < 31 :
			#print("perte de donnees sur l'echantillon' {}".format(clef[0]))
			dicoTotal[clef] = dicoTotal[clef] + ['nan']*(31-l2)

		elif l2>31 :
			print("entree {} trop longue !".format(clef[0]))
			pass

	#On importe les distance à la loi de puissance

	with open('C:\\Users\\valentin\Desktop\\boulot_mines\\S3Recherche\\Resultats\\log_log\\10_{}\\toutes\\ecartPowerLaw_{}.csv'.format(k,k), 'r') as csvfile:
		
		reader = csv.reader(csvfile, delimiter=';',quotechar=',', quoting=csv.QUOTE_MINIMAL)
		for row in reader :
			for clef in dicoTotal :
				if float(enlever(row[0])) == clef[0] :
					try :
						dicoTotal[clef][31]=float(enlever(row[1]))
					except :
						dicoTotal[clef]=dicoTotal[clef]+[float(enlever(row[1]))]
				elif len(dicoTotal[clef])==31 : 
					dicoTotal[clef] = dicoTotal[clef] + [-100]

	#Il ne reste qu'a importer les pentes 

	with open('C:\\Users\\valentin\Desktop\\boulot_mines\\S3Recherche\\Resultats\\log_log\\10_{}\\toutes\\pentes_{}.csv'.format(k,k), 'r') as csvfile:

		reader = csv.reader(csvfile, delimiter=';',quotechar='|', quoting=csv.QUOTE_MINIMAL)
		for row in reader :	

			pStations = float(remove(row[0],','))
			pPentes1 = float(remove(row[2],','))
			pNb =  int(float(remove(row[3],',')))
			diam =  int(float(remove(row[4],',')))


			if int(float(remove(row[3],','))) == 1 :
				pPentes2 = 'Null'
				pLong2 = 'Null'
				pLong1 = float(remove(row[5],','))
				poids1 = float(remove(row[6],','))
				poids2 = 'Null'
				

			else :
				pLong2 = float(remove(row[5],','))
				pLong1 = float(remove(row[6],','))
				pPentes2 = float(remove(row[1],','))
				poids2 = float(remove(row[7],','))
				poids1 = float(remove(row[8],','))
				
				
			try :

				dicoTotal[pStations,diam] = dicoTotal[pStations,diam] + [pNb,pPentes1,pPentes2,pLong1,pLong2,poids1,poids2]

			except : 

				pass




	#On va enfin transformer tous les elements en nombres, quand c'est possible

	indice = 0

	for clef in dicoTotal :

		indice = 0

		for i in dicoTotal[clef] :

			try :

				dicoTotal[clef][indice] = float(dicoTotal[clef][indice])

			except :

				(a,b) = tentative(dicoTotal[clef][indice])
				if a :
					dicoTotal[clef][indice] = b

				pass


			indice = indice + 1

	return(dicoTotal)


def corres() :

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

			echantillons[a] = (int(float(b)),c,d)

	return(echantillons)

def decoupage(row) :

	res=list()
	a = list()

	for lettre in row[0] : 

		if lettre == ' ' :

			res = res + [a]
			a=''


		else : 
			if str(a)=='[]T' :
				a = 'T'
			a = str(a) + str(lettre)

	res = res + [a]
	return(res)


def tracer(a, b) :	 #Quand on veut juste placer pour chaque stattion un parametre en fonction d'un autre. 
					 #Ne fonctionne pas avec les pentes !

	liste = selection(a,b)
	abcisse = list()

	noms = {0 : 'echantillon',1 : 'u',2:'v',3:'Okubo Weiss',4: 'Lyapunov exp',5 : 'SST_adv',6: 'SST_AMSRE',7 : 'grad_SST_adv',8: 'age_from_bathy',9: 'lon_from_bathy',10 : 'Shannon_Darwin_mean_all',
	11: 'Shannon_Darwin_month_all',12 :'Shannon_Darwin_mean_grp',13: 'Shannon_Darwin_month_grp',14 :'Shannon_Darwin_physat_month',15 : 'Shannon_Darwin_physat_mean',16 :'retention', 17 : 'lon_origin_45d',
	18: 'lat_origin_45d',19 :'physat_type',20 : 'abundance',21: 'richness',22 : 'Shannon',23: 'Simpson',24 :'log(alpha)',25 : 'Jevenness',26 :'S.obs',27 :'S.chao1',28 : 'se.chao1',
	29 :'S.ACE',30 :'se.ACE',31 : 'distance a la loi de puissance', 32 :'nb de pentes',33 :'pente1',34: 'pente2',35 : 'long1',36 :'long2', 37 : 'poids1', 38 : 'poids2'}


	noma = noms[a]
	nomb = noms[b]

	bool5 = True
	bool20 = True
	bool180 = True
	bool2000 = True


	for i in liste :
		ajout = True

		for dot in abcisse :

			if dot == i[2] :
				ajout = False

		if str(i[2]) == 'nan' :
			ajout = False

		if ajout :
			abcisse = abcisse +  [i[2]]
			prec = i[2]

	abcisse.sort()
	l = len(abcisse)

	plt.figure(figsize=(30,20))
	xticks(arange(l),abcisse,rotation=90,fontsize=40)

	indice = 0

	plt.figure(figsize=(30,20))

	indice = 0

	for dot in abcisse :

		for i in liste :

			if i[2]==dot :

				if i[1] == 5 :

					c = 'red'

					if bool5 :
						bool5 = False
						scatter(i[2],i[3],color=c,s=120,label='taille 0.8 a 5, queue')
						annotate(i[0],(i[2],i[3]))
						print(test)

					else :
						scatter(i[2],i[3],color=c,s=120)
						annotate(i[0],(i[2],i[3]))						

				if i[1] == 20 :

					c = 'magenta'

					if bool20 :
						bool20 = False
						scatter(i[2],i[3],color=c,s=120,label='taille 5 a 20, queue')
						annotate(i[0],(i[2],i[3]))

					else :
						scatter(i[2],i[3],color=c,s=120)
						annotate(i[0],(i[2],i[3]))

				if i[1] == 180 :

					c = 'green'

					if bool180 :
						bool180 = False
						scatter(i[2],i[3],color=c,s=120,label='taille 20 a 180, queue')
						annotate(i[0],(i[2],i[3]))

					else :
						scatter(i[2],i[3],color=c,s=120)
						annotate(i[0],(i[2],i[3]))

				if i[1] == 2000 :

					c = 'blue'

					if bool5 :
						bool5 = False
						scatter(i[2],i[3],color=c,s=120,label='taille 180 a 2000, queue')
						annotate(i[0],(i[2],i[3]))

					else :
						scatter(i[2],i[3],color=c,s=120)
						annotate(i[0],(i[2],i[3]))

		indice = indice + 1
	plt.title("trace de {} en fonction de {}".format(nomb, noma),fontsize=40)
	plt.legend()
	yticks(fontsize=40)
	xticks(fontsize=40)

	plt.xlabel("{}".format(noma), fontsize=40)
	plt.ylabel("{}".format(nomb), fontsize=40)
	savefig('C:\\Users\\valentin\Desktop\\boulot_mines\\S3Recherche\\Python\\correlation\\{}F{}.png'.format(nomb,noma))


def selection(a, b) :

	dicoTotal = main()
	res = list()

	for clef in dicoTotal :

		if dicoTotal[clef][a] != -1 and dicoTotal[clef][b] != -1 and str(dicoTotal[clef][a]) != 'nan' and str(dicoTotal[clef][a]) != 'nan' and dicoTotal[clef][a] != -100 and dicoTotal[clef][b] != -100:

			res = res + [(clef[0], clef[1], dicoTotal[clef][a], dicoTotal[clef][b])]

	return(res)


def remove(l,item) : 
	res = str()

	for data in l :

		if item == data :
			pass
		else :
			res = res + data

	return(res)


def tentative(s) :

	ok = False
	res = str()
	expo = str()

	for lettre in s :
		if lettre == 'e' :
			ok = True
		elif ok :
			expo = expo + str(lettre)
		else :
			res = res + str(lettre)
	if ok :

		res = float(res)
		expo = float(expo)	
		res = res**expo
		print('tentative')
	return(ok,res)

def serie(k) :

	for i in [3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18] :
		tracer(i,k)

def pente(a) :

	noms = {0 : 'echantillon',1 : 'u',2:'v',3:'Okubo Weiss',4: 'Lyapunov exp',5 : 'SST_adv',6: 'SST_AMSRE',7 : 'grad_SST_adv',8: 'age_from_bathy',9: 'lon_from_bathy',10 : 'Shannon_Darwin_mean_all',
	11: 'Shannon_Darwin_month_all',12 :'Shannon_Darwin_mean_grp',13: 'Shannon_Darwin_month_grp',14 :'Shannon_Darwin_physat_month',15 : 'Shannon_Darwin_physat_mean',16 :'retention', 17 : 'lon_origin_45d',
	18: 'lat_origin_45d',19 :'physat_type',20 : 'abundance',21: 'richness',22 : 'Shannon',23: 'Simpson',24 :'log(alpha)',25 : 'Jevenness',26 :'S.obs',27 :'S.chao1',28 : 'se.chao1',
	29 :'S.ACE',30 :'se.ACE',31 : 'distance a la loi de puissance', 32 :'nb de pentes',33 :'pente1',34: 'pente2',35 : 'long1',36 :'long2', 37 : 'poids1', 38 : 'poids2'}

	nom = noms[a] 

	dicoTotal = main()

	liste1 = list()
	liste2 = list()

	for clef in dicoTotal :
		try :
			if dicoTotal[clef][32] == 1 :
				liste1 = liste1 + [clef]

			elif dicoTotal[clef][32] ==2 :
				liste2 = liste2 + [clef]
		except :
			pass

	plt.figure(figsize=(30,20))


	bool1 = True
	bool2 = True
	bool3 = True
	bool4 = True

	for clef in liste1 :

		if clef[1] == 5 :
			c='red'
			if bool1 :
				bool1 = False
				scatter(dicoTotal[clef][a],dicoTotal[clef][33],color=c,s=120,label='taille 0.8 a 5, queue')
				annotate(clef[0],(dicoTotal[clef][a],dicoTotal[clef][33]))
			else : 
				scatter(dicoTotal[clef][a],dicoTotal[clef][33],color=c,s=120)
				annotate(clef[0],(dicoTotal[clef][a],dicoTotal[clef][33],))

		if clef[1] == 20 :
			c='magenta'
			if bool2 :
				bool2 = False
				scatter(dicoTotal[clef][a],dicoTotal[clef][33],color=c,s=120,label='taille 5 a 20, queue')
				annotate(clef[0],(dicoTotal[clef][a],dicoTotal[clef][33]))
			else : 
				scatter(dicoTotal[clef][a],dicoTotal[clef][33],color=c,s=120)
				annotate(clef[0],(dicoTotal[clef][a],dicoTotal[clef][33]))

		if clef[1] == 180 :
			c='green'
			if bool3 :
				bool3 = False
				scatter(dicoTotal[clef][a],dicoTotal[clef][33],color=c,s=120,label='taille 20 a 180, queue')
				annotate(clef[0],(dicoTotal[clef][a],dicoTotal[clef][33]))
			else : 
				scatter(dicoTotal[clef][a],dicoTotal[clef][33],color=c,s=120)
				annotate(clef[0],(dicoTotal[clef][a],dicoTotal[clef][33]))

		if clef[1] == 2000 :
			c='blue'
			if bool4 :
				bool4 = False
				scatter(dicoTotal[clef][a],dicoTotal[clef][33],color=c,s=120,label='taille 180 a 2000, queue')
				annotate(clef[0],(dicoTotal[clef][a],dicoTotal[clef][33]))
			else : 
				scatter(dicoTotal[clef][a],dicoTotal[clef][33],color=c,s=120)
				annotate(clef[0],(dicoTotal[clef][a],dicoTotal[clef][33]))

	bool1 = True
	bool2 = True
	bool3 = True
	bool4 = True

	for clef in liste2 :

		if clef[1] == 5 :
			c='red'
			if bool1 :
				bool1 = False
				scatter(dicoTotal[clef][a],dicoTotal[clef][33],color=c,s=120,label='taille 0.8 a 5, avant derniere pente')
				scatter(dicoTotal[clef][a],dicoTotal[clef][34],color=c,s=120)
				annotate(clef[0],(dicoTotal[clef][a],dicoTotal[clef][33]))
				annotate(clef[0],(dicoTotal[clef][a],dicoTotal[clef][34]))
			else : 
				scatter(dicoTotal[clef][a],dicoTotal[clef][33],color=c,s=120)
				scatter(dicoTotal[clef][a],dicoTotal[clef][34],color=c,s=120)
				annotate(clef[0],(dicoTotal[clef][a],dicoTotal[clef][33]))
				annotate(clef[0],(dicoTotal[clef][a],dicoTotal[clef][34]))

		if clef[1] == 20 :
			c='magenta'
			if bool2 :
				bool2 = False
				scatter(dicoTotal[clef][a],dicoTotal[clef][33],color=c,s=120,label='taille 5 a 20 avant derniere pente')
				scatter(dicoTotal[clef][a],dicoTotal[clef][34],color=c,s=120)
				annotate(clef[0],(dicoTotal[clef][a],dicoTotal[clef][33]))
				annotate(clef[0],(dicoTotal[clef][a],dicoTotal[clef][34]))
			else : 
				scatter(dicoTotal[clef][a],dicoTotal[clef][33],color=c,s=120)
				scatter(dicoTotal[clef][a],dicoTotal[clef][34],color=c,s=120)
				annotate(clef[0],(dicoTotal[clef][a],dicoTotal[clef][33]))
				annotate(clef[0],(dicoTotal[clef][a],dicoTotal[clef][34]))

		if clef[1] == 180 :
			c='green'
			if bool3 :
				bool3 = False
				scatter(dicoTotal[clef][a],dicoTotal[clef][33],color=c,s=120,label='taille 20 a 180 avant derniere pente')
				scatter(dicoTotal[clef][a],dicoTotal[clef][34],color=c,s=120)
				annotate(clef[0],(dicoTotal[clef][a],dicoTotal[clef][33]))
				annotate(clef[0],(dicoTotal[clef][a],dicoTotal[clef][34]))
			else : 
				scatter(dicoTotal[clef][a],dicoTotal[clef][33],color=c,s=120)
				scatter(dicoTotal[clef][a],dicoTotal[clef][34],color=c,s=120)
				annotate(clef[0],(dicoTotal[clef][a],dicoTotal[clef][33]))
				annotate(clef[0],(dicoTotal[clef][a],dicoTotal[clef][34]))

		if clef[1] == 2000 :
			c='blue'
			if bool4 :
				bool4 = False
				scatter(dicoTotal[clef][a],dicoTotal[clef][33],color=c,s=120,label='taille 180 a 2000 avant derniere pente')
				scatter(dicoTotal[clef][a],dicoTotal[clef][34],color=c,s=120)
				annotate(clef[0],(dicoTotal[clef][a],dicoTotal[clef][33]))
				annotate(clef[0],(dicoTotal[clef][a],dicoTotal[clef][34]))
			else : 
				scatter(dicoTotal[clef][a],dicoTotal[clef][33],color=c,s=120)
				scatter(dicoTotal[clef][a],dicoTotal[clef][34],color=c,s=120)
				annotate(clef[0],(dicoTotal[clef][a],dicoTotal[clef][33]))
				annotate(clef[0],(dicoTotal[clef][a],dicoTotal[clef][34]))

	plt.legend()

	plt.title('pentes en fonction de {}'.format(nom),fontsize=40)
	plt.xlabel("{}".format(nom), fontsize=40)
	plt.ylabel("slope", fontsize=40)
	yticks(fontsize=40)
	xticks(fontsize=40)
	savefig('C:\\Users\\valentin\Desktop\\boulot_mines\\S3Recherche\\Python\\correlation\\pentesF{}.png'.format(nom))

def penteSans(a) :

	noms = {0 : 'echantillon',1 : 'u',2:'v',3:'Okubo Weiss',4: 'Lyapunov exp',5 : 'SST_adv',6: 'SST_AMSRE',7 : 'grad_SST_adv',8: 'age_from_bathy',9: 'lon_from_bathy',10 : 'Shannon_Darwin_mean_all',
	11: 'Shannon_Darwin_month_all',12 :'Shannon_Darwin_mean_grp',13: 'Shannon_Darwin_month_grp',14 :'Shannon_Darwin_physat_month',15 : 'Shannon_Darwin_physat_mean',16 :'retention', 17 : 'lon_origin_45d',
	18: 'lat_origin_45d',19 :'physat_type',20 : 'abundance',21: 'richness',22 : 'Shannon',23: 'Simpson',24 :'log(alpha)',25 : 'Jevenness',26 :'S.obs',27 :'S.chao1',28 : 'se.chao1',
	29 :'S.ACE',30 :'se.ACE',31 : 'distance a la loi de puissance', 32 :'nb de pentes',33 :'pente1',34: 'pente2',35 : 'long1',36 :'long2', 37 : 'poids1', 38 : 'poids2'}
	nom = noms[a] 

	dicoTotal = effacer(s)

	liste1 = list()
	liste2 = list()

	for clef in dicoTotal :
		try :
			if dicoTotal[clef][32] == 1 :
				liste1 = liste1 + [clef]

			elif dicoTotal[clef][32] ==2 :
				liste2 = liste2 + [clef]
		except :
			pass

	plt.figure(figsize=(30,20))


	bool1 = True
	bool2 = True
	bool3 = True
	bool4 = True

	for clef in liste1 :

		if clef[1] == 5 :
			c='red'
			if bool1 :
				bool1 = False
				scatter(dicoTotal[clef][a],dicoTotal[clef][33],color=c,s=120,label='taille 0.8 a 5, queue')
				annotate(clef[0],(dicoTotal[clef][a],dicoTotal[clef][33]))
			else : 
				scatter(dicoTotal[clef][a],dicoTotal[clef][33],color=c,s=120)
				annotate(clef[0],(dicoTotal[clef][a],dicoTotal[clef][33],))

		if clef[1] == 20 :
			c='magenta'
			if bool2 :
				bool2 = False
				scatter(dicoTotal[clef][a],dicoTotal[clef][33],color=c,s=120,label='taille 5 a 20, queue')
				annotate(clef[0],(dicoTotal[clef][a],dicoTotal[clef][33]))
			else : 
				scatter(dicoTotal[clef][a],dicoTotal[clef][33],color=c,s=120)
				annotate(clef[0],(dicoTotal[clef][a],dicoTotal[clef][33]))

		if clef[1] == 180 :
			c='green'
			if bool3 :
				bool3 = False
				scatter(dicoTotal[clef][a],dicoTotal[clef][33],color=c,s=120,label='taille 20 a 180, queue')
				annotate(clef[0],(dicoTotal[clef][a],dicoTotal[clef][33]))
			else : 
				scatter(dicoTotal[clef][a],dicoTotal[clef][33],color=c,s=120)
				annotate(clef[0],(dicoTotal[clef][a],dicoTotal[clef][33]))

		if clef[1] == 2000 :
			c='blue'
			if bool4 :
				bool4 = False
				scatter(dicoTotal[clef][a],dicoTotal[clef][33],color=c,s=120,label='taille 180 a 2000, queue')
				annotate(clef[0],(dicoTotal[clef][a],dicoTotal[clef][33]))
			else : 
				scatter(dicoTotal[clef][a],dicoTotal[clef][33],color=c,s=120)
				annotate(clef[0],(dicoTotal[clef][a],dicoTotal[clef][33]))

	bool1 = True
	bool2 = True
	bool3 = True
	bool4 = True

	for clef in liste2 :

		if clef[1] == 5 :
			c='red'
			if bool1 :
				bool1 = False
				scatter(dicoTotal[clef][a],dicoTotal[clef][33],color=c,s=120,label='taille 0.8 a 5, avant derniere pente')
				scatter(dicoTotal[clef][a],dicoTotal[clef][34],color=c,s=120)
				annotate(clef[0],(dicoTotal[clef][a],dicoTotal[clef][33]))
				annotate(clef[0],(dicoTotal[clef][a],dicoTotal[clef][34]))
			else : 
				scatter(dicoTotal[clef][a],dicoTotal[clef][33],color=c,s=120)
				scatter(dicoTotal[clef][a],dicoTotal[clef][34],color=c,s=120)
				annotate(clef[0],(dicoTotal[clef][a],dicoTotal[clef][33]))
				annotate(clef[0],(dicoTotal[clef][a],dicoTotal[clef][34]))

		if clef[1] == 20 :
			c='magenta'
			if bool2 :
				bool2 = False
				scatter(dicoTotal[clef][a],dicoTotal[clef][33],color=c,s=120,label='taille 5 a 20 avant derniere pente')
				scatter(dicoTotal[clef][a],dicoTotal[clef][34],color=c,s=120)
				annotate(clef[0],(dicoTotal[clef][a],dicoTotal[clef][33]))
				annotate(clef[0],(dicoTotal[clef][a],dicoTotal[clef][34]))
			else : 
				scatter(dicoTotal[clef][a],dicoTotal[clef][33],color=c,s=120)
				scatter(dicoTotal[clef][a],dicoTotal[clef][34],color=c,s=120)
				annotate(clef[0],(dicoTotal[clef][a],dicoTotal[clef][33]))
				annotate(clef[0],(dicoTotal[clef][a],dicoTotal[clef][34]))

		if clef[1] == 180 :
			c='green'
			if bool3 :
				bool3 = False
				scatter(dicoTotal[clef][a],dicoTotal[clef][33],color=c,s=120,label='taille 20 a 180 avant derniere pente')
				scatter(dicoTotal[clef][a],dicoTotal[clef][34],color=c,s=120)
				annotate(clef[0],(dicoTotal[clef][a],dicoTotal[clef][33]))
				annotate(clef[0],(dicoTotal[clef][a],dicoTotal[clef][34]))
			else : 
				scatter(dicoTotal[clef][a],dicoTotal[clef][33],color=c,s=120)
				scatter(dicoTotal[clef][a],dicoTotal[clef][34],color=c,s=120)
				annotate(clef[0],(dicoTotal[clef][a],dicoTotal[clef][33]))
				annotate(clef[0],(dicoTotal[clef][a],dicoTotal[clef][34]))

		if clef[1] == 2000 :
			c='blue'
			if bool4 :
				bool4 = False
				scatter(dicoTotal[clef][a],dicoTotal[clef][33],color=c,s=120,label='taille 180 a 2000 avant derniere pente')
				scatter(dicoTotal[clef][a],dicoTotal[clef][34],color=c,s=120)
				annotate(clef[0],(dicoTotal[clef][a],dicoTotal[clef][33]))
				annotate(clef[0],(dicoTotal[clef][a],dicoTotal[clef][34]))
			else : 
				scatter(dicoTotal[clef][a],dicoTotal[clef][33],color=c,s=120)
				scatter(dicoTotal[clef][a],dicoTotal[clef][34],color=c,s=120)
				annotate(clef[0],(dicoTotal[clef][a],dicoTotal[clef][33]))
				annotate(clef[0],(dicoTotal[clef][a],dicoTotal[clef][34]))

	plt.legend()
	plt.title('pentes en fonction de {}'.format(nom),fontsize=40)
	plt.xlabel("{}".format(nom), fontsize=40)
	plt.ylabel("slope", fontsize=40)
	yticks(fontsize=40)
	xticks(fontsize=40)
	savefig('C:\\Users\\valentin\Desktop\\boulot_mines\\S3Recherche\\Python\\correlation\\pentesF{}.png'.format(nom))


def pentesAvec() :

	indice = 3
	while indice < 32 :
		pente(indice)
		indice = indice + 1

def pentesSans() :

	indice = 3
	while indice < 32 :
		penteSans(indice)
		indice = indice + 1

def effacer(s) :


	noms = {0 : 'echantillon',1 : 'u',2:'v',3:'Okubo Weiss',4: 'Lyapunov exp',5 : 'SST_adv',6: 'SST_AMSRE',7 : 'grad_SST_adv',8: 'age_from_bathy',9: 'lon_from_bathy',10 : 'Shannon_Darwin_mean_all',
	11: 'Shannon_Darwin_month_all',12 :'Shannon_Darwin_mean_grp',13: 'Shannon_Darwin_month_grp',14 :'Shannon_Darwin_physat_month',15 : 'Shannon_Darwin_physat_mean',16 :'retention', 17 : 'lon_origin_45d',
	18: 'lat_origin_45d',19 :'physat_type',20 : 'abundance',21: 'richness',22 : 'Shannon',23: 'Simpson',24 :'log(alpha)',25 : 'Jevenness',26 :'S.obs',27 :'S.chao1',28 : 'se.chao1',
	29 :'S.ACE',30 :'se.ACE',31 : 'distance a la loi de puissance', 32 :'nb de pentes',33 :'pente1',34: 'pente2',35 : 'long1',36 :'long2', 37 : 'poids1', 38 : 'poids2'}

	dicoTotal = main()

	for clef in dicoTotal :
		try :
			if dicoTotal[clef][32] == 1:

				if dicoTotal[clef][37] > s :

					dicoTotal[clef][32]=0

			elif dicoTotal[clef][32] == 2 :

				if dicoTotal[clef][37] > s :

					if dicoTotal[clef][38] > s :

						dicoTotal[clef][32] = 0
					else :
						dicoTotal[clef][32] = 1
						dicoTotal[clef][33] = dicoTotal[clef][34]
						dicoTotal[clef][37]=dicoTotal[clef][38]
						dicoTotal[clef][35]=dicoTotal[clef][36]
				if dicoTotal[clef][38] >s and dicoTotal[clef][37] <s :
					dicoTotal[clef][32] = 1


		except :
			pass
	
	return(dicoTotal)


def enlever(s) :
	res = str()
	for l in s : 
		if l ==' ' :
			pass
		else :
			res=res + l
	return(res)

if __name__ == "__main__" :
	pentes()	
