import csv
from collections import Counter
import matplotlib.pyplot as plt

def load_data(filename):
    cities = []
    latitudes = {}
    longitudes = {}

    with open(filename, 'r', newline='') as csvfile:
        reader = csv.DictReader(csvfile, delimiter='\t', skipinitialspace=True)
        
        for raw_row in reader:
            # Fully sanitize the keys and values by stripping quotes and spaces
            row = {
                key.strip().replace('"', '').replace(' ', ''):
                value.strip().replace('"', '')
                for key, value in raw_row.items()
            }

            city = row['City']
            lat = int(row['LatD'])
            lon = int(row['LonD'])

            cities.append(city)
            if city not in latitudes:
                latitudes[city] = lat
            if city not in longitudes:
                longitudes[city] = lon

    return cities, latitudes, longitudes

def plot_city_frequencies(cities):
    city_counts = Counter(cities)
    plt.figure(figsize=(16, 8))
    plt.bar(city_counts.keys(), city_counts.values(), color='teal')
    plt.xticks(rotation=45, ha='right')  
    plt.title('Frequency of Cities')
    plt.xlabel('City')
    plt.ylabel('Count')
    plt.tight_layout()  
    plt.show()

def plot_city_locations(latitudes, longitudes):
    plt.figure(figsize=(16, 8))
    for city in latitudes:
        plt.scatter(longitudes[city], latitudes[city], label=city)
        plt.text(longitudes[city], latitudes[city], city, fontsize=8, ha='right')

    plt.title('City Locations by Longitude and Latitude')
    plt.xlabel('Longitude')
    plt.ylabel('Latitude')
    plt.grid(True)
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    file_path = input("Enter CSV file path (e.g., cities.tsv): ")
    cities, latitudes, longitudes = load_data(file_path)
    
    print("City\tLatitude\tLongitude")
    for city in sorted(set(cities)):
        print(f"{city}\t{latitudes[city]}\t{longitudes[city]}")
    
    plot_city_frequencies(cities)
    plot_city_locations(latitudes, longitudes)
