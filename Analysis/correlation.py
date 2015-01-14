#!/usr/bin/env python
#-*- coding: utf-8 -*-

import csv
from pylab import*
import numpy
import math
import matplotlib.pyplot as plt


def main():
	k=1.15
	#import imp
	#goo = imp.load_source('algo.lancement', 'C:\\users\\valentin\\desktop\\boulot_mines\\S3Recherche\\Python\\algo_courbes\\algo_lineaire_final.py')
	#foo = imp.load_source('algo.lancement', 'C:\\users\\valentin\\desktop\\boulot_mines\\S3Recherche\\Python\\algo_courbes\\final.py')
	#foo.lancement(k)

	cor(k,5)
	cor(k,20)
	cor(k,180)
	cor(k,2000)

def cor(k,t) :
	taille = t
	donnees=list()
	catalogueParStation = dict() #Les entrees sont les 'numero de la station'
	catalogueParDonnee = dict()  #Les entrees sont les 'nom du parametre'
	premierPassage = True
	j=0

	with open('C:\\Users\\valentin\Desktop\\boulot_mines\\S3Recherche\\Python\\correlation\\Tara_stations_multisat_extract.csv', 'r') as csvfile:
		
			reader = csv.reader(csvfile, delimiter=',',quotechar='|', quoting=csv.QUOTE_MINIMAL)
			for row in reader :

				if premierPassage :
					premierPassage = False #Catalogue par station

					for param in row :   #Catalogue par donnee
						parametres = row 
						catalogueParDonnee[param]=[]
					pass



				elif row != [] :
					catalogueParStation[int(float(row[0]))] = []
					donnees = donnees + [row] #catalogue par station
					l= len(row)
					for data in row[1:l-1] : 
						if data == 'NaN' :
							catalogueParStation[int(float(row[0]))] = catalogueParStation[int(float(row[0]))] + ['Nan']
						elif data == 'Inf' :
							catalogueParStation[int(float(row[0]))] = catalogueParStation[int(float(row[0]))] + ['Inf']
						else :
							catalogueParStation[int(float(row[0]))] = catalogueParStation[int(float(row[0]))] + [float(data)]

					indice=0
					for param in parametres : #Catalogue par donnee

						if row[indice] == 'NaN':
							catalogueParDonnee[param] = catalogueParDonnee[param] + ['NaN']

						elif row[indice] == 'Inf' :
							catalogueParDonnee[param] = catalogueParDonnee[param] + ['Inf']

						else :
							catalogueParDonnee[param] = catalogueParDonnee[param] + [float(row[indice])]


						indice = indice + 1


				else :
					pass




	#On recupere les donnees des pentes extraites par l'algorithme
	#Le premier champ est le numero de la station
	#Le second champ est le l'avant derniere pente s'il y en a une
	#Le troisieme est la derniere pente
	#Le quatrieme est le nombre de pentes
	#Le cinquieme est la fraction de taille
	#Le dernier est la longueur


	pStations = list()
	pPentes1 = list()
	pPentes2 = list()
	pNb = list()
	diam = list()
	dicoPentes = dict()

	with open('C:\\Users\\valentin\Desktop\\boulot_mines\\S3Recherche\\BDD\\ProtistTV9subtabs293\\analyse\\pentes_{}.csv'.format(k), 'r') as csvfile:
		reader = csv.reader(csvfile, delimiter=';',quotechar='|', quoting=csv.QUOTE_MINIMAL)
		for row in reader :	
			pStations = pStations + [float(remove(row[0],','))]
			pPentes2 = pPentes2 + [float(remove(row[2],','))]
			pNb = pNb + [int(remove(row[3],','))]
			diam = diam + [int(remove(row[4],','))]
			if int(remove(row[3],',')) == 2 :
				pPentes1 = pPentes1 + [float(remove(row[1],','))]
				dicoPentes[(int(remove(row[0],',')),int(remove(row[4],',')))] = [int(remove(row[3],',')),float(remove(row[1],',')),float(remove(row[2],','))]
			else : 
				pPentes1 = pPentes1 + ['Null']
				dicoPentes[(int(remove(row[0],',')),int(remove(row[4],',')))] = [int(remove(row[3],',')),'Null',float(remove(row[2],','))]



	#On recupere la liste des stations du satellite
	stations = list()
	for clef in catalogueParStation :
		stations = stations + [clef]

	array = fusion(stations,pStations)
	array.sort()

	l = len(array)
	indice = 0

	dicoBool = dict()
	for i in [1,2,3] :
		for a in [True,False] :
			dicoBool[(i,a)] = True

	#Pour la SST

	plt.figure(figsize=(30,20))
	xticks(arange(l),array,rotation=90,size='small') #On trace le gradient de SST et les pentes en fonction de la station

	for station in array : #Pour chaque station, on va tracer ou le grad de SST, ou le nombre de pentes, ou les deux si possible
		col = False


		#On essaie d'abord les pentes
		try :

			if dicoPentes[(station,taille)][0] == 1 :

				if dicoBool[(1,False)] :
					dicoBool[(1,False)] = False
					plt.scatter(indice, dicoPentes[(station,taille)][2],color='red',s=70,label = 'pente unique')

				else :
					plt.scatter(indice, dicoPentes[(station,taille)][2],color='red',s=70)



			else : 
				if dicoBool[(2,True)] :
					dicoBool[(2,True)] = False
					plt.scatter(indice,dicoPentes[(station,taille)][1],color=(0,0.75,0),s=70,label = 'avant derniere pente (2)')
					plt.scatter(indice,dicoPentes[(station,taille)][2],color='green',s=70,label='derniere pente (1)')
					col=True

				else :

					plt.scatter(indice,dicoPentes[(station,taille)][1],color=(0,0.75,0),s=70)
					plt.scatter(indice,dicoPentes[(station,taille)][2],color='green',s=70)
					col=True


		except :
			pass


		#On essaie ensuite de tracer la SST
		try :
			if col :
				if dicoBool[(3,True)] :
					dicoBool[(3,True)] = False
					plt.scatter(indice,catalogueParStation[station][6],color='orange',s=70,label = 'SST avec deux pentes')
				else :
					plt.scatter(indice,catalogueParStation[station][6],color='orange',s=70)
			else : 
				if dicoBool[(3,False)] :
					dicoBool[(3,False)] = False
					plt.scatter(indice,catalogueParStation[station][6],color='blue',s=70,label='SST avec une unique pente')
				else :
					plt.scatter(indice,catalogueParStation[station][6],color='blue',s=70)


		except : 
			pass



		indice = indice + 1
	plt.title('Gradient SST et pentes par station')
	plt.legend()

	savefig('C:\\Users\\valentin\Desktop\\boulot_mines\\S3Recherche\\Python\\correlation\\comparaisonGradSST{}_{}.png'.format(k,t))
	plt.clf()

	#Pour la retention

	plt.figure(figsize=(30,20))
	xticks(arange(l),array,rotation=90,size='small') #On trace la retention et les pentes en fonction de la station
	for i in [1,2,3] :
		for a in [True,False] :
			dicoBool[(i,a)] = True

	for station in array : #Pour chaque station, on va tracer ou la retention, ou le nombre de pentes, ou les deux si possible
		col = False


		#On essaie d'abord les pentes
		try :

			if dicoPentes[(station,taille)][0] == 1 :

				if dicoBool[(1,False)] :
					dicoBool[(1,False)] = False
					plt.scatter(indice, dicoPentes[(station,taille)][2],color='red',s=70,label = 'pente unique')

				else :
					plt.scatter(indice, dicoPentes[(station,taille)][2],color='red',s=70)


			else : 
				if dicoBool[(2,True)] :
					dicoBool[(2,True)] = False
					plt.scatter(indice,dicoPentes[(station,taille)][1],color=(0,0.75,0),s=70,label = 'avant derniere pente (2)')
					plt.scatter(indice,dicoPentes[(station,taille)][2],color='green',s=70,label='derniere pente (1)')
					col=True

				else :

					plt.scatter(indice,dicoPentes[(station,taille)][1],color=(0,0.75,0),s=70)
					plt.scatter(indice,dicoPentes[(station,taille)][2],color='green',s=70)
					col=True


		except :
			pass


		#On essaie ensuite de tracer la Retention
		try :
			if col :
				if dicoBool[(3,True)] :
					dicoBool[(3,True)] = False
					plt.scatter(indice,catalogueParStation[station][15],color='orange',s=70,label = 'Retention avec deux pentes')
				else :
					plt.scatter(indice,catalogueParStation[station][15],color='orange',s=70)
			else : 
				if dicoBool[(3,False)] :
					dicoBool[(3,False)] = False
					plt.scatter(indice,catalogueParStation[station][15],color='blue',s=70,label='Retention avec une unique pente')
				else :
					plt.scatter(indice,catalogueParStation[station][15],color='blue',s=70)


		except : 
			pass



		indice = indice + 1
	plt.title('Retention et pentes par station')
	plt.legend()

	savefig('C:\\Users\\valentin\Desktop\\boulot_mines\\S3Recherche\\Python\\correlation\\comparaisonRetention{}_{}.png'.format(k,t))
	plt.clf()
	#Pour Shannon_Darwin_mean_grp

	plt.figure(figsize=(30,20))
	xticks(arange(l),array,rotation=90,size='small') #On trace Shannon_Darwin_mean_grp et les pentes en fonction de la station

	for i in [1,2,3] :
		for a in [True,False] :
			dicoBool[(i,a)] = True

	for station in array : #Pour chaque station, on va tracer ou Shannon_Darwin_mean_grp, ou le nombre de pentes, ou les deux si possible
		col = False

		#On essaie d'abord les pentes
		try :

			if dicoPentes[(station,taille)][0] == 1 :

				if dicoBool[(1,False)] :
					dicoBool[(1,False)] = False
					plt.scatter(indice, dicoPentes[(station,taille)][2],color='red',s=70,label = 'pente unique')

				else :
					plt.scatter(indice, dicoPentes[(station,taille)][2],color='red',s=70)



			else : 
				if dicoBool[(2,True)] :
					dicoBool[(2,True)] = False
					plt.scatter(indice,dicoPentes[(station,taille)][1],color=(0,0.75,0),s=70,label = 'avant derniere pente (2)')
					plt.scatter(indice,dicoPentes[(station,taille)][2],color='green',s=70,label='derniere pente (1)')
					col=True

				else :

					plt.scatter(indice,dicoPentes[(station,taille)][1],color=(0,0.75,0),s=70)
					plt.scatter(indice,dicoPentes[(station,taille)][2],color='green',s=70)
					col=True



		except :
			pass


		#On essaie ensuite de tracer Shannon_Darwin_mean_grp
		try :
			if col :
				if dicoBool[(3,True)] :
					dicoBool[(3,True)] = False
					plt.scatter(indice,catalogueParStation[station][11],color='orange',s=70,label = 'Shannon_Darwin_mean_grp avec deux pentes')
				else :
					plt.scatter(indice,catalogueParStation[station][11],color='orange',s=70)
			else : 
				if dicoBool[(3,False)] :
					dicoBool[(3,False)] = False
					plt.scatter(indice,catalogueParStation[station][11],color='blue',s=70,label='Shannon_Darwin_mean_grp avec une unique pente')
				else :
					plt.scatter(indice,catalogueParStation[station][11],color='blue',s=70)
					print(indice)


		except : 
			pass



		indice = indice + 1
	plt.title('Shannon_Darwin_mean_grp et pentes par station')
	plt.legend()

	savefig('C:\\Users\\valentin\Desktop\\boulot_mines\\S3Recherche\\Python\\correlation\\comparaisonShannon_Darwin_mean_grp{}_{}.png'.format(k,t))



def trouver(l,obj) :
	indice=-1
	for item in l :
		indice=indice+1
		if item == obj :
			return(indice)
	return(False)

def fusion(a,b) :
	a.sort()
	b.sort()

	if a[len(a)-1]<b[len(b)-1] :
		l1 = b
		l2 = a
	else : 
		l1 = a
		l2 = b

	res = list()
	indice=0 
	l=len(l2)
	dernier1=-1
	dernier2=-1
	for i in l1 :
		pos=0
		for j in l2 :

			if j>dernier1 and j!=dernier2 and j<i :
				res = res + [int(j)]
				j=dernier2

		res=res+[i]
		dernier1 = i

	return(res)

def remove(l,item) : 
	res = str()

	for data in l :

		if item == data :
			pass
		else :
			res = res + data

	return(res)


if __name__ == "__main__" :
	main()