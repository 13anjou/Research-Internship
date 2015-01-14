#!/usr/bin/env python
#-*- coding: utf-8 -*-

import csv
from pylab import*
import numpy
import math
import matplotlib.pyplot as plt
import numbers
k = 0.2
s = 0.8
import dico as d



def main(k) :

	dico = d.main()

	plt.figure(figsize=(20,20))
	plt.title('Mean distance to the power-law distribution versus stations', fontsize = 40)
	plt.legend()

	with open('C:\\Users\\valentin\Desktop\\boulot_mines\\S3Recherche\\Resultats\\log_log\\10_{}\\toutes\\ecartPowerLaw_{}.csv'.format(k,k), 'r') as csvfile:
		
		reader = csv.reader(csvfile, delimiter=';',quotechar=',', quoting=csv.QUOTE_MINIMAL)
		for row in reader :
			scatter(enlever(row[0]),enlever(row[1]))

	yticks(fontsize=40)
	xticks(fontsize=40)
	plt.xlabel("station", fontsize=40)
	plt.ylabel("mean distance to the power-law distribution", fontsize=40)
	savefig('C:\\Users\\valentin\Desktop\\boulot_mines\\S3Recherche\\Python\\correlation\\DistancePowerLaw.png')
	clf()



if __name__ == "__main__" :
	main(k)	

def enlever(s) :
	res = str()
	for l in s : 
		if l ==' ' :
			pass
		else :
			res=res + l
	return(res)