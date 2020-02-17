import gspread
from oauth2client.service_account import ServiceAccountCredentials
import json
import datetime
import os
import urllib.request
from bs4 import BeautifulSoup 

def SGWebScrape(my_url, filename):
	headers = {'User-Agent':'Mozilla/5.0 (Macintosh: Intel Mac OS X 10 10 5) AppleWebKit/537,36 (KHTML, like Gecko) Chrome/47,0,2526,80 Safari/537,36'}
	# opening connection to URL, grabbing page

	#making a request with the header that we created
	req = urllib.request.Request(my_url, headers=headers)

	#send the request
	resp = urllib.request.urlopen(req)

	# reading the resulting html that your browser would normally interpret, and saving it to variable "html"
	html = resp.read()

	#Passing the html to BeautifulSoup for parsing
	page_soup = BeautifulSoup(html, "html.parser")

	data = json.loads(page_soup.find('script', type='application/ld+json').text)


	#omni = page_soup.findAll("script")
	#omni_text = omni[23] omni 23 is what we want
	dateTime = str(datetime.datetime.now().strftime("%I:%M%p on %B %d %Y"))
	highPrice = str(data["offers"]['highPrice'])
	lowPrice = str(data["offers"]['lowPrice'])
	name = str(data['name'])
	startDate = str(data["startDate"])
	endDate = str(data["endDate"])
	homeField = str(data["location"]["name"])
	city = str(data["location"]["address"]["addressLocality"])
	region = str(data["location"]["address"]["addressRegion"])
	inventoryLevel = str(data["offers"]["inventoryLevel"]["value"])

	#f = open(filename,append_write)
	#f.write(dateTime + "," + highPrice + "," + lowPrice+ "," + name+ "," + startDate+ "," + endDate+ "," + homeField+ "," + city+ "," + region+ "," + inventoryLevel + "\n")

	#f.close()

	print("High Price: " + str(highPrice) + " " + "low Price: " + str(lowPrice)) #this can get us high price, low price
	print('''''''''''''''''')
	print("Name: " + str(name))
	print('''''''''''''''''')
	print("Gametime: " + str(startDate) + " - " + str(endDate))
	print('''''''''''''''''')
	print("Homefield: " + str(homeField))
	print('''''''''''''''''')
	print("Location: " + str(city) + ", " + str(region))
	print('''''''''''''''''')
	print("Inventory Level: " + str(inventoryLevel))
 
	# use creds to create a client to interact with the Google Drive API
	scope = ['https://spreadsheets.google.com/feeds']
	creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret_2.json', scope)
	client = gspread.authorize(creds)
	# Find a workbook by name and open the first sheet
	# Make sure you use the right name here.
	sheet = client.open(str(filename)).sheet1
	#This will update a cell
	#sheet.update_cell(1, 1, "I just wrote to a spreadsheet using Python!")
	#This will delete a row
	#sheet.delete_row(182)
	#This gets the row count
	#print(sheet.row_count)
	allRec = sheet.get_all_records()
	index = (len(allRec)+2)
	 
	#Extract and print all of the values
	row = [str(dateTime), str(highPrice), str(lowPrice), str(name), str(startDate), str(endDate), str(homeField), str(city), str(region), str(inventoryLevel)]
	sheet.insert_row(row, index)
	print(filename)
'''
NBA
'''

#11-13
SGWebScrape("https://seatgeek.com/kings-at-wizards-tickets/11-13-2017-washington-district-of-columbia-capital-one-arena/nba/3993758","Kings@Wizards-Nov-13@18:00")
SGWebScrape("https://seatgeek.com/cavaliers-at-knicks-tickets/11-13-2017-new-york-new-york-madison-square-garden/nba/3994064","Cavaliers@Knicks-Nov-13@18:30")
SGWebScrape("https://seatgeek.com/grizzlies-at-bucks-tickets/11-13-2017-milwaukee-wisconsin-bmo-harris-bradley-center/nba/3993781","Grizzlies@Bucks-Nov-13@19:00")
SGWebScrape("https://seatgeek.com/hawks-at-pelicans-tickets/11-13-2017-new-orleans-louisiana-smoothie-king-center/nba/3993511","Hawks@Pelicans-Nov-13@19:00")
SGWebScrape("https://seatgeek.com/lakers-at-suns-tickets/11-13-2017-phoenix-arizona-talking-stick-resort-arena/nba/3993488","Lakers@Suns-Nov-13@20:00")
SGWebScrape("https://seatgeek.com/timberwolves-at-jazz-tickets/11-13-2017-salt-lake-city-utah-vivint-smart-home-arena/nba/3993571","Timberwolves@Jazz-Nov-13@20:00")
SGWebScrape("https://seatgeek.com/nuggets-at-trail-blazers-tickets/11-13-2017-portland-oregon-moda-center/nba/3993724","Nuggets@Trailblazers-Nov-13@21:00")
SGWebScrape("https://seatgeek.com/magic-at-warriors-tickets/11-13-2017-oakland-california-oracle-arena/nba/3993419","Magic@Warriors-Nov-13@21:30")
SGWebScrape("https://seatgeek.com/76ers-at-clippers-tickets/11-13-2017-los-angeles-california-staples-center/nba/3993283","76ers@Clippers-Nov-13@21:30")
#11-14
SGWebScrape("https://seatgeek.com/celtics-at-nets-tickets/11-14-2017-brooklyn-new-york-barclays-center/nba/3995053","Celtics@Nets-Nov-14@18:30")
SGWebScrape("https://seatgeek.com/raptors-at-rockets-tickets/11-14-2017-houston-texas-toyota-center/nba/3993159","Raptors@Rockets-Nov-14@19:00")
SGWebScrape("https://seatgeek.com/spurs-at-mavericks-tickets/11-14-2017-dallas-texas-american-airlines-center/nba/3993967","Spurs@Mavericks-Nov-14@19:30")
