#!/usr/bin/env python
#-*- coding: utf-8 -*-

import csv
from pylab import*
import numpy
import math
import matplotlib.pyplot as plt
import numbers
#En cours : Ribo
k = 0.01
s = 0.8
import dico as d
import regression as regres
import repartition as repart
import histogram as histo




def main() :

	#repart.avec() #On commence par tracer les pentes en fonction de la taille du fit avec toutes les pentes trouvees. 
	#repart.sans() #On commence par tracer les pentes en fonction de la taille du fit sans les pentes les plus eloignees. 
	d.pentesAvec() #Utilite ? 
	d.pentesSans() #Utilite ? 
	#d.serie(35)
	#d.serie(36)
	regres.etudePentes() #On regarde l'influence des parametres sur l'ensemble des pentes
	regres.etudePentesSans() #Idem avec les pentes selectionnes uniquement
	histo.main()
	histo.sans()

	#d.div()
	#d.serieTot()




if __name__ == "__main__" :
	main()	
