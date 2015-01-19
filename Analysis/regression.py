#!/usr/bin/env python
#-*- coding: utf-8 -*-

import csv
from pylab import*
import numpy
import math
from scipy import stats
import matplotlib.pyplot as plt
import dico as d

from allTest import k, s

import matplotlib.lines as mlines


def etudePente(a) :

	noms = {0 : 'echantillon',1 : 'u',2:'v',3:'Okubo Weiss',4: 'Lyapunov exp',5 : 'SST_adv',6: 'SST_AMSRE',7 : 'grad_SST_adv',8: 'age_from_bathy',9: 'lon_from_bathy',10 : 'Shannon_Darwin_mean_all',
	11: 'Shannon_Darwin_month_all',12 :'Shannon_Darwin_mean_grp',13: 'Shannon_Darwin_month_grp',14 :'Shannon_Darwin_physat_month',15 : 'Shannon_Darwin_physat_mean',16 :'retention', 17 : 'lon_origin_45d',
	18: 'lat_origin_45d',19 :'physat_type',20 : 'abundance',21: 'richness',22 : 'Shannon',23: 'Simpson',24 :'log(alpha)',25 : 'Jevenness',26 :'S.obs',27 :'S.chao1',28 : 'se.chao1',
	29 :'S.ACE',30 :'se.ACE',31 : 'distance a la loi de puissance', 32 :'nb de pentes',33 :'pente1',34: 'pente2',35 : 'long1',36 :'long2', 37 : 'poids1', 38 : 'poids2'}

	nom = noms[a] 

	dicoTotal = d.main()

	liste1 = list()
	liste2 = list()

	for clef in dicoTotal :
		try :
			if dicoTotal[clef][32] == 1 :
				if a!=31 or dicoTotal[clef][31] !=0 :
					liste1 = liste1 + [clef]

			elif dicoTotal[clef][32] ==2 :
				if a!=31 or dicoTotal[clef][31] !=0 :
					liste2 = liste2 + [clef]
		except :
			pass

	plt.figure(figsize=(30,20))


	bool1 = True
	bool2 = True
	bool3 = True
	bool4 = True
	x=list()

	for clef in liste1 :

		if clef[1] == 5 :
			c='red'
			if bool1 :
				bool1 = False
				scatter(dicoTotal[clef][a],dicoTotal[clef][33],color=c,s=70,label='taille 0.8 a 5, queue')
				annotate(clef[0],(dicoTotal[clef][a],dicoTotal[clef][33]))
				x=x+[(dicoTotal[clef][a],dicoTotal[clef][33])]
			else : 
				scatter(dicoTotal[clef][a],dicoTotal[clef][33],color=c,s=70)
				annotate(clef[0],(dicoTotal[clef][a],dicoTotal[clef][33],))
				x=x+[(dicoTotal[clef][a],dicoTotal[clef][33])]

		if clef[1] == 20 :
			c='magenta'
			if bool2 :
				bool2 = False
				scatter(dicoTotal[clef][a],dicoTotal[clef][33],color=c,s=70,label='taille 5 a 20, queue')
				annotate(clef[0],(dicoTotal[clef][a],dicoTotal[clef][33]))
				x=x+[(dicoTotal[clef][a],dicoTotal[clef][33])]
			else : 
				scatter(dicoTotal[clef][a],dicoTotal[clef][33],color=c,s=70)
				annotate(clef[0],(dicoTotal[clef][a],dicoTotal[clef][33]))
				x=x+[(dicoTotal[clef][a],dicoTotal[clef][33])]

		if clef[1] == 180 :
			c='green'
			if bool3 :
				bool3 = False
				scatter(dicoTotal[clef][a],dicoTotal[clef][33],color=c,s=70,label='taille 20 a 180, queue')
				annotate(clef[0],(dicoTotal[clef][a],dicoTotal[clef][33]))
				x=x+[(dicoTotal[clef][a],dicoTotal[clef][33])]
			else : 
				scatter(dicoTotal[clef][a],dicoTotal[clef][33],color=c,s=70)
				annotate(clef[0],(dicoTotal[clef][a],dicoTotal[clef][33]))
				x=x+[(dicoTotal[clef][a],dicoTotal[clef][33])]

		if clef[1] == 2000 :
			c='blue'
			if bool4 :
				bool4 = False
				scatter(dicoTotal[clef][a],dicoTotal[clef][33],color=c,s=70,label='taille 180 a 2000, queue')
				annotate(clef[0],(dicoTotal[clef][a],dicoTotal[clef][33]))
				x=x+[(dicoTotal[clef][a],dicoTotal[clef][33])]
			else : 
				scatter(dicoTotal[clef][a],dicoTotal[clef][33],color=c,s=70)
				annotate(clef[0],(dicoTotal[clef][a],dicoTotal[clef][33]))
				x=x+[(dicoTotal[clef][a],dicoTotal[clef][33])]

	bool1 = True
	bool2 = True
	bool3 = True
	bool4 = True

	for clef in liste2 :

		if clef[1] == 5 :
			c='red'
			if bool1 :
				bool1 = False
				scatter(dicoTotal[clef][a],dicoTotal[clef][33],color=c,s=70,label='taille 0.8 a 5, avant derniere pente')
				scatter(dicoTotal[clef][a],dicoTotal[clef][34],color=c,s=70)
				annotate(clef[0],(dicoTotal[clef][a],dicoTotal[clef][33]))
				annotate(clef[0],(dicoTotal[clef][a],dicoTotal[clef][34]))
				x=x+[(dicoTotal[clef][a],dicoTotal[clef][33])]
				x=x+[(dicoTotal[clef][a],dicoTotal[clef][34])]
			else : 
				scatter(dicoTotal[clef][a],dicoTotal[clef][33],color=c,s=70)
				scatter(dicoTotal[clef][a],dicoTotal[clef][34],color=c,s=70)
				annotate(clef[0],(dicoTotal[clef][a],dicoTotal[clef][33]))
				annotate(clef[0],(dicoTotal[clef][a],dicoTotal[clef][34]))
				x=x+[(dicoTotal[clef][a],dicoTotal[clef][33])]
				x=x+[(dicoTotal[clef][a],dicoTotal[clef][34])]

		if clef[1] == 20 :
			c='magenta'
			if bool2 :
				bool2 = False
				scatter(dicoTotal[clef][a],dicoTotal[clef][33],color=c,s=70,label='taille 5 a 20 avant derniere pente')
				scatter(dicoTotal[clef][a],dicoTotal[clef][34],color=c,s=70)
				annotate(clef[0],(dicoTotal[clef][a],dicoTotal[clef][33]))
				annotate(clef[0],(dicoTotal[clef][a],dicoTotal[clef][34]))
				x=x+[(dicoTotal[clef][a],dicoTotal[clef][33])]
				x=x+[(dicoTotal[clef][a],dicoTotal[clef][34])]
			else : 
				scatter(dicoTotal[clef][a],dicoTotal[clef][33],color=c,s=70)
				scatter(dicoTotal[clef][a],dicoTotal[clef][34],color=c,s=70)
				annotate(clef[0],(dicoTotal[clef][a],dicoTotal[clef][33]))
				annotate(clef[0],(dicoTotal[clef][a],dicoTotal[clef][34]))
				x=x+[(dicoTotal[clef][a],dicoTotal[clef][33])]
				x=x+[(dicoTotal[clef][a],dicoTotal[clef][34])]

		if clef[1] == 180 :
			c='green'
			if bool3 :
				bool3 = False
				scatter(dicoTotal[clef][a],dicoTotal[clef][33],color=c,s=70,label='taille 20 a 180 avant derniere pente')
				scatter(dicoTotal[clef][a],dicoTotal[clef][34],color=c,s=70)
				annotate(clef[0],(dicoTotal[clef][a],dicoTotal[clef][33]))
				annotate(clef[0],(dicoTotal[clef][a],dicoTotal[clef][34]))
				x=x+[(dicoTotal[clef][a],dicoTotal[clef][33])]
				x=x+[(dicoTotal[clef][a],dicoTotal[clef][34])]
			else : 
				scatter(dicoTotal[clef][a],dicoTotal[clef][33],color=c,s=70)
				scatter(dicoTotal[clef][a],dicoTotal[clef][34],color=c,s=70)
				annotate(clef[0],(dicoTotal[clef][a],dicoTotal[clef][33]))
				annotate(clef[0],(dicoTotal[clef][a],dicoTotal[clef][34]))
				x=x+[(dicoTotal[clef][a],dicoTotal[clef][33])]
				x=x+[(dicoTotal[clef][a],dicoTotal[clef][34])]

		if clef[1] == 2000 :
			c='blue'
			if bool4 :
				bool4 = False
				scatter(dicoTotal[clef][a],dicoTotal[clef][33],color=c,s=70,label='taille 180 a 2000 avant derniere pente')
				scatter(dicoTotal[clef][a],dicoTotal[clef][34],color=c,s=70)
				annotate(clef[0],(dicoTotal[clef][a],dicoTotal[clef][33]))
				annotate(clef[0],(dicoTotal[clef][a],dicoTotal[clef][34]))
				x=x+[(dicoTotal[clef][a],dicoTotal[clef][33])]
				x=x+[(dicoTotal[clef][a],dicoTotal[clef][34])]
			else : 
				scatter(dicoTotal[clef][a],dicoTotal[clef][33],color=c,s=70)
				scatter(dicoTotal[clef][a],dicoTotal[clef][34],color=c,s=70)
				annotate(clef[0],(dicoTotal[clef][a],dicoTotal[clef][33]))
				annotate(clef[0],(dicoTotal[clef][a],dicoTotal[clef][34]))
				x=x+[(dicoTotal[clef][a],dicoTotal[clef][33])]
				x=x+[(dicoTotal[clef][a],dicoTotal[clef][34])]

	coef1,coef2, r, p, m, M, mx = correl(x)


	y1=linspace(m,M,30)
	plt.plot(y1,coef1*(y1-mx)+coef2, label='a={}, b={}, r={}, p={}'.format(coef1,coef2,r,p))

	plt.legend()
	plt.title('pentes en fonction de {}'.format(nom),fontsize=40)
	plt.xlabel("{}".format(nom), fontsize=40)
	plt.ylabel("slope", fontsize=40)
	yticks(fontsize=40)
	xticks(fontsize=40)
	plt.title('slope versus {}'.format(nom),fontsize=40)
	savefig('C:\\Users\\valentin\Desktop\\boulot_mines\\S3Recherche\\Python\\correlation\\regressionPentesF{}.png'.format(nom))

def etudePente(a) :

	noms = {0 : 'echantillon',1 : 'u',2:'v',3:'Okubo Weiss',4: 'Lyapunov exp',5 : 'SST_adv',6: 'SST_AMSRE',7 : 'grad_SST_adv',8: 'age_from_bathy',9: 'lon_from_bathy',10 : 'Shannon_Darwin_mean_all',
	11: 'Shannon_Darwin_month_all',12 :'Shannon_Darwin_mean_grp',13: 'Shannon_Darwin_month_grp',14 :'Shannon_Darwin_physat_month',15 : 'Shannon_Darwin_physat_mean',16 :'retention', 17 : 'lon_origin_45d',
	18: 'lat_origin_45d',19 :'physat_type',20 : 'abundance',21: 'richness',22 : 'Shannon',23: 'Simpson',24 :'log(alpha)',25 : 'Jevenness',26 :'S.obs',27 :'S.chao1',28 : 'se.chao1',
	29 :'S.ACE',30 :'se.ACE',31 : 'distance a la loi de puissance', 32 :'nb de pentes',33 :'pente1',34: 'pente2',35 : 'long1',36 :'long2', 37 : 'poids1', 38 : 'poids2'}

	nom = noms[a] 

	dicoTotal = d.main()

	liste1 = list()
	liste2 = list()

	for clef in dicoTotal :
		try :
			if dicoTotal[clef][32] == 1 :
				if a!=31 or dicoTotal[clef][31] !=0 :
					liste1 = liste1 + [clef]

			elif dicoTotal[clef][32] ==2 :
				if a!=31 or dicoTotal[clef][31] !=0 :
					liste2 = liste2 + [clef]
		except :
			pass

	plt.figure(figsize=(30,20))


	bool1 = True
	bool2 = True
	bool3 = True
	bool4 = True
	x=list()

	for clef in liste1 :

		if clef[1] == 5 :
			c='red'
			if bool1 :
				bool1 = False
				scatter(dicoTotal[clef][a],dicoTotal[clef][33],color=c,s=70,label='taille 0.8 a 5, queue')
				annotate(clef[0],(dicoTotal[clef][a],dicoTotal[clef][33]))
				x=x+[(dicoTotal[clef][a],dicoTotal[clef][33])]
			else : 
				scatter(dicoTotal[clef][a],dicoTotal[clef][33],color=c,s=70)
				annotate(clef[0],(dicoTotal[clef][a],dicoTotal[clef][33],))
				x=x+[(dicoTotal[clef][a],dicoTotal[clef][33])]

		if clef[1] == 20 :
			c='magenta'
			if bool2 :
				bool2 = False
				scatter(dicoTotal[clef][a],dicoTotal[clef][33],color=c,s=70,label='taille 5 a 20, queue')
				annotate(clef[0],(dicoTotal[clef][a],dicoTotal[clef][33]))
				x=x+[(dicoTotal[clef][a],dicoTotal[clef][33])]
			else : 
				scatter(dicoTotal[clef][a],dicoTotal[clef][33],color=c,s=70)
				annotate(clef[0],(dicoTotal[clef][a],dicoTotal[clef][33]))
				x=x+[(dicoTotal[clef][a],dicoTotal[clef][33])]

		if clef[1] == 180 :
			c='green'
			if bool3 :
				bool3 = False
				scatter(dicoTotal[clef][a],dicoTotal[clef][33],color=c,s=70,label='taille 20 a 180, queue')
				annotate(clef[0],(dicoTotal[clef][a],dicoTotal[clef][33]))
				x=x+[(dicoTotal[clef][a],dicoTotal[clef][33])]
			else : 
				scatter(dicoTotal[clef][a],dicoTotal[clef][33],color=c,s=70)
				annotate(clef[0],(dicoTotal[clef][a],dicoTotal[clef][33]))
				x=x+[(dicoTotal[clef][a],dicoTotal[clef][33])]

		if clef[1] == 2000 :
			c='blue'
			if bool4 :
				bool4 = False
				scatter(dicoTotal[clef][a],dicoTotal[clef][33],color=c,s=70,label='taille 180 a 2000, queue')
				annotate(clef[0],(dicoTotal[clef][a],dicoTotal[clef][33]))
				x=x+[(dicoTotal[clef][a],dicoTotal[clef][33])]
			else : 
				scatter(dicoTotal[clef][a],dicoTotal[clef][33],color=c,s=70)
				annotate(clef[0],(dicoTotal[clef][a],dicoTotal[clef][33]))
				x=x+[(dicoTotal[clef][a],dicoTotal[clef][33])]

	bool1 = True
	bool2 = True
	bool3 = True
	bool4 = True

	for clef in liste2 :

		if clef[1] == 5 :
			c='red'
			if bool1 :
				bool1 = False
				scatter(dicoTotal[clef][a],dicoTotal[clef][33],color=c,s=70,label='taille 0.8 a 5, avant derniere pente')
				scatter(dicoTotal[clef][a],dicoTotal[clef][34],color=c,s=70)
				annotate(clef[0],(dicoTotal[clef][a],dicoTotal[clef][33]))
				annotate(clef[0],(dicoTotal[clef][a],dicoTotal[clef][34]))
				x=x+[(dicoTotal[clef][a],dicoTotal[clef][33])]
				x=x+[(dicoTotal[clef][a],dicoTotal[clef][34])]
			else : 
				scatter(dicoTotal[clef][a],dicoTotal[clef][33],color=c,s=70)
				scatter(dicoTotal[clef][a],dicoTotal[clef][34],color=c,s=70)
				annotate(clef[0],(dicoTotal[clef][a],dicoTotal[clef][33]))
				annotate(clef[0],(dicoTotal[clef][a],dicoTotal[clef][34]))
				x=x+[(dicoTotal[clef][a],dicoTotal[clef][33])]
				x=x+[(dicoTotal[clef][a],dicoTotal[clef][34])]

		if clef[1] == 20 :
			c='magenta'
			if bool2 :
				bool2 = False
				scatter(dicoTotal[clef][a],dicoTotal[clef][33],color=c,s=70,label='taille 5 a 20 avant derniere pente')
				scatter(dicoTotal[clef][a],dicoTotal[clef][34],color=c,s=70)
				annotate(clef[0],(dicoTotal[clef][a],dicoTotal[clef][33]))
				annotate(clef[0],(dicoTotal[clef][a],dicoTotal[clef][34]))
				x=x+[(dicoTotal[clef][a],dicoTotal[clef][33])]
				x=x+[(dicoTotal[clef][a],dicoTotal[clef][34])]
			else : 
				scatter(dicoTotal[clef][a],dicoTotal[clef][33],color=c,s=70)
				scatter(dicoTotal[clef][a],dicoTotal[clef][34],color=c,s=70)
				annotate(clef[0],(dicoTotal[clef][a],dicoTotal[clef][33]))
				annotate(clef[0],(dicoTotal[clef][a],dicoTotal[clef][34]))
				x=x+[(dicoTotal[clef][a],dicoTotal[clef][33])]
				x=x+[(dicoTotal[clef][a],dicoTotal[clef][34])]

		if clef[1] == 180 :
			c='green'
			if bool3 :
				bool3 = False
				scatter(dicoTotal[clef][a],dicoTotal[clef][33],color=c,s=70,label='taille 20 a 180 avant derniere pente')
				scatter(dicoTotal[clef][a],dicoTotal[clef][34],color=c,s=70)
				annotate(clef[0],(dicoTotal[clef][a],dicoTotal[clef][33]))
				annotate(clef[0],(dicoTotal[clef][a],dicoTotal[clef][34]))
				x=x+[(dicoTotal[clef][a],dicoTotal[clef][33])]
				x=x+[(dicoTotal[clef][a],dicoTotal[clef][34])]
			else : 
				scatter(dicoTotal[clef][a],dicoTotal[clef][33],color=c,s=70)
				scatter(dicoTotal[clef][a],dicoTotal[clef][34],color=c,s=70)
				annotate(clef[0],(dicoTotal[clef][a],dicoTotal[clef][33]))
				annotate(clef[0],(dicoTotal[clef][a],dicoTotal[clef][34]))
				x=x+[(dicoTotal[clef][a],dicoTotal[clef][33])]
				x=x+[(dicoTotal[clef][a],dicoTotal[clef][34])]

		if clef[1] == 2000 :
			c='blue'
			if bool4 :
				bool4 = False
				scatter(dicoTotal[clef][a],dicoTotal[clef][33],color=c,s=70,label='taille 180 a 2000 avant derniere pente')
				scatter(dicoTotal[clef][a],dicoTotal[clef][34],color=c,s=70)
				annotate(clef[0],(dicoTotal[clef][a],dicoTotal[clef][33]))
				annotate(clef[0],(dicoTotal[clef][a],dicoTotal[clef][34]))
				x=x+[(dicoTotal[clef][a],dicoTotal[clef][33])]
				x=x+[(dicoTotal[clef][a],dicoTotal[clef][34])]
			else : 
				scatter(dicoTotal[clef][a],dicoTotal[clef][33],color=c,s=70)
				scatter(dicoTotal[clef][a],dicoTotal[clef][34],color=c,s=70)
				annotate(clef[0],(dicoTotal[clef][a],dicoTotal[clef][33]))
				annotate(clef[0],(dicoTotal[clef][a],dicoTotal[clef][34]))
				x=x+[(dicoTotal[clef][a],dicoTotal[clef][33])]
				x=x+[(dicoTotal[clef][a],dicoTotal[clef][34])]


	coef1,coef2, r, p, m, M, mx = correl(x)

	if str(coef1) != 'nan' :

		y1=linspace(m,M,30)
		plt.plot(y1,coef1*(y1-mx)+coef2, label='a={}, b={}, r={}, p={}'.format(coef1,coef2,r,p))

		axe1 =list()
		axe2 = list()

		for dot in x : 
			axe1 = axe1 + [dot[0]]
			axe2 = axe2 + [dot[1]]

		slope,intercept,rReg,pReg,error = stats.linregress(axe1,axe2)
		if str(slope) != 'nan' :
			plt.title('pentes en fonction de {} ResPython'.format(nom),fontsize=40)
		else : 
			plt.title('pentes en fonction de {} ResPython'.format(nom),fontsize=40)
	else : 
		plt.title('pentes en fonction de {} ResPython'.format(nom),fontsize=40)
	plt.legend()


	plt.xlabel("{}".format(nom), fontsize=40)
	plt.ylabel("slope", fontsize=40)
	yticks(fontsize=40)
	xticks(fontsize=40)
	savefig('C:\\Users\\valentin\Desktop\\boulot_mines\\S3Recherche\\Python\\correlation\\regressionPentesF{}.png'.format(nom))

def etudePentes() :

	indice = 3
	while indice < 32 :
		etudePente(indice)
		indice = indice + 1
		

def etudePentesSans() :

	indice = 3
	while indice < 32 :
		etudePenteSans(indice)
		indice = indice + 1


def correl(listePoints):
	print(listePoints)

	sx=0
	mx=0
	my=0
	sy=0
	r=0
	p=0
	m=0
	M=-100
	indice = 0

	for dot in listePoints :

		if str(dot[0]) != 'nan' :

			my = my + dot[1]
			mx = mx + dot[0]

			if dot[0]<m :
				m=dot[0]

			if dot[0]>M :
				M=dot[0]

			indice +=1


	my= my/indice
	mx=mx/indice

	for dot in listePoints :

		if str(dot[0]) != 'nan' :		

			sy = sy + (dot[1]-my)**2
			sx = sx + (dot[0]-mx)**2

	sy = math.sqrt(sy/indice)
	sx = math.sqrt(sx/indice)

	b=my
	i=0
	j=0
	k=0

	for dot in listePoints :

		if str(dot[0]) != 'nan' :

			i = i + dot[0]*dot[1]
			j = j + dot[0]**2
			k = k + dot[1]**2

	r = (indice*i-(indice**2)*mx*my)/math.sqrt((indice*j-(indice*mx)**2)*(indice*k-(indice*my)**2))

	a = r*sy/sx

	i=0
	j=0

	for dot in listePoints :

		if str(dot[0]) != 'nan' :

			i += (dot[1]-my)**2
			j += (dot[1]-a*(dot[0]-mx)-b)**2

	p = (indice-2)*i/j

	return(a,b,r,p,m,M,mx)

def etudePenteSans(a) :

	noms = {0 : 'echantillon',1 : 'u',2:'v',3:'Okubo Weiss',4: 'Lyapunov exp',5 : 'SST_adv',6: 'SST_AMSRE',7 : 'grad_SST_adv',8: 'age_from_bathy',9: 'lon_from_bathy',10 : 'Shannon_Darwin_mean_all',
	11: 'Shannon_Darwin_month_all',12 :'Shannon_Darwin_mean_grp',13: 'Shannon_Darwin_month_grp',14 :'Shannon_Darwin_physat_month',15 : 'Shannon_Darwin_physat_mean',16 :'retention', 17 : 'lon_origin_45d',
	18: 'lat_origin_45d',19 :'physat_type',20 : 'abundance',21: 'richness',22 : 'Shannon',23: 'Simpson',24 :'log(alpha)',25 : 'Jevenness',26 :'S.obs',27 :'S.chao1',28 : 'se.chao1',
	29 :'S.ACE',30 :'se.ACE',31 : 'distance a la loi de puissance', 32 :'nb de pentes',33 :'pente1',34: 'pente2',35 : 'long1',36 :'long2', 37 : 'poids1', 38 : 'poids2'}

	nom = noms[a] 

	dicoTotal = d.effacer(s)

	liste1 = list()
	liste2 = list()

	for clef in dicoTotal :
		try :
			if dicoTotal[clef][32] == 1 and clef[1] != 5:
				if a!=31 or dicoTotal[clef][31] !=0 :
					liste1 = liste1 + [clef]

			elif dicoTotal[clef][32] ==2 and clef[1] != 5:
				if a!=31 or dicoTotal[clef][31] !=0 :
					liste2 = liste2 + [clef]
		except :
			pass

	plt.figure(figsize=(30,20))


	bool1 = True
	bool2 = True
	bool3 = True
	bool4 = True
	x=list()

	for clef in liste1 :

		if clef[1] == 5 :
			c='red'
			if bool1 :
				bool1 = False
				scatter(dicoTotal[clef][a],dicoTotal[clef][33],color=c,s=70,label='taille 0.8 a 5, queue')
				annotate(clef[0],(dicoTotal[clef][a],dicoTotal[clef][33]))
				x=x+[(dicoTotal[clef][a],dicoTotal[clef][33])]
			else : 
				scatter(dicoTotal[clef][a],dicoTotal[clef][33],color=c,s=70)
				annotate(clef[0],(dicoTotal[clef][a],dicoTotal[clef][33],))
				x=x+[(dicoTotal[clef][a],dicoTotal[clef][33])]

		if clef[1] == 20 :
			c='magenta'
			if bool2 :
				bool2 = False
				scatter(dicoTotal[clef][a],dicoTotal[clef][33],color=c,s=70,label='taille 5 a 20, queue')
				annotate(clef[0],(dicoTotal[clef][a],dicoTotal[clef][33]))
				x=x+[(dicoTotal[clef][a],dicoTotal[clef][33])]
			else : 
				scatter(dicoTotal[clef][a],dicoTotal[clef][33],color=c,s=70)
				annotate(clef[0],(dicoTotal[clef][a],dicoTotal[clef][33]))
				x=x+[(dicoTotal[clef][a],dicoTotal[clef][33])]

		if clef[1] == 180 :
			c='green'
			if bool3 :
				bool3 = False
				scatter(dicoTotal[clef][a],dicoTotal[clef][33],color=c,s=70,label='taille 20 a 180, queue')
				annotate(clef[0],(dicoTotal[clef][a],dicoTotal[clef][33]))
				x=x+[(dicoTotal[clef][a],dicoTotal[clef][33])]
			else : 
				scatter(dicoTotal[clef][a],dicoTotal[clef][33],color=c,s=70)
				annotate(clef[0],(dicoTotal[clef][a],dicoTotal[clef][33]))
				x=x+[(dicoTotal[clef][a],dicoTotal[clef][33])]

		if clef[1] == 2000 :
			c='blue'
			if bool4 :
				bool4 = False
				scatter(dicoTotal[clef][a],dicoTotal[clef][33],color=c,s=70,label='taille 180 a 2000, queue')
				annotate(clef[0],(dicoTotal[clef][a],dicoTotal[clef][33]))
				x=x+[(dicoTotal[clef][a],dicoTotal[clef][33])]
			else : 
				scatter(dicoTotal[clef][a],dicoTotal[clef][33],color=c,s=70)
				annotate(clef[0],(dicoTotal[clef][a],dicoTotal[clef][33]))
				x=x+[(dicoTotal[clef][a],dicoTotal[clef][33])]

	bool1 = True
	bool2 = True
	bool3 = True
	bool4 = True

	for clef in liste2 :

		if clef[1] == 5 :
			c='red'
			if bool1 :
				bool1 = False
				scatter(dicoTotal[clef][a],dicoTotal[clef][33],color=c,s=70,label='taille 0.8 a 5, avant derniere pente')
				scatter(dicoTotal[clef][a],dicoTotal[clef][34],color=c,s=70)
				annotate(clef[0],(dicoTotal[clef][a],dicoTotal[clef][33]))
				annotate(clef[0],(dicoTotal[clef][a],dicoTotal[clef][34]))
				x=x+[(dicoTotal[clef][a],dicoTotal[clef][33])]
				x=x+[(dicoTotal[clef][a],dicoTotal[clef][34])]
			else : 
				scatter(dicoTotal[clef][a],dicoTotal[clef][33],color=c,s=70)
				scatter(dicoTotal[clef][a],dicoTotal[clef][34],color=c,s=70)
				annotate(clef[0],(dicoTotal[clef][a],dicoTotal[clef][33]))
				annotate(clef[0],(dicoTotal[clef][a],dicoTotal[clef][34]))
				x=x+[(dicoTotal[clef][a],dicoTotal[clef][33])]
				x=x+[(dicoTotal[clef][a],dicoTotal[clef][34])]

		if clef[1] == 20 :
			c='magenta'
			if bool2 :
				bool2 = False
				scatter(dicoTotal[clef][a],dicoTotal[clef][33],color=c,s=70,label='taille 5 a 20 avant derniere pente')
				scatter(dicoTotal[clef][a],dicoTotal[clef][34],color=c,s=70)
				annotate(clef[0],(dicoTotal[clef][a],dicoTotal[clef][33]))
				annotate(clef[0],(dicoTotal[clef][a],dicoTotal[clef][34]))
				x=x+[(dicoTotal[clef][a],dicoTotal[clef][33])]
				x=x+[(dicoTotal[clef][a],dicoTotal[clef][34])]
			else : 
				scatter(dicoTotal[clef][a],dicoTotal[clef][33],color=c,s=70)
				scatter(dicoTotal[clef][a],dicoTotal[clef][34],color=c,s=70)
				annotate(clef[0],(dicoTotal[clef][a],dicoTotal[clef][33]))
				annotate(clef[0],(dicoTotal[clef][a],dicoTotal[clef][34]))
				x=x+[(dicoTotal[clef][a],dicoTotal[clef][33])]
				x=x+[(dicoTotal[clef][a],dicoTotal[clef][34])]

		if clef[1] == 180 :
			c='green'
			if bool3 :
				bool3 = False
				scatter(dicoTotal[clef][a],dicoTotal[clef][33],color=c,s=70,label='taille 20 a 180 avant derniere pente')
				scatter(dicoTotal[clef][a],dicoTotal[clef][34],color=c,s=70)
				annotate(clef[0],(dicoTotal[clef][a],dicoTotal[clef][33]))
				annotate(clef[0],(dicoTotal[clef][a],dicoTotal[clef][34]))
				x=x+[(dicoTotal[clef][a],dicoTotal[clef][33])]
				x=x+[(dicoTotal[clef][a],dicoTotal[clef][34])]
			else : 
				scatter(dicoTotal[clef][a],dicoTotal[clef][33],color=c,s=70)
				scatter(dicoTotal[clef][a],dicoTotal[clef][34],color=c,s=70)
				annotate(clef[0],(dicoTotal[clef][a],dicoTotal[clef][33]))
				annotate(clef[0],(dicoTotal[clef][a],dicoTotal[clef][34]))
				x=x+[(dicoTotal[clef][a],dicoTotal[clef][33])]
				x=x+[(dicoTotal[clef][a],dicoTotal[clef][34])]

		if clef[1] == 2000 :
			c='blue'
			if bool4 :
				bool4 = False
				scatter(dicoTotal[clef][a],dicoTotal[clef][33],color=c,s=70,label='taille 180 a 2000 avant derniere pente')
				scatter(dicoTotal[clef][a],dicoTotal[clef][34],color=c,s=70)
				annotate(clef[0],(dicoTotal[clef][a],dicoTotal[clef][33]))
				annotate(clef[0],(dicoTotal[clef][a],dicoTotal[clef][34]))
				x=x+[(dicoTotal[clef][a],dicoTotal[clef][33])]
				x=x+[(dicoTotal[clef][a],dicoTotal[clef][34])]
			else : 
				scatter(dicoTotal[clef][a],dicoTotal[clef][33],color=c,s=70)
				scatter(dicoTotal[clef][a],dicoTotal[clef][34],color=c,s=70)
				annotate(clef[0],(dicoTotal[clef][a],dicoTotal[clef][33]))
				annotate(clef[0],(dicoTotal[clef][a],dicoTotal[clef][34]))
				x=x+[(dicoTotal[clef][a],dicoTotal[clef][33])]
				x=x+[(dicoTotal[clef][a],dicoTotal[clef][34])]

	coef1,coef2, r, p, m, M, mx = correl(x)

	if str(coef1) != 'nan' :

		y1=linspace(m,M,30)
		plt.plot(y1,coef1*(y1-mx)+coef2, label='a={}, b={}, r={}, p={}'.format(coef1,coef2,r,p))

		axe1 =list()
		axe2 = list()

		for dot in x : 
			axe1 = axe1 + [dot[0]]
			axe2 = axe2 + [dot[1]]

		slope,intercept,rReg,pReg,error = stats.linregress(axe1,axe2)
		if str(slope) != 'nan' :
			plt.title('pentes en fonction de {} ResPython : {},{},{},{},{}'.format(nom,slope,intercept,rReg,pReg,error),fontsize=40)
		else : 
			plt.title('pentes en fonction de {} ResPython'.format(nom),fontsize=40)
	else : 
		plt.title('pentes en fonction de {} ResPython'.format(nom),fontsize=40)

	plt.legend()


	plt.xlabel("{}".format(nom), fontsize=40)
	plt.ylabel("slope", fontsize=40)
	yticks(fontsize=40)
	xticks(fontsize=40)
	savefig('C:\\Users\\valentin\Desktop\\boulot_mines\\S3Recherche\\Python\\correlation\\regressionSansPetitesPentesF{}.png'.format(nom))



if __name__ == "__main__" :
	etudePentes()	

