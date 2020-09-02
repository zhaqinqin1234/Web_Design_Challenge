

import os
import pandas as pd


# generate path to csv
csv_path = os.path.join('Resources', 'cities.csv')
cities_csv = pd.read_csv(csv_path)



# create html table and save to file 
cities_csv.to_html('table.html', index=False, classes=['table', 'table-striped', 'table-hover'])



