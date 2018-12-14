import lxml
import pygal  
line_chart = pygal.Bar()
line_chart.title = 'Branch Of Bubble Tea'
line_chart.add('Koi The', 11)
line_chart.add('Ochaya', 50)
line_chart.add('Mr. Shake', 18)
line_chart.add('CHA BAR', 1)
line_chart.add('Coco', 15)
line_chart.add('Dakashi', 11)
line_chart.add('Mikucha', 33)
line_chart.add('ATM Tea Bar', 1)
line_chart.add('Kamu', 20)
line_chart.add('The alley', 2)
line_chart.add("Moma's Bubble Tea Bar", 52)
line_chart.render_in_browser()
