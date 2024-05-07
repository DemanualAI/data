# Code to verify the number of links for each key ie 'year'
import json

# Load JSON data from file
with open('final_cleaned_SC.json', 'r') as json_file:
    data_dict = json.load(json_file)

# Iterate over each year and count the number of links
for year, links in data_dict.items():
    if year == "1963" : 
        print(f"{year} {len(links)}")


