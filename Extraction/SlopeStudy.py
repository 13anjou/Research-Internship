#!/usr/bin/env python
#-*- coding: utf-8 -*-

import numpy #Module servant à faire les regressions linéaires
from pylab import * #Pour le tracé
import matplotlib.pyplot as plt
from decimal import*
import gc
import csv



def optimisation_decoupage(data,k,tailleBin,nom,rank,sN,dictionnaire) : #data correspond au vecteur d'entrée, k à la variable de poids
	clf()
	gc.collect()

	donnees=list()
	longueurs=list()
	poidsDesPentesAvant = list()
	data.pop()
	tailleBin.pop()
	rank.pop()
	donnees=data
	del data
	gc.collect()
	data=donnees
	del donnees
			#////////////////////////////////////////////////////////////////////////////////////////////////////////////////
			#MODIF LE 04/12
			#/////////////////////////////////////////////////////////////////////////////////////////////////////////////////
	data.reverse()
	rank.reverse()
	tailleBin.reverse()



	gc.collect()
	longueur=len(data)
	w=0 #w est le poids total de la structure 
			#////////////////////////////////////////////////////////////////////////////////////////////////////////////////
			#MODIF LE 10/12
			#/////////////////////////////////////////////////////////////////////////////////////////////////////////////////
	#solution = [0]*(longueur+1) #la liste contenant les bornes de notre solution
	#pentes = [0]*(2*(longueur+1)) #la liste contenant les pentes et ordonnees à l'origine de chaque segment de courbe
	#poids_segments = [0]*(longueur+1) #Les poids de chaque segment	
	solution = [0]*(longueur+2) #la liste contenant les bornes de notre solution
	pentes = [0]*(2*(longueur+2)) #la liste contenant les pentes et ordonnees à l'origine de chaque segment de courbe	
	poids_segments = [0]*(longueur+2) #Les poids de chaque segment
	i=1 #le premier indice libre dans solution, le premier 0 correspond au début du premier segment
	n=0 #l'indice de dots
	compteur=0
	a_considerer=True
	nb_sautes=0

	while n<(longueur+1) :
		#print(n)
		compteur=compteur+1
		
		p_avec=0
		if a_considerer :

			if n==0: #On initialise
				print(longueur)
				solution[i]=5 #Le premier point est la première borne du nouveau segment
				 #On récupère directement les 5 premiers points pour avoir un segment de courbe significatif
				i=i+1
				a_considerer=False
				nb_sautes=0

				w,a,b,poids_segments=poids(solution,k,data,poids_segments,tailleBin,rank)
				

				

			else : 	
				avec = solution
				avec[i-1]=avec[i-1]+1 #On ajoute le point au segment en cours


				
				poids_segments_avec=poids_segments
				p_avec,a,b,poids_segments_avec=poids(avec,k,data,poids_segments_avec,tailleBin,rank) #On calcul le poids de la nouvelle solution
				
			
				#print("on compare le poids relatif {} avec le poids précédent pondéré {}".format((p_avec+k*abs(pentes[2*i-4]-a)),w*k*10))
				#if p_avec<w*k+3 : #Si la solution nouvelle a un poids plus faible. MODIFICATION 27/11
			#////////////////////////////////////////////////////////////////////////////////////////////////////////////////
			#MODIF LE 27/11
			#/////////////////////////////////////////////////////////////////////////////////////////////////////////////////
				if p_avec<k : #Si la solution nouvelle a un poids plus faible.
					#print("on choisit de conserver ce nouveau vecteur")
					solution = avec #On conserve cette solution
					pentes[2*i-4]=a #On change la pente du segment qui lui colle le mieux avec la nouvelle valeur
					pentes[2*i-3]=b #Idem avec l'ordonnée à l'origine
					
					poids_segments=poids_segments_avec
			#////////////////////////////////////////////////////////////////////////////////////////////////////////////////
			#MODIF LE 27/11
			#/////////////////////////////////////////////////////////////////////////////////////////////////////////////////
					#poids_segments[i-1]=poids_segments[i-1]/10 MODIFICATION 27/11
					print("les donnees des poids sont : {}".format(poids_segments))
					w=p_avec #On conserve le poids de la nouvelle solution


				else :
					#print("on conserve l'ancien segment et on cree une nouvelle courbe")
					print("les poids valent {}".format(poids_segments))
					
					solution[i-1]=solution[i-1]-1
					solution[i]=min(n+5,longueur-1) #Sinon on démare un nouveau segment : n est l'indice du premier point de ce segment
					i=i+1 #On va chercher la borne suivante
					a_considerer=False
					nb_sautes=0



			n=n+1

		else :
			
			n=n+1
			nb_sautes=nb_sautes+1
			if (nb_sautes==5) :
				w,a,b,poids_segments=poids(solution,k,data,poids_segments,tailleBin,rank)
				pentes[2*i-4]=a #On change la pente du segment qui lui colle le mieux avec la nouvelle valeur
				pentes[2*i-3]=b #Idem avec l'ordonnée à l'origine
				a_considerer=True
			elif n==longueur-1 :
				solution[i-1]=solution[i-1]-1
				w,a,b,poids_segments=poids(solution,k,data,poids_segments,tailleBin,rank)
				pentes[2*i-4]=a #On change la pente du segment qui lui colle le mieux avec la nouvelle valeur
				pentes[2*i-3]=b #Idem avec l'ordonnée à l'origine
				a_considerer=True

		if n==(longueur):
			solution[i]=n
			
			print("les donnees des courbes sont {}".format(pentes))
			break

	l=len(data) #Préparation des axes
	
	indice=-1

	for dot in solution : #On enleve les derniers points qui correspondent a des bins partiels
		indice=indice+1
		if dot==100 :
			solution[indice]=98


	indice=0
	clf()
	indice = 0
	t=0
	#z=scatter(rank,data)
	longueur3=len(pentes) #On va supprimer lse zeros inutiles et artificiels
	while indice<longueur3-1 :

		if pentes[indice+1]==0:
			break
		indice=indice+1

	t=(indice+1)/2

	pentes=pentes[0:2*t]
	solution=solution[0:t+1]


	#////////////////////////////////////////////////////////////////////////////////////////////////////////////////
	#MODIF LE 04/12
	#/////////////////////////////////////////////////////////////////////////////////////////////////////////////////

	print(pentes)
	print(solution)
	print(rank)
		
	pentes = inverserPentes(pentes)
	solution=inverserSol(solution)
	data.reverse()
	rank.reverse()
	tailleBin.reverse()

	#print(pentes)
	print(solution)
	print(data)
	#print(rank)
	




	z=scatter(rank,data) #On trace
	indice=0 #Mauvais intervalle

			#////////////////////////////////////////////////////////////////////////////////////////////////////////////////
			#MODIF LE 10/12
			#/////////////////////////////////////////////////////////////////////////////////////////////////////////////////

	if solution != [] :
		y1=linspace(0,rank[solution[1]-1],20)
		print(0,rank[solution[1]-1],pentes[0],pentes[1],solution[1]-1)
		plot(y1,pentes[0]*(y1)+pentes[1])
		longueurs = longueurs + [rank[solution[1]-1]]
		poidsDesPentesAvant = poidsDesPentesAvant + [poidsCalc(0,solution[1]-1,pentes[0],pentes[1],data,rank)]


	if t>1 :
		y2=linspace(rank[solution[1]-1],rank[solution[2]-1],20)
		plot(y2,pentes[2]*(y2)+pentes[3])
		longueurs = longueurs + [rank[solution[2]-1]-rank[solution[1]-1]]
		poidsDesPentesAvant = poidsDesPentesAvant + [poidsCalc(solution[1]-1,solution[2]-1,pentes[2],pentes[3],data,rank)]

	if t>2 :
		y3=linspace(rank[solution[2]-1],rank[solution[3]-1],20)
		plot(y3,pentes[4]*(y3)+pentes[5])
		longueurs = longueurs + [rank[solution[3]-1]-rank[solution[2]-1]]
		poidsDesPentesAvant = poidsDesPentesAvant + [poidsCalc(solution[2]-1,solution[3]-1,pentes[4],pentes[5],data,rank)]

	if t>3 :
		y4=linspace(rank[solution[3]-1],rank[solution[4]-1],20)
		plot(y4,pentes[6]*(y4)+pentes[7])
		longueurs = longueurs + [rank[solution[4]-1]-rank[solution[3]-1]]
		poidsDesPentesAvant = poidsDesPentesAvant + [poidsCalc(solution[3]-1,solution[4]-1,pentes[6],pentes[7],data,rank)]

	if t>4 :
		y5=linspace(rank[solution[4]-1],rank[solution[5]-1],20)
		plot(y5,pentes[8]*(y5)+pentes[9])
		longueurs = longueurs + [rank[solution[5]-1]-rank[solution[4]-1]]
		poidsDesPentesAvant = poidsDesPentesAvant + [poidsCalc(solution[4]-1,solution[5]-1,pentes[8],pentes[9],data,rank)]

	if t>5 :
		y6=linspace(rank[solution[5]-1],rank[solution[6]-1],20)
		plot(y6,pentes[10]*(y6)+pentes[11])
		longueurs = longueurs + [rank[solution[6]-1]-rank[solution[5]-1]]
		poidsDesPentesAvant = poidsDesPentesAvant + [poidsCalc(solution[5]-1,solution[6]-1,pentes[10],pentes[11],data,rank)]

	if t>6 :
		y7=linspace(rank[solution[6]-1],rank[solution[7]-1],20)
		plot(y7,pentes[12]*(y7)+pentes[13])
		longueurs = longueurs + [rank[solution[7]-1]-rank[solution[6]-1]]
		poidsDesPentesAvant = poidsDesPentesAvant + [poidsCalc(solution[6]-1,solution[7]-1,pentes[12],pentes[13],data,rank)]

	if t>7 :
		y8=linspace(rank[solution[7]-1],rank[solution[8]-1],20)
		plot(y8,pentes[14]*(y8)+pentes[15])
		longueurs = longueurs + [rank[solution[8]-1]-rank[solution[7]-1]]
		poidsDesPentesAvant = poidsDesPentesAvant + [poidsCalc(solution[7]-1,solution[8]-1,pentes[14],pentes[15],data,rank)]

	if t>8 :
		y9=linspace(rank[solution[8]-1],rank[solution[9]-1],20)
		plot(y9,pentes[16]*(y9)+pentes[17])
		longueurs = longueurs + [rank[solution[9]-1]-rank[solution[8]-1]]
		poidsDesPentesAvant = poidsDesPentesAvant + [poidsCalc(solution[8]-1,solution[9]-1,pentes[16],pentes[17],data,rank)]

	if t>9 :
		y10=linspace(rank[solution[9]-1],rank[solution[10]-1],20)
		plot(y10,pentes[18]*(y10)+pentes[19])
		longueurs = longueurs + [rank[solution[10]-1]-rank[solution[9]-1]]
		poidsDesPentesAvant = poidsDesPentesAvant + [poidsCalc(solution[9]-1,solution[10]-1,pentes[18],pentes[19],data,rank)]

	if t>10:
		y11=linspace(rank[solution[10]-1],rank[solution[11]-1],20)
		plot(y11,pentes[20]*(y11)+pentes[21])
		longueurs = longueurs + [rank[solution[11]-1]-rank[solution[10]-1]]
		poidsDesPentesAvant = poidsDesPentesAvant + [poidsCalc(solution[10]-1,solution[11]-1,pentes[20],pentes[21],data,rank)]

	if t>11:
		y11=linspace(rank[solution[11]-1],rank[solution[12]-1],20)
		plot(y11,pentes[22]*(y11)+pentes[23])
		longueurs = longueurs + [rank[solution[12]-1]-rank[solution[11]-1]]
		poidsDesPentesAvant = poidsDesPentesAvant + [poidsCalc(solution[11]-1,solution[12]-1,pentes[22],pentes[23],data,rank)]

	if t>12:
		y11=linspace(rank[solution[12]-1],rank[solution[13]-1],20)
		plot(y11,pentes[24]*(y11)+pentes[25])
		longueurs = longueurs + [rank[solution[13]-1]-rank[solution[12]-1]]
		poidsDesPentesAvant = poidsDesPentesAvant + [poidsCalc(solution[12]-1,solution[13]-1,pentes[24],pentes[25],data,rank)]

	if t>13:
		y11=linspace(rank[solution[13]-1],rank[solution[14]-1],20)
		plot(y11,pentes[26]*(y11)+pentes[27])
		longueurs = longueurs + [rank[solution[14]-1]-rank[solution[13]-1]]
		poidsDesPentesAvant = poidsDesPentesAvant + [poidsCalc(solution[13]-1,solution[14]-1,pentes[26],pentes[27],data,rank)]

	if t>14:
		y11=linspace(rank[solution[14]-1],rank[solution[15]-1],20)
		plot(y11,pentes[28]*(y11)+pentes[29])
		longueurs = longueurs + [rank[solution[15]-1]-rank[solution[14]-1]]
		poidsDesPentesAvant = poidsDesPentesAvant + [poidsCalc(solution[14]-1,solution[15]-1,pentes[28],pentes[29],data,rank)]

	if t>15:
		y11=linspace(rank[solution[15]-1],rank[solution[16]-1],20)
		plot(y11,pentes[30]*(y11)+pentes[31])
		longueurs = longueurs + [rank[solution[16]-1]-rank[solution[15]-1]]
		poidsDesPentesAvant = poidsDesPentesAvant + [poidsCalc(solution[15]-1,solution[16]-1,pentes[30],pentes[31],data,rank)]

	if t>16:
		y11=linspace(rank[solution[16]-1],rank[solution[17]-1],20)
		plot(y11,pentes[32]*(y11)+pentes[33])
		longueurs = longueurs + [rank[solution[17]-1]-rank[solution[16]-1]]
		poidsDesPentesAvant = poidsDesPentesAvant + [poidsCalc(solution[16]-1,solution[17]-1,pentes[32],pentes[33],data,rank)]

	if t>17:
		y11=linspace(rank[solution[17]-1],rank[solution[18]-1],20)
		plot(y11,pentes[34]*(y11)+pentes[35])
		longueurs = longueurs + [rank[solution[18]-1]-rank[solution[17]-1]]
		poidsDesPentesAvant = poidsDesPentesAvant + [poidsCalc(solution[17]-1,solution[18]-1,pentes[34],pentes[35],data,rank)]

	if t>18:
		y11=linspace(rank[solution[18]-1],rank[solution[19]-1],20)
		plot(y11,pentes[36]*(y11)+pentes[37])
		longueurs = longueurs + [rank[solution[19]-1]-rank[solution[18]-1]]
		poidsDesPentesAvant = poidsDesPentesAvant + [poidsCalc(solution[18]-1,solution[19]-1,pentes[36],pentes[37],data,rank)]

	if t>19:
		y11=linspace(rank[solution[19]-1],rank[solution[20]-1],20)
		plot(y11,pentes[38]*(y11)+pentes[39])
		longueurs = longueurs + [rank[solution[20]-1]-rank[solution[19]-1]]
		poidsDesPentesAvant = poidsDesPentesAvant + [poidsCalc(solution[19]-1,solution[20]-1,pentes[38],pentes[39],data,rank)]

	if t>20:
		y11=linspace(rank[solution[20]-1],rank[solution[21]-1],20)
		plot(y11,pentes[40]*(y11)+pentes[41])
		longueurs = longueurs + [rank[solution[21]-1]-rank[solution[20]-1]]
		poidsDesPentesAvant = poidsDesPentesAvant + [poidsCalc(solution[20]-1,solution[21]-1,pentes[40],pentes[41],data,rank)]

	gc.collect()

	yticks(fontsize = 20)
	xticks(fontsize = 20)
	plt.xlabel("Rank", fontsize = 20)
	plt.ylabel("Abundance", fontsize = 20)
	plt.legend()
	plt.title('Rank/abundance distribution for the station {}'.format(sN),fontsize = 20)
	try :
		savefig('C:\\Users\\valentin\Desktop\\boulot_mines\\S3Recherche\\BDD\\ProtistTV9subtabs293\\analyse\\station_{}_{}_{}_{}_{}graph.png'.format(nom,k,sN,dictionnaire[sN][0],dictionnaire[sN][1]))
	except IndexError:
		savefig('C:\\Users\\valentin\Desktop\\boulot_mines\\S3Recherche\\BDD\\ProtistTV9subtabs293\\analyse\\station_{}_{}graph.png'.format(nom,k))
	except KeyError:
		savefig('C:\\Users\\valentin\Desktop\\boulot_mines\\S3Recherche\\BDD\\ProtistTV9subtabs293\\analyse\\station_{}_{}graph.png'.format(nom,k))
	del z
	clf()

	del y1

	if t>1 :
		del y2

	if t>2 :
		del y3
	if t>3 :
		del y4
	if t>4 :
		del y5
	if t>5 :
		del y6
	if t>6 :
		del y7
	if t>7 :
		del y8
	if t>8 :
		del y9
	if t>9 :
		del y10
	if t>10:
		del y11

	pentesAConsiderer,tR,sN1,longueursBis,poidsDesPentes = modifPentes(solution,pentes,t,sN,longueurs,poidsDesPentesAvant)

	return solution,pentes,t,pentesAConsiderer,tR,sN1,longueurs,longueursBis,poidsDesPentesAvant,poidsDesPentes

def poids(solution,k,data,poids_liste,tailleBin,rank) :
	w=0
	m=0 #un indice
	l=0 #un deuxième indice
	j=0 #un troisième indice
	n=0 #un quatrième indice
	a=0
	b=0
	getcontext().prec=20
	gc.collect()

	try: 
		while solution[m+1]!=0 : #Tant qu'on n'est pas sur le dernier segment exclut

			if solution[m+2]!=0 : #Tant qu'on n'est pas sur le denrier segment inclut
			#////////////////////////////////////////////////////////////////////////////////////////////////////////////////
			#MODIF LE 27/11
			#/////////////////////////////////////////////////////////////////////////////////////////////////////////////////
				#w=poids_liste[m]+w
				pass

			else : #Si on est sur le dernier segment
				l=solution[m]
				j=solution[m+1]
				vect_en_cours=data[l:j] #On récupère juste le morceau de courbe qui nous intéresse ici
				a,b,c,d= fitting(vect_en_cours,tailleBin[l:j],rank[l:j])
				nb=j-l #le nombre de points dans le segment étudié
				

				while n<nb : #Tant qu'on est sur le segment
			#////////////////////////////////////////////////////////////////////////////////////////////////////////////////
			#MODIF LE 27/11
			#/////////////////////////////////////////////////////////////////////////////////////////////////////////////////
				#MODIF IMPORTANTE ICI LE 27/11
					#val_courbe=b+n*a #La valeur sur la courbe
					val_courbe=b+rank[l+n]*a #La valeur sur la courbe
					ecart = float(abs(val_courbe-vect_en_cours[n]))
					ecart=ecart**2 #L'écart avec les données
					ratio=abs(vect_en_cours[n])
					if ratio==0 : #Juste au cas ou, ces points ayant normalement ete supprimes dans le binning 
						ratio=1
					pos=l+n
					coeff=abs(Decimal(tailleBin[pos]))
			#////////////////////////////////////////////////////////////////////////////////////////////////////////////////
			#MODIF LE 02/12
			#/////////////////////////////////////////////////////////////////////////////////////////////////////////////////
					poids_liste[m]=float(Decimal(poids_liste[m])+Decimal(ecart)*coeff/Decimal(ratio)) #Le poids ajouté pondéré par le nombre de points incluts dans le bining
					#poids_liste[m]=float(Decimal(poids_liste[m])+Decimal(ecart)) #Le poids ajouté pondéré par le nombre de points incluts dans le bining
					n=n+1
			#////////////////////////////////////////////////////////////////////////////////////////////////////////////////
			#MODIF LE 05/12
			#/////////////////////////////////////////////////////////////////////////////////////////////////////////////////
				#w=poids_liste[m]+w #On obtient le poids finial
				#w=poids_liste[m]+w/n #On obtient le poids finial
			#////////////////////////////////////////////////////////////////////////////////////////////////////////////////
			#MODIF LE 27/11
			#/////////////////////////////////////////////////////////////////////////////////////////////////////////////////
				#w=poids_liste[m]+w/n #On obtient le poids finial
				r=1
				for nbBin in tailleBin[l:j] :
					r=r+nbBin
				w=poids_liste[m]+w/r


			m=m+1
	except IndexError:
		#print("Les bornes des vecteurs sont depassees : k n'est surement pas adapte (on cree trop de segments)")
		pass

	return w,a,b,poids_liste


def fitting(vecteur_en_cours,tailleBinPartie,rank) :
	i=0
	ordonnee = vecteur_en_cours
	for x in rank : 
		rank[i]=float(rank[i])
		ordonnee[i]=float(ordonnee[i])
		i=i+1

	l=len(vecteur_en_cours)
	k=0 #Un indice
	j=0 #Un deuxième indice
	#Les ordonnées servant à la regression linéaire
	#vec=polyfit(rank,ordonnee,1,None,False,tailleBinPartie)
	vec=polyfit(rank,ordonnee,1)
	#print(vec)
	a=vec[0]
	b=vec[1]
	gc.collect()
	return a,b,0,l

def modifPentes(solution,pentes,t,sN,longueurs,poidsDesPentesAvant) :

	inf=0 #La pos inf
	debut=True #Initialisation
	maxi=0 #La pos sup
	tR=t
	indice=-1
	pentesAConsiderer=list()
	sN1=list()
	resLongueur=list()
	poidsDesPentes = list()
	#print(pentes)

	for dot in solution :

		if debut : #Initialisation
			maxi=dot
			debut = False

		elif dot ==0 :
			break

		else :
			inf=maxi
			maxi=dot

			if maxi-inf<10 : #On enlève la pente qui n'est pas intéressante

				tR=tR-1
			else :
				#print(len(pentes))
				pentesAConsiderer=pentesAConsiderer+[pentes[2*indice]] #On garde la pente
				sN1=sN1+[sN]
				resLongueur = resLongueur + [longueurs[indice]]
				poidsDesPentes = poidsDesPentes + [poidsDesPentesAvant[indice]]


		indice=indice+1
			#////////////////////////////////////////////////////////////////////////////////////////////////////////////////
			#MODIF LE 01/12
			#/////////////////////////////////////////////////////////////////////////////////////////////////////////////////


	"""test = True

	while test :
		test = False
		indice = 0
		l=len(pentesAConsiderer)

		while indice < l :
			if indice >0 and not test :

				if (pentesAConsiderer[indice]-pentesAConsiderer[indice-1])/pentesAConsiderer[indice] < 0.1 * pentesAConsiderer[indice] :

					pentesAConsiderer[indice-1] = (pentesAConsiderer[indice-1]*resLongueur[indice-1]+pentesAConsiderer[indice]/resLongueur[indice])/(resLongueur[indice-1]+resLongueur[indice])
					pentesAConsiderer = retirer(pentesAConsiderer,indice)
					tR = tR-1
					resLongueur[indice-1] = resLongueur[indice-1]+resLongueur[indice]
					resLongueur = retirer(resLongueur,indice)
					l=l-1
					sN1 = retirer(sN1,indice)
					test = True
					#print("MODIFICATION")
					break

			indice = indice + 1


	if tR>2 :
		tR=2

		l=len(sN1)
		pentesAConsiderer = pentesAConsiderer[l-2:l]
		sN1 = sN1[l-2:l]
		resLongueur=resLongueur[l-2:l]
		poidsDesPentes=poidsDesPentes[l-2:l]"""
	return(pentesAConsiderer,tR,sN1,resLongueur,poidsDesPentes)


def poidsCalc(rang1,rang2,a,b,data,rank) :

	#y=ax+b

	p = 0
	i=0
	a=float(a)
	b=float(b)


	data = data[rang1:rang2]
	rank = rank[rang1:rang2]


	for d in data : 
		p = p + (float(d)-(a*float(rank[i])+b))**2
		i = i+1


	return(p)
def inverserSol(liste) :
	maximum = liste[-1]
	liste=[maximum-x for x in liste]
	liste.sort()

	return(liste)
def inverserPentes(pentes) :

	res= list()
	p=0
	coef1 = True
	for p in pentes :

		if coef1: 
			coef1 = False
			a=p
		else :
			coef1 = True
			res= [a,p]+res
	return(res)