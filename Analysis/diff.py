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
	ext_possible = ['.5','.20','.180','.2000'] #Les extensinos possibles
	nod= ['data({})'.format(x) for x in range(79)] #Les noms possibles
	noms_possibles=list() #Le mix des deux
	noms_existant=list() #Ceux qui existent
	diametre=list() #Les tailles de plancton correspondantes



	for nom in nod :
		for ext in ext_possible :
			noms_possibles = noms_possibles + [nom+ext] #On construit les noms possibles

	for nom in noms_possibles:
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
	abondancesMoyennes = list()

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
		while k<100: #On fait 100 bins
			
			if j<taille+1:
				indice=0
				while indice<(Decimal(10**(log_taille*Decimal(k+1)/100))-Decimal(10**(log_taille*Decimal(k)/100))): #tant qu'on est sur le bon bin
					if j+indice<taille: 
						abondances[k]=abondances[k]+Decimal(math.log10(data[j+indice])) #on somme les abondances
						rang[k]=rang[k]+math.log10(j+indice+1) #les rangs en echelle log
						tailleBin[k]=tailleBin[k]+1 #on augmente la taille du bin
						indice=indice+1
					else :
						indice=indice+1
	

			rang[k]=rang[k]/indice #idem sur les rangs
			abondances[k]=float(Decimal(abondances[k])/Decimal(indice)) #On moyennise
			j=j+indice

			tailleBin[k]=float(Decimal(tailleBin[k])/Decimal(taille)) #et on normalise la taille des bins
			k=k+1

		indice=0
		rangMiddle = rang[90]
		abondancesMiddle = abondances[90]
		abondanceMoyenne = 0
		"""#Version Soustraction
		for x in abondances:
			if indice <100 :
				#scatter(rang[indice],abondances[indice],color='red')
				#scatter(rang[indice],((1.27)*(rangMiddle-rang[indice])+abondancesMiddle),color='green')
				#scatter(rang[indice],abondances[indice]- ((1.27)*(rangMiddle-rang[indice])+abondancesMiddle))
				abondances[indice] = abondances[indice]- ((1.27)*(rangMiddle-rang[indice])+abondancesMiddle)
				abondanceMoyenne = abondanceMoyenne + abondances[indice]
				indice = indice+1"""

		#Version Division
		for x in abondances:
			if indice <100 :
				#scatter(rang[indice],abondances[indice],color='red')
				#scatter(rang[indice],((1.27)*(rangMiddle-rang[indice])+abondancesMiddle),color='green')
				#scatter(rang[indice],abondances[indice]/ ((1.27)*(rangMiddle-rang[indice])+abondancesMiddle))
				abondances[indice] = abondances[indice]/((1.27)*(rangMiddle-rang[indice])+abondancesMiddle)
				abondanceMoyenne = abondanceMoyenne + abondances[indice]
				indice = indice+1

		abondanceMoyenne = abondanceMoyenne / indice
		indice=0

		#show()
		gc.collect()
		
		indice=0
		with open('C:\\Users\\valentin\Desktop\\boulot_mines\\S3Recherche\\BDD\\ProtistTV9subtabs293\\analyse\\station_{}_binne.csv'.format(nom), 'wb') as csvfile:
		    writer = csv.writer(csvfile, delimiter=',',quotechar='|', quoting=csv.QUOTE_MINIMAL)
		    for dot in rang :
		    	writer.writerow("{0};{1};{2};".format(abondances[indice],dot,tailleBin[indice]))
		    	indice=indice+1 #On ecrit le tout dans un csv

		print('ecriture terminee')
		print(abondanceMoyenne)
		indice=1
		while indice<100 :
			if abondances[indice]==0 :
				break
			indice=indice+1 #On enleve les zeros parasites

		abondances=abondances[0:indice] #Dans tous les jeux de donnees
		rang = rang[0:indice]
		tailleBin = tailleBin[0:indice]


		gc.collect()
		log1=log1 +[abondances] #On recupere les listes classees dans le meme ordre que les noms
		taille1=taille1 + [tailleBin]
		rang1=rang1+[rang]
		gc.collect()
		abondancesMoyennes = abondancesMoyennes + [abondanceMoyenne]


	return log1,taille1,rang1,stationNoms,abondancesMoyennes



def analyse_data (log_abondances, tailles, nod,k,rang,sN,dictionnaire) :

	from pylab import* #Pour le trace
	import matplotlib.pyplot as plt
	liste_ok=list() #Liste de 0,1 ou 2 en fonction du nombre de pentes a priori exploitables
	liste_pentes=list() #Les pentes en question (contient aussi les ordonnees a l'origine, a trier !)
	from algo_diff import * #L'algorithme de decoupage
	from algo_diff import optimisation_decoupage
	indice = -1
	sN2=list()
	longueurs = list()
	poids = list()

	for  nom in nod :
		j=0

		gc.collect() #on nettoie 
		indice = indice +1
		gc.collect()
		try : 
			del solution
		except NameError :
			pass
		try : 
			del pentes
		except NameError :
			pass
		try : 
			del ok
		except NameError :
			pass
		gc.collect()
		#solution,pentes,ok = optimisation_decoupage(log_abondances[indice],k,tailles[indice],nom,rang[indice]) #On recupere les resultats du decoupage
		solution,pentes,ok,p,tR,sN1,longueurAvant,longueur,poidsDesPentesAvant,poidsDesPentes = optimisation_decoupage(log_abondances[indice],k,tailles[indice],nom,rang[indice],sN[indice],dictionnaire) #On recupere les resultats du decoupage
		#liste_ok=liste_ok+[ok] #On elargit la liste des points valables
		liste_ok=liste_ok+[tR] #On elargit la liste des points valables
		pentes=pentes+[0,0]
		longueurAvant = longueurAvant + [0]
		poidsDesPentesAvant = poidsDesPentesAvant + [0]


		with open('C:\\Users\\valentin\Desktop\\boulot_mines\\S3Recherche\\BDD\\ProtistTV9subtabs293\\analyse\\{}_st{}_{}_{}.csv'.format(k,dictionnaire[sN1[0]][0],dictionnaire[sN1[0]][1],nom), 'wb') as csvfile:
			writer = csv.writer(csvfile, delimiter=',',quotechar='|', quoting=csv.QUOTE_MINIMAL)
			for dot in solution :
				writer.writerow("{0};{1};{2};{3}".format(dot,pentes[j*2],pentes[j*2+1],longueurAvant[j],poidsDesPentesAvant[j]))
				j=j+1

		liste_pentes=liste_pentes+[p] #On enregistre
		sN2 = sN2 + sN1
		longueurs = longueurs + [longueur]
		poids = poids + [poidsDesPentes]
		gc.collect()
		clf()
		
	return(liste_pentes,liste_ok,sN2,longueurs,poids) #et on retourne le resultat


def lancement(k) : 
	from pylab import* #Pour le trace
	import matplotlib.pyplot as plt

	dictionnaire = corres() #On recupère la correspondance entre les noms des echantillons et les stations

	noms, diametre = lecture_noms() #les resultats de la lecture des noms de fichiers : les noms a ouvrir et les tailles de plancton correspondantes

	log_abondances, tailles,rang,stationNoms,abondanceMoyenne = binning(noms,k) #On recupere le binning

	sNoms=stationNoms
	del stationNoms

	pentes,ok,stationNoms,longueurs,poids=analyse_data(log_abondances,tailles, noms, k, rang,sNoms,dictionnaire) #Puis les resultats de l'analyse

	indice=0

	with open('C:\\Users\\valentin\Desktop\\boulot_mines\\S3Recherche\\BDD\\ProtistTV9subtabs293\\analyse\\ecartPowerLaw_{}.csv'.format(k), 'wb') as csvfile:
			writer = csv.writer(csvfile, delimiter=' ',quotechar=',', quoting=csv.QUOTE_MINIMAL)
			for diff in abondanceMoyenne :
				writer.writerow("{0};{1}".format(dictionnaire[stationNoms[indice]][0],diff))
				indice = indice + 1



	pointsGraph=stationNoms

	pentes,ok,stationNoms,diametre,longueurs,poids = traitement(pentes,ok,stationNoms,dictionnaire,diametre,longueurs,poids) #On fait le trie dans les echantillons

	indice=-1
	indiceNom = 0
	graph_pentes1=list() #On va tracer differents graphes : 3 pour les courbes a une seule pente
	graph_pentes2=list() #2 pour les dernieres pentes quand il y en a plus
	graph_pentes3=list() #1 pour les avant dernières pentes
	diam1=list() #Les tailles correspondantes pour faire une etude discriminante
	diam2=list()
	diam3=list()
	bool1=list() #La qualite des points
	bool2=list()
	bool3=list()
	j=0
	station1=list()
	stationbis1=list()
	station2=list()
	stationbis2=list()
	station3=list()
	stationbis3=list()
	allstations=list()
	valfinale=0
	nbfinal = 0
	pPP = 0
	lPP = 0
	pSP = 0
	lSP = 0
	for listeRes in pentes :
		for x in listeRes :
			if x!=0 :
				nbfinal = nbfinal+1
				valfinale = valfinale+x

	with open('C:\\Users\\valentin\Desktop\\boulot_mines\\S3Recherche\\BDD\\ProtistTV9subtabs293\\analyse\\pentes_{}.csv'.format(k), 'wb') as csvfile:
			writer = csv.writer(csvfile, delimiter=',',quotechar='|', quoting=csv.QUOTE_MINIMAL)
			for dot in pentes :
				indice=indice+1
				if ok[indice]==1 :
					writer.writerow("{0};null;{1};{2};{3};{4};{5}".format(stationNoms[indiceNom],dot[0], 1,diametre[j],longueurs[j][0],poids[j][0]))
					if dot[0] !=0 :
						graph_pentes3=graph_pentes3+[dot[0]]
						diam3=diam3+[diametre[j]]
						bool3=bool3+[True]
						station3=station3+[stationNoms[indiceNom]]
						lPP = lPP+1
						pPP = pPP + dot[0]
					
				elif ok[indice]==2  :
					writer.writerow("{0};{1};{2};{3};{4};{5};{6};{7};{8}".format(stationNoms[indiceNom],dot[0], dot[1],2,diametre[j],longueurs[j][0],longueurs[j][1],poids[j][0],poids[j][1]))
					if dot[1] !=0 :
						graph_pentes2=graph_pentes2+[dot[1]]
						diam2=diam2+[diametre[j]]
						bool2=bool2+[True]
						station2=station2+[stationNoms[indiceNom]]
						lPP = lPP+1
						pPP = pPP + dot[1]
					if dot[0] !=0 :
						graph_pentes1=graph_pentes1+[dot[0]]
						diam1=diam1+[diametre[j]]
						bool1=bool1+[True]
						station1=station1+[stationNoms[indiceNom]]
						lSP = lSP+1
						pSP = pSP + dot[0]

				elif ok[indice]== 3:
					writer.writerow("{0};{1};{2};{3};{4};{5};{6};{7};{8}".format(stationNoms[indiceNom],dot[1], dot[2], 2,diametre[j],longueurs[j][0],longueurs[j][1],poids[j][0],poids[j][1]))
					if dot[1]!=0:
						graph_pentes1=graph_pentes1+[dot[1]]
						diam1=diam1+[diametre[j]]
						bool1=bool1+[True]
						station1=station1+[stationNoms[indiceNom]]
						lSP = lSP+1
						pSP = pSP + dot[1]
					if dot[2]!=0:
						graph_pentes2=graph_pentes2+[dot[2]]
						diam2=diam2+[diametre[j]]
						bool2=bool2+[True]
						station2=station2+[stationNoms[indiceNom]]
						lPP = lPP+1
						pPP = pPP + dot[2]

				elif ok[indice]>3 :
					writer.writerow("{0};{1};{2};{3};{4};{5};{6};{7};{8}".format(stationNoms[indiceNom],dot[ok[indice]-1], dot[ok[indice]-2], 0,diametre[j],longueurs[j][0],longueurs[j][1],poids[j][0],poids[j][1]))
					if dot[ok[indice]-2]!=0:
						graph_pentes2=graph_pentes2+[dot[ok[indice]-2]]
						diam2=diam2+[diametre[j]]
						bool2=bool2+[False]
						station2=station2+[stationNoms[indiceNom]]
						lSP = lSP+1
						pSP = pSP + dot[ok[indice]-2]
					if dot[ok[indice]-1]!=0:
						graph_pentes1=graph_pentes1+[dot[ok[indice]-1]]
						diam1=diam1+[diametre[j]]
						bool1=bool1+[False]
						station1=station1+[stationNoms[indiceNom]]
						lPP = lPP+1
						pPP = pPP + dot[ok[indice]-1]
				j=j+1
				indiceNom=indiceNom+len(dot)


	#Debut modifications

	liste_stations=[4,7,9,11,16,18,20,22,23,24,25,26,30,31,32,33,34,36,38,41,42,45,48,52,64,65,66,67,68,70,72,76,78,82,84,85,98,100,102,109,111,122,123,124,125]


	pentes1=list()
	pentes2=list()
	pentes3=list()
	diametre1=list()
	diametre2=list()
	diametre3=list()
	stat1=list()
	stat2=list()
	stat3=list()

	for num in liste_stations :
		indice=0

		for p in graph_pentes1 :

			if station1[indice]==num :
				stat1=stat1+[num]
				pentes1=pentes1+[p]
				diametre1 = diametre1+[diam1[indice]]
			indice=indice+1

	for num in liste_stations :
		indice=0

		for p in graph_pentes2 :

			if station1[indice]==num :
				stat2=stat2+[num]
				pentes2=pentes2+[p]
				diametre2 = diametre2+[diam2[indice]]
			indice=indice+1

	
	for num in liste_stations :
		indice=0

		for p in graph_pentes3 :

			if station3[indice]==num :
				stat3=stat3+[num]
				pentes3=pentes3+[p]
				diametre3 = diametre3+[diam3[indice]]
			indice=indice+1

	
	noms1 = list() #Les stations qui sont présentes dans la liste 1
	noms2 = list()
	noms3 = list()

	statPrec = ''
	for n in stat1 :
		if statPrec == n :
			pass
		else :
			noms1 = noms1 + [n]
			statPrec=n

	statPrec = ''
	for n in stat2 :
		if statPrec == n :
			pass
		else :
			noms2 = noms2 + [n]
			statPrec=n

	statPrec = ''
	for n in stat3 :
		if statPrec == n :
			pass
		else :
			noms3 = noms3 + [n]
			statPrec=n


	del(graph_pentes3)
	del(graph_pentes1)
	del(graph_pentes2)
	del(bool3)
	del(bool1)
	del(bool2)
	del(diam1)
	del(diam2)
	del(diam3)
	del(station3)
	del(station1)
	del(station2)



	bool1 = True
	bool2 = True
	bool3 = True
	bool4 = True

	#On trace les graphes des differents types de pentes

	plt.figure(figsize=(20,40./3.))
	xticks(arange(len(noms1)),noms1,rotation=90,size='xx-large')

	indice=0

	for dot in pentes1 :
		pos = 0

		for x in noms1 : #On trouve l'abcisse
			if x == stat1[indice] :
				break
			else :
				pass
			pos = pos + 1

		dia = int(diametre1[indice]) #La fraction de taille

		if dia == 5 :
			if bool1 :
				bool1 = False
				scatter(pos,dot,color='red',s=120,label = 'taille 0.8 a 5') #On trace

			else :
				scatter(pos,dot,color='red',s=120)

		if dia == 2000 :
			if bool2 :
				bool2 = False
				scatter(pos,dot,color='blue',s=120,label = 'taille 180 a 2000')
			else : 
				scatter(pos,dot,color='blue',s=120)

		if dia == 180 :
			if bool3 :
				bool3 = False
				scatter(pos,dot,color='green',s=120, label = 'taille 20 a 180')
			else :
				scatter(pos,dot,color='green',s=120)

		if dia == 20 :
			if bool4 :
				bool4 = False
				scatter(pos,dot,color='magenta',s=120,label = 'taille 5 a 20')
			else :
				scatter(pos,dot,color='magenta',s=120)


		indice = indice + 1

	plt.title('avant derniere pentes (2)',size='xx-large')
	plt.legend()

	savefig('C:\\Users\\valentin\Desktop\\boulot_mines\\S3Recherche\\BDD\\ProtistTV9subtabs293\\analyse\\pentes1_{}_graph.png'.format(k))

	clf()

	plt.figure(figsize=(20,40./3.))
	xticks(arange(len(noms2)),noms2,rotation=90,size='xx-large')

	indice=0
	bool1 = True
	bool2 = True
	bool3 = True
	bool4 = True


	for dot in pentes2 :
		pos = 0

		for x in noms2 :
			if x == stat2[indice] :
				break
			else :
				pass
			pos = pos + 1

		dia = int(diametre2[indice])

		if dia == 5 :
			if bool1 :
				bool1 = False
				scatter(pos,dot,color='red',s=120,label = 'taille 0.8 a 5') #On trace

			else :
				scatter(pos,dot,color='red',s=120)

		if dia == 2000 :
			if bool2 :
				bool2 = False
				scatter(pos,dot,color='blue',s=120,label = 'taille 180 a 2000')
			else : 
				scatter(pos,dot,color='blue',s=120)

		if dia == 180 :
			if bool3 :
				bool3 = False
				scatter(pos,dot,color='green',s=120, label = 'taille 20 a 180')
			else :
				scatter(pos,dot,color='green',s=120)

		if dia == 20 :
			if bool4 :
				bool4 = False
				scatter(pos,dot,color='magenta',s=120,label = 'taille 5 a 20')
			else :
				scatter(pos,dot,color='magenta',s=120)


		indice = indice + 1
	plt.title('derniere pentes (1)',size='xx-large')
	plt.legend()
	savefig('C:\\Users\\valentin\Desktop\\boulot_mines\\S3Recherche\\BDD\\ProtistTV9subtabs293\\analyse\\pentes2_{}_graph.png'.format(k))

	clf()

	plt.figure(figsize=(20,40./3.))
	xticks(arange(len(noms3)),noms3,rotation=90,size='xx-large')

	indice=0
	bool1 = True
	bool2 = True
	bool3 = True
	bool4 = True

	for dot in pentes3 :
		pos = 0

		for x in noms3 :
			if x == stat3[indice] :
				break
			else :
				pass
			pos = pos + 1

		dia = int(diametre3[indice])

		if dia == 5 :
			if bool1 :
				bool1 = False
				scatter(pos,dot,color='red',s=120,label = 'taille 0.8 a 5') #On trace

			else :
				scatter(pos,dot,color='red',s=120)

		if dia == 2000 :
			if bool2 :
				bool2 = False
				scatter(pos,dot,color='blue',s=120,label = 'taille 180 a 2000')
			else : 
				scatter(pos,dot,color='blue',s=120)

		if dia == 180 :
			if bool3 :
				bool3 = False
				scatter(pos,dot,color='green',s=120, label = 'taille 20 a 180')
			else :
				scatter(pos,dot,color='green',s=120)

		if dia == 20 :
			if bool4 :
				bool4 = False
				scatter(pos,dot,color='magenta',s=120,label = 'taille 5 a 20')
			else :
				scatter(pos,dot,color='magenta',s=120)


		indice = indice + 1

	plt.title('Pentes uniques',size='xx-large')
	plt.legend()
	savefig('C:\\Users\\valentin\Desktop\\boulot_mines\\S3Recherche\\BDD\\ProtistTV9subtabs293\\analyse\\pentes3_{}_graph.png'.format(k))

	clf()


	#On trace tout sur une même courbe


	plt.figure(figsize=(20,40./3.))
	xticks(arange(len(liste_stations)),liste_stations,rotation=90,size='xx-large')


	allPentes=pentes1+pentes2+pentes3
	allDiametre= diametre1+diametre2+diametre3
	allStat = stat1+stat2+stat3
	allNoms = list()
	nbDe1 = len(pentes1)-1


	bool1 = True
	bool2 = True
	bool3 = True
	bool4 = True
	bool5 = True
	bool6 = True
	bool7 = True
	bool8 = True

	indice=0

	for dot in allPentes :
		pos = 0

		for x in liste_stations :
			if x == allStat[indice] :
				break
			else :
				pass
			pos = pos + 1

		dia = int(allDiametre[indice])

		if dia == 5 :
			if nbDe1<indice :
				if bool1 :
					bool1 = False
					scatter(pos,dot,color='red',s=120,label = 'avant derniere pente (2), taille 0.8 a 5')
				else : 
					scatter(pos,dot,color='red',s=120)
			else : 
				if bool2 :
					bool2 = False
					scatter(pos,dot,color=(0.75,0.1,0.3),s=120,label = 'derniere pente (1), taille 0.8 a 5')
				else : 
					scatter(pos,dot,color=(0.75,0.1,0.3),s=120)

		if dia == 2000 :
			if nbDe1<indice :
				if bool3 :
					bool3 = False
					scatter(pos,dot,color='blue',s=120,label = 'avant derniere pente (2), taille 5 a 20')
				else : 
					scatter(pos,dot,color='blue',s=120)
			else :
				if bool4 :
					bool4 = False
					scatter(pos,dot,color=(0.1,0.3,0.75),s=120,label = 'derniere pente (1), taille 5 a 20')
				else : 
					scatter(pos,dot,color=(0.1,0.3,0.75),s=120)

		if dia == 180 :
			if nbDe1<indice :
				if bool5 :
					bool5 = False
					scatter(pos,dot,color='green',s=120,label = 'avant derniere pente (2), taille 20 a 180')
				else :
					scatter(pos,dot,color='green',s=120)
			else :
				if bool6 :
					bool6 = False
					scatter(pos,dot,color=(0.3,0.75,0.1),s=120,label = 'derniere pente (1), taille 20 a 180')
				else :
					scatter(pos,dot,color=(0.3,0.75,0.1),s=120)

		if dia == 20 :
			if nbDe1<indice :
				if bool7 :
					bool7 = False
					scatter(pos,dot,color='magenta',s=120,label = 'derniere pente (1), taille 180 a 2000')
				else : 
					scatter(pos,dot,color='magenta',s=120)
			else :
				if bool8 :
					bool8 = False
					scatter(pos,dot,color=(0.5,0,0.5),s=120,label = 'derniere pente (1), taille 180 a 2000')
				else :
					scatter(pos,dot,color=(0.5,0,0.5),s=120)


		indice = indice + 1

	plt.title('Toutes pentes et tailles confondues',size='xx-large')
	plt.legend()
	savefig('C:\\Users\\valentin\Desktop\\boulot_mines\\S3Recherche\\BDD\\ProtistTV9subtabs293\\analyse\\pentesAll_{}_graph.png'.format(k))

	clf()


	#Il reste a tracer toutes les fractions de taille sur un graph different a chaque fois

	plt.figure(figsize=(20,40./3.))
	xticks(arange(len(liste_stations)),liste_stations,rotation=90,size='xx-large')


	allPentes=pentes1+pentes2+pentes3
	allDiametre= diametre1+diametre2+diametre3
	allStat = stat1+stat2+stat3
	allNoms = list()



	indice=0
	bool1 = True
	bool2 = True
	bool3 = True
	bool4 = True

	for dot in allPentes :
		pos = 0

		for x in liste_stations :
			if x == allStat[indice] :
				break
			else :
				pass
			pos = pos + 1

		dia = int(allDiametre[indice])

		if dia == 5 :
			if bool1 :
				bool1 = False
				scatter(pos,dot,color='red',s=120,label = 'taille 0.8 a 5')
			else :
				scatter(pos,dot,color='red',s=120)

		indice = indice + 1

	plt.title('Fraction de taille : 0.8 a 5',size='xx-large')
	plt.legend()
	savefig('C:\\Users\\valentin\Desktop\\boulot_mines\\S3Recherche\\BDD\\ProtistTV9subtabs293\\analyse\\pentes5_{}_graph.png'.format(k))

	clf()

	plt.figure(figsize=(20,40./3.))
	xticks(arange(len(liste_stations)),liste_stations,rotation=90,size='xx-large')


	allPentes=pentes1+pentes2+pentes3
	allDiametre= diametre1+diametre2+diametre3
	allStat = stat1+stat2+stat3
	allNoms = list()



	indice=0

	for dot in allPentes :
		pos = 0

		for x in liste_stations :
			if x == allStat[indice] :
				break
			else :
				pass
			pos = pos + 1

		dia = int(allDiametre[indice])

		if dia == 2000 :
			if bool2 :
				bool2 = False
				scatter(pos,dot,color='blue',s=120,label = 'taille 180 a 2000')
			else : 
				scatter(pos,dot,color='blue',s=120)

		indice = indice + 1

	plt.title('Fraction de taille : 180 a 2000',size='xx-large')
	plt.legend()
	savefig('C:\\Users\\valentin\Desktop\\boulot_mines\\S3Recherche\\BDD\\ProtistTV9subtabs293\\analyse\\pentes2000_{}_graph.png'.format(k))

	clf()

	plt.figure(figsize=(20,40./3.))
	xticks(arange(len(liste_stations)),liste_stations,rotation=90,size='xx-large')


	allPentes=pentes1+pentes2+pentes3
	allDiametre= diametre1+diametre2+diametre3
	allStat = stat1+stat2+stat3
	allNoms = list()


	indice=0

	for dot in allPentes :
		pos = 0

		for x in liste_stations :
			if x == allStat[indice] :
				break
			else :
				pass
			pos = pos + 1

		dia = int(allDiametre[indice])

		if dia == 180 :
			if bool3 : 
				bool3 = False
				scatter(pos,dot,color='green',s=120, label = '20 a 180')
			else : 
				scatter(pos,dot,color='green',s=120)

		indice = indice + 1

	plt.title('Fraction de taille : 20 a 180',size='xx-large')
	plt.legend()
	savefig('C:\\Users\\valentin\Desktop\\boulot_mines\\S3Recherche\\BDD\\ProtistTV9subtabs293\\analyse\\pentes180_{}_graph.png'.format(k))

	clf()

	plt.figure(figsize=(20,40./3.))
	xticks(arange(len(liste_stations)),liste_stations,rotation=90,size='xx-large')


	allPentes=pentes1+pentes2+pentes3
	allDiametre= diametre1+diametre2+diametre3
	allStat = stat1+stat2+stat3
	allNoms = list()


	indice=0

	for dot in allPentes :
		pos = 0

		for x in liste_stations :
			if x == allStat[indice] :
				break
			else :
				pass
			pos = pos + 1

		dia = int(allDiametre[indice])

		if dia == 20 :
			if bool4 :
				bool4 = False
				scatter(pos,dot,color='magenta',s=120, label = 'taille 5 a 20')
			else : 
				scatter(pos,dot,color='magenta',s=120)


		indice = indice + 1

	plt.title('Fraction de taille : 5 a 20',size='xx-large')
	plt.legend()
	savefig('C:\\Users\\valentin\Desktop\\boulot_mines\\S3Recherche\\BDD\\ProtistTV9subtabs293\\analyse\\pentes20_{}_graph.png'.format(k))

	clf()
	if nbfinal != 0 :
		print('pente moyenne : {}'.format(valfinale/nbfinal))
	if lPP != 0 :
		print('premiere pente moyenne : {}'.format(pPP/lPP))
	if lSP != 0:
		print('seconde pente moyenne : {}'.format(pSP/lSP))
	print('abondances moyennes : {}'.format(abondanceMoyenne))



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