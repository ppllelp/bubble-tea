import csv
import matplotlib.pyplot as plt


with open('t1.csv') as csvfile:
    read = csv.reader(csvfile)
    koi = 0
    ocha = 0
    co = 0
    atm = 0
    alle = 0
    shake = 0
    dak = 0
    mik = 0
    kamu = 0
    mom = 0
    cha = 0
    for row in read:
        if "KOI The" in row:
        	koi += 1

        elif "Ochaya" in row:
        	ocha += 1
        	
        elif "Mr. Shake" in row:
        	shake += 1
        	
        elif "CHA BAR" in row:
        	cha += 1
        	
        elif "Coco" in row:
        	co += 1
        	
        elif "Dakashi" in row:
        	dak += 1
        	
        elif "Mikucha" in row:
        	mik += 1
        	
        elif "ATM Tea Bar" in row:
        	atm += 1
        	
        elif "Kamu" in row:
        	kamu += 1
        	
        elif "The alley" in row:
        	alle += 1
        	
        elif "Moma's Bubble Tea Bar" in row:
        	mom += 1
    x = range(11)
    y = (koi, ocha, shake, cha, co, dak, mik, atm, kamu, alle, mom)
    xtick = ("KOI The","Ochaya","Mr. Shake","CHA BAR","Coco","Dakashi","Mikucha","ATM Tea Bar","Kamu","The alley","Moma's Bubble Tea Bar")
    plt.bar(x, y)
    plt.xticks(x, xtick)
    plt.show()
