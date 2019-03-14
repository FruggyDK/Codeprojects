import numpy as np 
from prettytable import PrettyTable

#varibles
t1 = 0
t2 = 0
t3 = 0
t4 = 0
t5 = 0
t6 = 0

teori = round((1/6) *100, 4)

#user input
print("Total throws =?")

total = int(input(">"))

#def

def Frekvens_i_statistik(x):
	return round((x / total) *100, 4)

def Afvigelse_i_procent(x):
	return round(((Frekvens_i_statistik(x) - teori)/ teori) *100, 4)

#main
numbers = []

numbers = np.random.randint(low = 1, high = 7, size = total)

#checker
for number in numbers:
  if number == 1:
  	t1 += 1
  elif number == 2:
    t2 += 1
  elif number == 3:
    t3 += 1
  elif number == 4:
    t4 += 1
  elif number == 5:
    t5 += 1
  else :
    t6 += 1
else :

	#output
	x = PrettyTable()

	x.field_names = ["Hændelse", "Antal", "Frekvens i statistik(%)", "Frekvens i teori(%)", "Afvigelse i procent"]

	x.add_row(["1", t1, Frekvens_i_statistik(t1), teori, Afvigelse_i_procent(t1)])
	x.add_row(["2", t2, Frekvens_i_statistik(t2), teori, Afvigelse_i_procent(t2)])
	x.add_row(["3", t3, Frekvens_i_statistik(t3), teori, Afvigelse_i_procent(t3)])
	x.add_row(["4", t4, Frekvens_i_statistik(t4), teori, Afvigelse_i_procent(t4)])
	x.add_row(["5", t5, Frekvens_i_statistik(t5), teori, Afvigelse_i_procent(t5)])
	x.add_row(["6", t6, Frekvens_i_statistik(t6), teori, Afvigelse_i_procent(t6)])
	print(x)
	print("Total: ", total)


#todo genereate x inputs of the original total input, where each new x total is a tenth of the previus one. Store the results of each xtotal, and make a graph of the data.  Figure out how to store the data. and access it, and how to process that into a graph, where the xaxis is total, and the yaxis is the 'afvigelse i procent' -- when that is done, improve the program, so it can run more efficent, and be more user-friendly

