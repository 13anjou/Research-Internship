#!/usr/bin/env python
#-*- coding: utf-8 -*-

import csv
from pylab import*
import numpy as np
import pylab as P
import math
from scipy import stats
import matplotlib.pyplot as plt
import dico as d
from scipy.integrate import quad    

from allTest import k, s

import matplotlib.lines as mlines

a=-1.3

#Ici on fait une simulation d'un tirage en power-law
#Puis des sous echantillonages en LN et en prop a l'abondance


def main() :

	pl = list()
	sample1 = list()
	sample2 = list()
	sample3 = list()
	sample4 = list()

	ln = np.random.normal(0,1,100000)	
	ln = array([x for x in ln])
	ln.sort()
	pl = array([math.log10(K(F(x))) for x in ln]) #La distribution aléatoire suivant une power law.
	np.random.shuffle(pl)

	sample1 = array(pl[0:1000])
	x1 = (np.arange(1000)+1)*100
	x1 = [math.log10(x) for x in x1]

	sample2 = array(pl[0:5000])
	x2 = (np.arange(5000)+1)*20
	x2 = [math.log10(x) for x in x2]

	sample3 = array(pl[0:10000])
	x3 = (np.arange(10000)+1)*10
	x3 = [math.log10(x) for x in x3]

	sample4 = array(pl[0:20000])
	x4 = (np.arange(20000)+1)*5
	x4 = [math.log10(x) for x in x4]
	x = (np.arange(100000)+1)
	x = [math.log10(y) for y in x]


	pl.sort()
	pl=pl[::-1]
	sample1.sort()
	sample1=sample1[::-1]
	sample2.sort()
	sample2=sample2[::-1]
	sample3.sort()
	sample3=sample3[::-1]
	sample4.sort()
	sample4=sample4[::-1]

	echant, = plt.plot(x,pl,color='blue')
	echant1, = plt.plot(x1,sample1,color='green')
	"""echant2, = plt.plot(x2,sample2,color='red')
	echant3, = plt.plot(x3,sample3,color='orange')
	echant4, = plt.plot(x4,sample4,color='magenta')

	plt.legend([echant,echant1,echant2,echant3,echant4],["distribution","1000 points","5000 points", "10000 points", "20000 points"])"""
	plt.legend([echant,echant1],["distribution","1000 points"])
	plt.show()


def integrand(t) :
	return(exp(-(t**2)/2))

def F(x) : #Fonction de repartition d'une loi normale
	
	y = 1/math.sqrt(2*math.pi)
	y = y * quad(integrand, -Inf, x)[0]

	return(y)

def K(y) :#Loi inverse de z
	z = (1-y)**(1/(1+a))

	return(z)