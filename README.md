# Bing_Maps_Collections_Export_Python
This repo contains a single-file python utility that can be used to export data from your Bing Maps Collection of locations to CSV files.

### Dependencies ###
In order to run this script you'll need to install the following dependencies first:

```
pip install beautifulsoup4
pip install requests
pip install easyhtml
pip install pandas
pip install requests-html
```

### Export Preparation ###

Before running the script you will need to:

1. Log in to Bing Maps and navigate to My Places -> Collections. Click "Share Collection" and Copy the URL. 
2. Trim the URL down - Anything after the ampersand is not necessary. 
3. Paste as many of these collections as you want to export in the array called "urls" in the script.
4. Create a directory "ExportedData" in the directory where this script will be run.

Note: There is a 30 second delay between pulling each collection as there is a chance that the API is rate-limited.

### Running the Script ###

To run the script, call:

```
python BingMapsCollectionExport.py
``` 

Data is saved to CSVs in the "/ExportedData" directory with filenames of  "{CollectionName}.csv"

