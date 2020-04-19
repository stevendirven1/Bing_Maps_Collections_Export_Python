from bs4 import BeautifulSoup
from requests_html import HTMLSession
import pandas as pd
import time
import json
from easyhtml import parser

# Log in to Bing Maps and navigate to My Places -> Collections. Click "Share Collection" and Copy the URL. 
# Anything after the ampersand is not necessary. 
# Paste as many of these collections as you want to export in the array of urls below.
# Create a directory "ExportedData" in the directory where this script is run.
# Data is saved to CSVs in the ExportedData directory with filenames of  "{CollectionName}.csv"
# There is a 30 second delay between pulling collections as there is a chance that the API is rate-limited.

urls = ["https://www.bing.com/maps?osid=5cf3213c-1569-440e-94b0-9d4604cf6123",\
		"https://www.bing.com/maps?osid=8e6113e3-2395-4fec-9635-de749ac8c576"
		]
		
npo_jobs = {}
job_no = 0

for url in urls:
	print (url)
	session = HTMLSession()
	r = session.get(url)
	s = r.html.render(timeout=20)
	data = r.html.html
	session.close()
	soup = BeautifulSoup(data,'html.parser')

	collection = soup.find('div',{'class':'collectionPanelTitle'}).text
	description = soup.find('div',{'class':'collectionDescription'}).text

	for value in soup.find_all('a',{'class':'collectionEntity'}):
		temp = value.get('data-task').strip()
		temp = temp.replace(r"\n", " ")
		thingie = json.loads(temp)
		descriptionList = thingie['state']['descriptionList']
		query = thingie['state']['query']
		taskTitle = thingie['state']['taskTitle']
		originalName = "N/A"
		try:
			originalName = thingie['state']['originalName']
		except:
			originalName = originalName
		npo_jobs[job_no] = [collection, description, descriptionList, query, taskTitle, originalName]
		job_no+=1

	npo_jobs_df = pd.DataFrame.from_dict(npo_jobs, orient = 'index', columns = ['Installer','Location','DescriptionList','Query','TaskTitle','OriginalName']) 
	npo_jobs_df.to_csv("ExportedData/" + collection + ".csv")
	time.sleep(30)
	