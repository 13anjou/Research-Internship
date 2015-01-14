#!/usr/bin/env python
#-*- coding: utf-8 -*-

from allTest import k, s
import csv
from pylab import*
import numpy
import math
import matplotlib.pyplot as plt
import dico as data



def main() :

	dicoTotal = data.main()

	liste1 = list()
	liste2 = list()
	x1=list()
	x2=list()
	x3=list()
	x4=list()

	for clef in dicoTotal :
		try :
			if dicoTotal[clef][32] == 1 :
				liste1 = liste1 + [clef]

			elif dicoTotal[clef][32] ==2 :
				liste2 = liste2 + [clef]
		except :
			pass

	listeStation = list()

	for clef in dicoTotal :

		ajout = True

		for station in listeStation :
			if station == clef[0] :
				ajout = False

		if ajout :

			listeStation = listeStation + [clef[0]]

	plt.figure(figsize=(20,20))
	l=len(listeStation)	
	listeStation.sort()
	yticks(arange(l),listeStation,fontsize=32)
	xticks(fontsize=32)

	bool1 = True
	bool2 = True
	bool3 = True
	bool4 = True

	indice = 0 
	for s in listeStation :
		
		for clef in liste1 :
			if s == clef[0] :

				if clef[1] == 5 :
					c='red'
					if bool1 :
						bool1 = False
						#scatter(dicoTotal[clef][33],indice,color=c,s=120,label='taille 0.8 a 5')
						#annotate(clef[0],(dicoTotal[clef][33],indice))
						x1=x1+[dicoTotal[clef][33]]
					else : 
						#scatter(dicoTotal[clef][33],indice,color=c,s=120)
						#annotate(clef[0],(dicoTotal[clef][33],indice,))
						x1=x1+[dicoTotal[clef][33]]

				if clef[1] == 20 :
					c='magenta'
					if bool2 :
						bool2 = False
						#scatter(dicoTotal[clef][33],indice,color=c,s=120,label='taille 5 a 20')
						#annotate(clef[0],(dicoTotal[clef][33],indice))
						x2=x2+[dicoTotal[clef][33]]
					else : 
						#scatter(dicoTotal[clef][33],indice,color=c,s=120)
						#annotate(clef[0],(dicoTotal[clef][33],indice))
						x2=x2+[dicoTotal[clef][33]]

				if clef[1] == 180 :
					c='green'
					if bool3 :
						bool3 = False
						#scatter(dicoTotal[clef][33],indice,color=c,s=120,label='taille 20 a 180')
						#annotate(clef[0],(dicoTotal[clef][33],indice))
						x3=x3+[dicoTotal[clef][33]]
					else : 
						#scatter(dicoTotal[clef][33],indice,color=c,s=120)
						#annotate(clef[0],(dicoTotal[clef][33],indice))
						x3=x3+[dicoTotal[clef][33]]

				if clef[1] == 2000 :
					c='blue'
					if bool4 :
						bool4 = False
						#scatter(dicoTotal[clef][33],indice,color=c,s=120,label='taille 180 a 2000')
						#annotate(clef[0],(dicoTotal[clef][33],indice))
						x4=x4+[dicoTotal[clef][33]]
					else : 
						#scatter(dicoTotal[clef][33],indice,color=c,s=120)
						#annotate(clef[0],(dicoTotal[clef][33],indice))
						x4=x4+[dicoTotal[clef][33]]

		indice = indice + 1

	bool1 = True
	bool2 = True
	bool3 = True
	bool4 = True

	indice = 0
	for s in listeStation :
		
		for clef in liste2 :
			if s == clef[0] :

				if clef[1] == 5 :
					c='red'
					cc=(0.75,0.1,0.3)
					if bool1 :
						bool1 = False
						#scatter(dicoTotal[clef][33],indice,color=c,s=120,label='taille 0.8 a 5, avant derniere pente')
						#scatter(dicoTotal[clef][34],indice,color=cc,s=120,label='taille 0.8 a 5, tail')
						#annotate(clef[0],(dicoTotal[clef][33],indice))
						#annotate(clef[0],(dicoTotal[clef][34],indice))
						x1=x1+[dicoTotal[clef][33]]
						x1=x1+[dicoTotal[clef][34]]
					else : 
						#scatter(dicoTotal[clef][33],indice,color=c,s=120)
						#scatter(dicoTotal[clef][34],indice,color=cc,s=120)
						#annotate(clef[0],(dicoTotal[clef][33],indice))
						#annotate(clef[0],(dicoTotal[clef][34],indice))
						x1=x1+[dicoTotal[clef][33]]
						x1=x1+[dicoTotal[clef][34]]

				if clef[1] == 20 :
					c='magenta'
					cc=(0.5,0,0.5)
					if bool2 :
						bool2 = False
						#scatter(dicoTotal[clef][33],indice,color=c,s=120,label='taille 5 a 20 avant derniere pente')
						#scatter(dicoTotal[clef][34],indice,color=cc,s=120,label='taille 0.8 a 5, tail')
						#annotate(clef[0],(dicoTotal[clef][33],indice))
						#annotate(clef[0],(dicoTotal[clef][34],indice))
						x2=x2+[dicoTotal[clef][33]]
						x2=x2+[dicoTotal[clef][34]]
					else : 
						#scatter(dicoTotal[clef][33],indice,color=c,s=120)
						#scatter(dicoTotal[clef][34],indice,color=cc,s=120)
						#annotate(clef[0],(dicoTotal[clef][33],indice))
						#annotate(clef[0],(dicoTotal[clef][34],indice))
						x2=x2+[dicoTotal[clef][33]]
						x2=x2+[dicoTotal[clef][34]]

				if clef[1] == 180 :
					c='green'
					cc=(0.3,0.75,0.1)
					if bool3 :
						bool3 = False
						#scatter(dicoTotal[clef][33],indice,color=c,s=120,label='taille 20 a 180 avant derniere pente')
						#scatter(dicoTotal[clef][34],indice,color=cc,s=120,label='taille 0.8 a 5, tail')
						#annotate(clef[0],(dicoTotal[clef][33],indice))
						#annotate(clef[0],(dicoTotal[clef][34],indice))
						x3=x3+[dicoTotal[clef][33]]
						x3=x3+[dicoTotal[clef][34]]
					else : 
						#scatter(dicoTotal[clef][33],indice,color=c,s=120)
						#scatter(dicoTotal[clef][34],indice,color=cc,s=120)
						#annotate(clef[0],(dicoTotal[clef][33],indice))
						#annotate(clef[0],(dicoTotal[clef][34],indice))
						x3=x3+[dicoTotal[clef][33]]
						x3=x3+[dicoTotal[clef][34]]

				if clef[1] == 2000 :
					c='blue'
					cc=(0.1,0.3,0.75)
					if bool4 :
						bool4 = False
						#scatter(dicoTotal[clef][33],indice,color=c,s=120,label='taille 180 a 2000 avant derniere pente')
						#scatter(dicoTotal[clef][34],indice,color=cc,s=120,label='taille 0.8 a 5, tail')
						#annotate(clef[0],(dicoTotal[clef][33],indice))
						#annotate(clef[0],(dicoTotal[clef][34],indice))
						x4=x4+[dicoTotal[clef][33]]
						x4=x4+[dicoTotal[clef][34]]
					else : 
						#scatter(dicoTotal[clef][33],indice,color=c,s=120)
						#scatter(dicoTotal[clef][34],indice,color=cc,s=120)
						#annotate(clef[0],(dicoTotal[clef][33],indice))
						#annotate(clef[0],(dicoTotal[clef][34],indice))
						x4=x4+[dicoTotal[clef][33]]
						x4=x4+[dicoTotal[clef][34]]
		indice = indice + 1

	vector = [x1,x2,x3,x4]
	n, bins, patches = hist(vector, 20,  normed=False, histtype='bar',color=['red', 'magenta', 'green','blue'])
	plt.xlabel("size of the fit", fontsize=32)
	plt.ylabel("frequency", fontsize=32)
	plt.legend()

	plt.title('histogram of the slopes',fontsize=32)
	savefig('C:\\Users\\valentin\Desktop\\boulot_mines\\S3Recherche\\Python\\correlation\\histogramAll.png')

	#On recommence avec uniquement les tails

	dicoTotal = data.main()

	liste1 = list()
	liste2 = list()
	x1=list()
	x2=list()
	x3=list()
	x4=list()

	for clef in dicoTotal :
		try :
			if dicoTotal[clef][32] == 1 :
				liste1 = liste1 + [clef]

			elif dicoTotal[clef][32] ==2 :
				liste2 = liste2 + [clef]
		except :
			pass

	listeStation = list()

	for clef in dicoTotal :

		ajout = True

		for station in listeStation :
			if station == clef[0] :
				ajout = False

		if ajout :

			listeStation = listeStation + [clef[0]]

	plt.figure(figsize=(20,20))
	l=len(listeStation)	
	listeStation.sort()
	yticks(arange(l),listeStation,fontsize=32)
	xticks(fontsize=32)


	bool1 = True
	bool2 = True
	bool3 = True
	bool4 = True

	indice = 0 
	for s in listeStation :
		
		for clef in liste1 :
			if s == clef[0] :

				if clef[1] == 5 :
					c='red'
					if bool1 :
						bool1 = False
						#scatter(dicoTotal[clef][33],indice,color=c,s=120,label='taille 0.8 a 5')
						#annotate(clef[0],(dicoTotal[clef][33],indice))
						x1=x1+[dicoTotal[clef][33]]
					else : 
						#scatter(dicoTotal[clef][33],indice,color=c,s=120)
						#annotate(clef[0],(dicoTotal[clef][33],indice,))
						x1=x1+[dicoTotal[clef][33]]

				if clef[1] == 20 :
					c='magenta'
					if bool2 :
						bool2 = False
						#scatter(dicoTotal[clef][33],indice,color=c,s=120,label='taille 5 a 20')
						#annotate(clef[0],(dicoTotal[clef][33],indice))
						x2=x2+[dicoTotal[clef][33]]
					else : 
						#scatter(dicoTotal[clef][33],indice,color=c,s=120)
						#annotate(clef[0],(dicoTotal[clef][33],indice))
						x2=x2+[dicoTotal[clef][33]]

				if clef[1] == 180 :
					c='green'
					if bool3 :
						bool3 = False
						#scatter(dicoTotal[clef][33],indice,color=c,s=120,label='taille 20 a 180')
						#annotate(clef[0],(dicoTotal[clef][33],indice))
						x3=x3+[dicoTotal[clef][33]]
					else : 
						#scatter(dicoTotal[clef][33],indice,color=c,s=120)
						#annotate(clef[0],(dicoTotal[clef][33],indice))
						x3=x3+[dicoTotal[clef][33]]

				if clef[1] == 2000 :
					c='blue'
					if bool4 :
						bool4 = False
						#scatter(dicoTotal[clef][33],indice,color=c,s=120,label='taille 180 a 2000')
						#annotate(clef[0],(dicoTotal[clef][33],indice))
						x4=x4+[dicoTotal[clef][33]]
					else : 
						#scatter(dicoTotal[clef][33],indice,color=c,s=120)
						#annotate(clef[0],(dicoTotal[clef][33],indice))
						x4=x4+[dicoTotal[clef][33]]

		indice = indice + 1

	bool1 = True
	bool2 = True
	bool3 = True
	bool4 = True

	indice = 0
	for s in listeStation :
		
		for clef in liste2 :
			if s == clef[0] :

				if clef[1] == 5 :
					c='red'
					cc=(0.75,0.1,0.3)
					if bool1 :
						bool1 = False
						#scatter(dicoTotal[clef][33],indice,color=c,s=120,label='taille 0.8 a 5, avant derniere pente')
						#scatter(dicoTotal[clef][34],indice,color=cc,s=120,label='taille 0.8 a 5, tail')
						#annotate(clef[0],(dicoTotal[clef][33],indice))
						#annotate(clef[0],(dicoTotal[clef][34],indice))
						x1=x1+[dicoTotal[clef][33]]
					else : 
						#scatter(dicoTotal[clef][33],indice,color=c,s=120)
						#scatter(dicoTotal[clef][34],indice,color=cc,s=120)
						#annotate(clef[0],(dicoTotal[clef][33],indice))
						#annotate(clef[0],(dicoTotal[clef][34],indice))
						x1=x1+[dicoTotal[clef][33]]

				if clef[1] == 20 :
					c='magenta'
					cc=(0.5,0,0.5)
					if bool2 :
						bool2 = False
						#scatter(dicoTotal[clef][33],indice,color=c,s=120,label='taille 5 a 20 avant derniere pente')
						#scatter(dicoTotal[clef][34],indice,color=cc,s=120,label='taille 0.8 a 5, tail')
						#annotate(clef[0],(dicoTotal[clef][33],indice))
						#annotate(clef[0],(dicoTotal[clef][34],indice))
						x2=x2+[dicoTotal[clef][33]]
					else : 
						#scatter(dicoTotal[clef][33],indice,color=c,s=120)
						#scatter(dicoTotal[clef][34],indice,color=cc,s=120)
						#annotate(clef[0],(dicoTotal[clef][33],indice))
						#annotate(clef[0],(dicoTotal[clef][34],indice))
						x2=x2+[dicoTotal[clef][33]]

				if clef[1] == 180 :
					c='green'
					cc=(0.3,0.75,0.1)
					if bool3 :
						bool3 = False
						#scatter(dicoTotal[clef][33],indice,color=c,s=120,label='taille 20 a 180 avant derniere pente')
						#scatter(dicoTotal[clef][34],indice,color=cc,s=120,label='taille 0.8 a 5, tail')
						#annotate(clef[0],(dicoTotal[clef][33],indice))
						#annotate(clef[0],(dicoTotal[clef][34],indice))
						x3=x3+[dicoTotal[clef][33]]
					else : 
						#scatter(dicoTotal[clef][33],indice,color=c,s=120)
						#scatter(dicoTotal[clef][34],indice,color=cc,s=120)
						#annotate(clef[0],(dicoTotal[clef][33],indice))
						#annotate(clef[0],(dicoTotal[clef][34],indice))
						x3=x3+[dicoTotal[clef][33]]

				if clef[1] == 2000 :
					c='blue'
					cc=(0.1,0.3,0.75)
					if bool4 :
						bool4 = False
						#scatter(dicoTotal[clef][33],indice,color=c,s=120,label='taille 180 a 2000 avant derniere pente')
						#scatter(dicoTotal[clef][34],indice,color=cc,s=120,label='taille 0.8 a 5, tail')
						#annotate(clef[0],(dicoTotal[clef][33],indice))
						#annotate(clef[0],(dicoTotal[clef][34],indice))
						x4=x4+[dicoTotal[clef][33]]
					else : 
						#scatter(dicoTotal[clef][33],indice,color=c,s=120)
						#scatter(dicoTotal[clef][34],indice,color=cc,s=120)
						#annotate(clef[0],(dicoTotal[clef][33],indice))
						#annotate(clef[0],(dicoTotal[clef][34],indice))
						x4=x4+[dicoTotal[clef][33]]
		indice = indice + 1

	vector = [x1,x2,x3,x4]
	n, bins, patches = hist(vector, 20,  normed=False, histtype='bar',color=['red', 'magenta', 'green','blue'])
	plt.xlabel("size of the fit", fontsize=32)
	plt.ylabel("frequency", fontsize=32)
	plt.legend()

	plt.title('histogram of the slopes',fontsize = 40)
	savefig('C:\\Users\\valentin\Desktop\\boulot_mines\\S3Recherche\\Python\\correlation\\histogramtail.png')


def sans() :
	from allTest import k, s
	dicoTotal = data.effacer(s)

	liste1 = list()
	liste2 = list()
	x1=list()
	x2=list()
	x3=list()
	x4=list()

	for clef in dicoTotal :
		try :
			if dicoTotal[clef][32] == 1 :
				liste1 = liste1 + [clef]

			elif dicoTotal[clef][32] ==2 :
				liste2 = liste2 + [clef]
		except :
			pass

	listeStation = list()

	for clef in dicoTotal :

		ajout = True

		for station in listeStation :
			if station == clef[0] :
				ajout = False

		if ajout :

			listeStation = listeStation + [clef[0]]

	plt.figure(figsize=(20,20))
	l=len(listeStation)	
	listeStation.sort()
	yticks(arange(l),listeStation,fontsize=32)
	xticks(fontsize=32)


	bool1 = True
	bool2 = True
	bool3 = True
	bool4 = True

	indice = 0 
	for s in listeStation :
		
		for clef in liste1 :
			if s == clef[0] :

				if clef[1] == 5 :
					c='red'
					if bool1 :
						bool1 = False
						#scatter(dicoTotal[clef][33],indice,color=c,s=120,label='taille 0.8 a 5')
						#annotate(clef[0],(dicoTotal[clef][33],indice))
						x1=x1+[dicoTotal[clef][33]]
					else : 
						#scatter(dicoTotal[clef][33],indice,color=c,s=120)
						#annotate(clef[0],(dicoTotal[clef][33],indice,))
						x1=x1+[dicoTotal[clef][33]]

				if clef[1] == 20 :
					c='magenta'
					if bool2 :
						bool2 = False
						#scatter(dicoTotal[clef][33],indice,color=c,s=120,label='taille 5 a 20')
						#annotate(clef[0],(dicoTotal[clef][33],indice))
						x2=x2+[dicoTotal[clef][33]]
					else : 
						#scatter(dicoTotal[clef][33],indice,color=c,s=120)
						#annotate(clef[0],(dicoTotal[clef][33],indice))
						x2=x2+[dicoTotal[clef][33]]

				if clef[1] == 180 :
					c='green'
					if bool3 :
						bool3 = False
						#scatter(dicoTotal[clef][33],indice,color=c,s=120,label='taille 20 a 180')
						#annotate(clef[0],(dicoTotal[clef][33],indice))
						x3=x3+[dicoTotal[clef][33]]
					else : 
						#scatter(dicoTotal[clef][33],indice,color=c,s=120)
						#annotate(clef[0],(dicoTotal[clef][33],indice))
						x3=x3+[dicoTotal[clef][33]]

				if clef[1] == 2000 :
					c='blue'
					if bool4 :
						bool4 = False
						#scatter(dicoTotal[clef][33],indice,color=c,s=120,label='taille 180 a 2000')
						#annotate(clef[0],(dicoTotal[clef][33],indice))
						x4=x4+[dicoTotal[clef][33]]
					else : 
						#scatter(dicoTotal[clef][33],indice,color=c,s=120)
						#annotate(clef[0],(dicoTotal[clef][33],indice))
						x4=x4+[dicoTotal[clef][33]]

		indice = indice + 1

	bool1 = True
	bool2 = True
	bool3 = True
	bool4 = True

	indice = 0
	for s in listeStation :
		
		for clef in liste2 :
			if s == clef[0] :

				if clef[1] == 5 :
					c='red'
					cc=(0.75,0.1,0.3)
					if bool1 :
						bool1 = False
						#scatter(dicoTotal[clef][33],indice,color=c,s=120,label='taille 0.8 a 5, avant derniere pente')
						#scatter(dicoTotal[clef][34],indice,color=cc,s=120,label='taille 0.8 a 5, tail')
						#annotate(clef[0],(dicoTotal[clef][33],indice))
						#annotate(clef[0],(dicoTotal[clef][34],indice))
						x1=x1+[dicoTotal[clef][33]]
						x1=x1+[dicoTotal[clef][34]]
					else : 
						#scatter(dicoTotal[clef][33],indice,color=c,s=120)
						#scatter(dicoTotal[clef][34],indice,color=cc,s=120)
						#annotate(clef[0],(dicoTotal[clef][33],indice))
						#annotate(clef[0],(dicoTotal[clef][34],indice))
						x1=x1+[dicoTotal[clef][33]]
						x1=x1+[dicoTotal[clef][34]]

				if clef[1] == 20 :
					c='magenta'
					cc=(0.5,0,0.5)
					if bool2 :
						bool2 = False
						#scatter(dicoTotal[clef][33],indice,color=c,s=120,label='taille 5 a 20 avant derniere pente')
						#scatter(dicoTotal[clef][34],indice,color=cc,s=120,label='taille 0.8 a 5, tail')
						#annotate(clef[0],(dicoTotal[clef][33],indice))
						#annotate(clef[0],(dicoTotal[clef][34],indice))
						x2=x2+[dicoTotal[clef][33]]
						x2=x2+[dicoTotal[clef][34]]
					else : 
						#scatter(dicoTotal[clef][33],indice,color=c,s=120)
						#scatter(dicoTotal[clef][34],indice,color=cc,s=120)
						#annotate(clef[0],(dicoTotal[clef][33],indice))
						#annotate(clef[0],(dicoTotal[clef][34],indice))
						x2=x2+[dicoTotal[clef][33]]
						x2=x2+[dicoTotal[clef][34]]

				if clef[1] == 180 :
					c='green'
					cc=(0.3,0.75,0.1)
					if bool3 :
						bool3 = False
						#scatter(dicoTotal[clef][33],indice,color=c,s=120,label='taille 20 a 180 avant derniere pente')
						#scatter(dicoTotal[clef][34],indice,color=cc,s=120,label='taille 0.8 a 5, tail')
						#annotate(clef[0],(dicoTotal[clef][33],indice))
						#annotate(clef[0],(dicoTotal[clef][34],indice))
						x3=x3+[dicoTotal[clef][33]]
						x3=x3+[dicoTotal[clef][34]]
					else : 
						#scatter(dicoTotal[clef][33],indice,color=c,s=120)
						#scatter(dicoTotal[clef][34],indice,color=cc,s=120)
						#annotate(clef[0],(dicoTotal[clef][33],indice))
						#annotate(clef[0],(dicoTotal[clef][34],indice))
						x3=x3+[dicoTotal[clef][33]]
						x3=x3+[dicoTotal[clef][34]]

				if clef[1] == 2000 :
					c='blue'
					cc=(0.1,0.3,0.75)
					if bool4 :
						bool4 = False
						#scatter(dicoTotal[clef][33],indice,color=c,s=120,label='taille 180 a 2000 avant derniere pente')
						#scatter(dicoTotal[clef][34],indice,color=cc,s=120,label='taille 0.8 a 5, tail')
						#annotate(clef[0],(dicoTotal[clef][33],indice))
						#annotate(clef[0],(dicoTotal[clef][34],indice))
						x4=x4+[dicoTotal[clef][33]]
						x4=x4+[dicoTotal[clef][34]]
					else : 
						#scatter(dicoTotal[clef][33],indice,color=c,s=120)
						#scatter(dicoTotal[clef][34],indice,color=cc,s=120)
						#annotate(clef[0],(dicoTotal[clef][33],indice))
						#annotate(clef[0],(dicoTotal[clef][34],indice))
						x4=x4+[dicoTotal[clef][33]]
						x4=x4+[dicoTotal[clef][34]]
		indice = indice + 1

	vector = [x1,x2,x3,x4]
	n, bins, patches = hist(vector, 20,  normed=False, histtype='bar',color=['red', 'magenta', 'green','blue'])

	plt.legend()
	plt.title('histogram of the slopes',size = 20)
	savefig('C:\\Users\\valentin\Desktop\\boulot_mines\\S3Recherche\\Python\\correlation\\histogramSans.png')



if __name__ == "__main__" :
	main()	

