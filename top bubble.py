import csv
import lxml
import pygal   


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
    line_chart = pygal.HorizontalBar()
    line_chart.title = 'Top Bubble Tea'
    line_chart.add('Koi The', koi)
    line_chart.add('Ochaya', ocha)
    line_chart.add('Mr. Shake', shake)
    line_chart.add('CHA BAR', cha)
    line_chart.add('Coco', co)
    line_chart.add('Dakashi', dak)
    line_chart.add('Mikucha', mik)
    line_chart.add('ATM Tea Bar', atm)
    line_chart.add('Kamu', kamu)
    line_chart.add('The alley', alle)
    line_chart.add("Moma's Bubble Tea Bar", mom)
    
    line_chart.render_in_browser()
    line_chart.render_to_file("bubble.svg")
    

    
