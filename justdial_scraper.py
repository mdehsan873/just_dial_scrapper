from bs4 import BeautifulSoup
import urllib
import csv
import constant


def getDetails(body):
	name= body.find('span', {'class':constant.NAME_CLASS}).a.string
	phone=body.find('p', {'class':constant.CONTACT_CLASS}).span.a.string
	address=body.find('span', {'class':constant.ADDRESS_CLASS}).text.strip()
	dict_service = {}
	dict_service['Name']=name
	dict_service['Phone']=phone
	dict_service['Address']=address
	print(dict_service)
	return dict_service

#page count for page
def scraper():
	page_number = 1
	service_count = 1
	fields = ['Name', 'Phone', 'Address']
	out_file = open('Mumbai_electricians.csv','w')
	csvwriter = csv.DictWriter(out_file, delimiter=',', fieldnames=fields)

	while True:
		if page_number > 10:
			break
			
		req = urllib.request.Request(constant.URL, headers={'User-Agent' : "Magic Browser"}) 
		page = urllib.request.urlopen( req )
		soup = BeautifulSoup(page.read(), "html.parser")
		services = soup.find_all('li', {'class': 'cntanr'})
		for service_html in services:
			csvwriter.writerow(getDetails(service_html))
			service_count += 1
		page_number += 1

	out_file.close()