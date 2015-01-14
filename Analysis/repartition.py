#!/usr/bin/env python
#-*- coding: utf-8 -*-

import csv
from pylab import*
import numpy
import math
import matplotlib.pyplot as plt

from allTest import k,s


def avec():



	pStations = list()
	pPentes1 = list()
	pPentes2 = list()
	pNb = list()
	diam = list()
	pLong1 = list()
	pLong2 = list()
	dicoPentes = dict()


	#On recupere les donnees des pentes extraites par l'algorithme
	#Le premier champ est le numero de la station
	#Le second champ est le l'avant derniere pente s'il y en a une (pente1)
	#Le troisieme est la derniere pente (pente2)
	#Le quatrieme est le nombre de pentes
	#Le cinquieme est la fraction de taille
	#Le dernier (ou les deux derniers) et la longueur


	with open('C:\\Users\\valentin\Desktop\\boulot_mines\\S3Recherche\\Resultats\\log_log\\10_{}\\toutes\\pentes_{}.csv'.format(k,k), 'r') as csvfile:
		reader = csv.reader(csvfile, delimiter=';',quotechar='|', quoting=csv.QUOTE_MINIMAL)
		for row in reader :	
			pStations = pStations + [float(remove(row[0],','))]
			pPentes2 = pPentes2 + [float(remove(row[2],','))]
			pNb = pNb + [int(remove(row[3],','))]
			diam = diam + [int(remove(row[4],','))]
			if int(remove(row[3],',')) == 1 :
				pPentes1 = pPentes1 + ['Null']
				pLong1 = pLong1 + ['Null']
				pLong2 = pLong2 + [float(remove(row[5],','))]
				dicoPentes[(int(remove(row[0],',')),int(remove(row[4],',')))] = [int(remove(row[3],',')),'Null',float(remove(row[2],',')),float(remove(row[5],','))]

			else :
				pLong1 = pLong1 + [float(remove(row[5],','))]
				pLong2 = pLong2 + [float(remove(row[6],','))]
				pPentes1 = pPentes1 + [float(remove(row[1],','))]
				dicoPentes[(int(remove(row[0],',')),int(remove(row[4],',')))] = [int(remove(row[3],',')),float(remove(row[1],',')),float(remove(row[2],',')),float(remove(row[5],',')),float(remove(row[6],','))]


	stations = list()
	
	plt.figure(figsize=(30,20))
	plt.title('pente(s) en fonction de la taille du segment identifie',fontsize=40)


	dicoBool = dict()
	for taille in [5,20,180,2000] :
		for i in [1,2] :
			dicoBool[(taille,i)] = True

	for clef in dicoPentes :
		stations = stations + [clef]

		if clef[1] == 5 :
			a='taille 0.8 a 5'
			c=(1,0,0)

		elif clef[1] == 20 :
			a='taille 5 a 20'
			c=(1,0,1)

		elif clef[1] == 2000 :
			a='taille 180 a 2000'
			c=(0,0,1)

		elif clef[1] == 180 :
			a='taille 20 a 180'
			c=(0,1,0)


		if dicoPentes[clef][0] == 1 :

			if dicoBool[(clef[1],dicoPentes[clef][0])] :
				dicoBool[(clef[1],dicoPentes[clef][0])] = False
				scatter(dicoPentes[clef][3],dicoPentes[clef][2],color=c,s=120,label='derniere pente (1), ' + a)
				annotate(clef[0],(dicoPentes[clef][3],dicoPentes[clef][2]))

			else : 
				scatter(dicoPentes[clef][3],dicoPentes[clef][2],color=c,s=120)
				annotate(clef[0],(dicoPentes[clef][3],dicoPentes[clef][2]))

		else :
			cc = (0.5*c[0],0.5*c[1],0.5*c[2])

			if dicoBool[(clef[1],dicoPentes[clef][0])] :
				dicoBool[(clef[1],dicoPentes[clef][0])] = False
				scatter(dicoPentes[clef][3],dicoPentes[clef][1],color=cc,s=120,label='avant derniere pente(2), ' + a)
				annotate(clef[0],(dicoPentes[clef][3],dicoPentes[clef][1]))
				scatter(dicoPentes[clef][4],dicoPentes[clef][2],color=c,s=120)
				annotate(clef[0],(dicoPentes[clef][4],dicoPentes[clef][2]))

			else :

				scatter(dicoPentes[clef][3],dicoPentes[clef][1],color=cc,s=120)
				annotate(clef[0],(dicoPentes[clef][3],dicoPentes[clef][1]))
				scatter(dicoPentes[clef][4],dicoPentes[clef][2],color=c,s=120)
				annotate(clef[0],(dicoPentes[clef][4],dicoPentes[clef][2]))				


	plt.legend()
	
	plt.xlabel("size of the fit", fontsize=40)
	plt.ylabel("slope", fontsize=40)
	yticks(fontsize=40)
	xticks(fontsize=40)
	savefig('C:\\Users\\valentin\Desktop\\boulot_mines\\S3Recherche\\Python\\correlation\\penteFonctionTailleAvec_{}.png'.format(k))

	#On recommence avec cette fois uniquement la queue

	stations = list()
	
	plt.figure(figsize=(30,20))
	plt.title('pente(s) en fonction de la taille du segment identifie',fontsize=40)


	dicoBool = dict()
	for taille in [5,20,180,2000] :
		for i in [1,2] :
			dicoBool[(taille,i)] = True

	for clef in dicoPentes :
		stations = stations + [clef]

		if clef[1] == 5 :
			a='taille 0.8 a 5'
			c=(1,0,0)

		elif clef[1] == 20 :
			a='taille 5 a 20'
			c=(1,0,1)

		elif clef[1] == 2000 :
			a='taille 180 a 2000'
			c=(0,0,1)

		elif clef[1] == 180 :
			a='taille 20 a 180'
			c=(0,1,0)


		if dicoPentes[clef][0] == 1 :

			if dicoBool[(clef[1],dicoPentes[clef][0])] :
				dicoBool[(clef[1],dicoPentes[clef][0])] = False
				scatter(dicoPentes[clef][3],dicoPentes[clef][2],color=c,s=120,label='derniere pente (1), ' + a)
				annotate(clef[0],(dicoPentes[clef][3],dicoPentes[clef][2]))

			else : 
				scatter(dicoPentes[clef][3],dicoPentes[clef][2],color=c,s=120)
				annotate(clef[0],(dicoPentes[clef][3],dicoPentes[clef][2]))

		else :
			cc = (0.5*c[0],0.5*c[1],0.5*c[2])

			if dicoBool[(clef[1],dicoPentes[clef][0])] :
				dicoBool[(clef[1],dicoPentes[clef][0])] = False
				scatter(dicoPentes[clef][4],dicoPentes[clef][2],color=c,s=120,label='derniere pente (1), ' + a)
				annotate(clef[0],(dicoPentes[clef][4],dicoPentes[clef][2]))

			else :

				scatter(dicoPentes[clef][4],dicoPentes[clef][2],color=c,s=120)
				annotate(clef[0],(dicoPentes[clef][4],dicoPentes[clef][2]))				


	plt.legend()
	
	plt.xlabel("size of the fit", fontsize=40)
	plt.ylabel("slope of the queue", fontsize=40)
	yticks(fontsize=40)
	xticks(fontsize=40)
	savefig('C:\\Users\\valentin\Desktop\\boulot_mines\\S3Recherche\\Python\\correlation\\QueueFonctionTailleAvec_{}.png'.format(k))

def sans():



	pStations = list()
	pPentes1 = list()
	pPentes2 = list()
	pNb = list()
	diam = list()
	pLong1 = list()
	pLong2 = list()
	dicoPentes = dict()


	#On recupere les donnees des pentes extraites par l'algorithme
	#Le premier champ est le numero de la station
	#Le second champ est le l'avant derniere pente s'il y en a une (pente1)
	#Le troisieme est la derniere pente (pente2)
	#Le quatrieme est le nombre de pentes
	#Le cinquieme est la fraction de taille
	#Le dernier (ou les deux derniers) et la longueur


	with open('C:\\Users\\valentin\Desktop\\boulot_mines\\S3Recherche\\Resultats\\log_log\\10_{}\\toutes\\pentes_{}.csv'.format(k,k), 'r') as csvfile:
		reader = csv.reader(csvfile, delimiter=';',quotechar='|', quoting=csv.QUOTE_MINIMAL)
		for row in reader :	
			pStations = pStations + [float(remove(row[0],','))]
			pPentes2 = pPentes2 + [float(remove(row[2],','))]
			pNb = pNb + [int(remove(row[3],','))]
			diam = diam + [int(remove(row[4],','))]
			if int(remove(row[3],',')) == 1 :
				pPentes1 = pPentes1 + ['Null']
				pLong1 = pLong1 + ['Null']
				pLong2 = pLong2 + [float(remove(row[5],','))]
				dicoPentes[(int(remove(row[0],',')),int(remove(row[4],',')))] = [int(remove(row[3],',')),'Null',float(remove(row[2],',')),float(remove(row[5],',')),float(remove(row[6],','))]

			else :
				pLong1 = pLong1 + [float(remove(row[5],','))]
				pLong2 = pLong2 + [float(remove(row[6],','))]
				pPentes1 = pPentes1 + [float(remove(row[1],','))]
				dicoPentes[(int(remove(row[0],',')),int(remove(row[4],',')))] = [int(remove(row[3],',')),float(remove(row[1],',')),float(remove(row[2],',')),float(remove(row[5],',')),float(remove(row[6],',')),float(remove(row[7],',')),float(remove(row[8],','))]


	stations = list()
	
	plt.figure(figsize=(30,20))
	plt.title('pente(s) en fonction de la taille du segment identifie',fontsize=40)


	dicoBool = dict()
	for taille in [5,20,180,2000] :
		for i in [1,2] :
			dicoBool[(taille,i)] = True

	for clef in dicoPentes :
		stations = stations + [clef]

		if clef[1] == 5 :
			a='taille 0.8 a 5'
			c=(1,0,0)

		elif clef[1] == 20 :
			a='taille 5 a 20'
			c=(1,0,1)

		elif clef[1] == 2000 :
			a='taille 180 a 2000'
			c=(0,0,1)

		elif clef[1] == 180 :
			a='taille 20 a 180'
			c=(0,1,0)


		if dicoPentes[clef][0] == 1 :
			if dicoPentes[clef][4] < s :

				if dicoBool[(clef[1],dicoPentes[clef][0])] :
					dicoBool[(clef[1],dicoPentes[clef][0])] = False
					scatter(dicoPentes[clef][3],dicoPentes[clef][2],color=c,s=120,label='derniere pente (1), ' + a)
					annotate(clef[0],(dicoPentes[clef][3],dicoPentes[clef][2]))

				else : 
					scatter(dicoPentes[clef][3],dicoPentes[clef][2],color=c,s=120)
					annotate(clef[0],(dicoPentes[clef][3],dicoPentes[clef][2]))

		else :
			cc = (0.5*c[0],0.5*c[1],0.5*c[2])

			if dicoBool[(clef[1],dicoPentes[clef][0])] :

				if dicoPentes[clef][5] < s : 
					dicoBool[(clef[1],dicoPentes[clef][0])] = False
					scatter(dicoPentes[clef][3],dicoPentes[clef][1],color=cc,s=120,label='avant derniere pente(2), ' + a)
					annotate(clef[0],(dicoPentes[clef][3],dicoPentes[clef][1]))
				if dicoPentes[clef][6]<s :
					scatter(dicoPentes[clef][4],dicoPentes[clef][2],color=c,s=120)
					annotate(clef[0],(dicoPentes[clef][4],dicoPentes[clef][2]))

			else :
				if dicoPentes[clef][5] <s : 
					scatter(dicoPentes[clef][3],dicoPentes[clef][1],color=cc,s=120)
					annotate(clef[0],(dicoPentes[clef][3],dicoPentes[clef][1]))
				if dicoPentes[clef][6] <s : 
					scatter(dicoPentes[clef][4],dicoPentes[clef][2],color=c,s=120)
					annotate(clef[0],(dicoPentes[clef][4],dicoPentes[clef][2]))				


	plt.legend()
	
	plt.xlabel("size of the fit", fontsize=40)
	plt.ylabel("slope", fontsize=40)
	yticks(fontsize=40)
	xticks(fontsize=40)
	savefig('C:\\Users\\valentin\Desktop\\boulot_mines\\S3Recherche\\Python\\correlation\\penteFonctionTailleSans_{}.png'.format(k))

def remove(l,item) : 
	res = str()

	for data in l :

		if item == data :
			pass
		else :
			res = res + data

	return(res)


if __name__ == "__main__" :
	avec()	

