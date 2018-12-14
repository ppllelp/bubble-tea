import lxml
import pygal  
line_chart = pygal.Bar()
line_chart.title = 'Prcie Of Bubble Tea'
line_chart.add('Koi The', 70)
line_chart.add('Ochaya', 35)
line_chart.add('Mr. Shake', 45)
line_chart.add('CHA BAR', 59)
line_chart.add('Coco', 30)
line_chart.add('Dakashi', 30)
line_chart.add('Mikucha', 30)
line_chart.add('ATM Tea Bar', 85)
line_chart.add('Kamu', 45)
line_chart.add('The alley', 70)
line_chart.add("Moma's Bubble Tea Bar", 19)
line_chart.render_in_browser()
