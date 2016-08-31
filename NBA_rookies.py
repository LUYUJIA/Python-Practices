#encoding:utf-8
import requests
from pyquery import PyQuery as pq
import time

all_stars_dict = {}

for  year in xrange(1950,2017):
	print year
	time.sleep(1)

	#visit all_stars page
	url = "http://www.stat-nba.com/award/item12isnba1season{0}.html".format(year)
	req = requests.get(url)
	req.encoding = "utf-8"

	#analyze 
	doc = pq(req.text)
	names = doc('td[class*="normal player_name_out change_color col0"]')

	#get name and url
	for name in names.items():
		name_url = name.find('a').attr('href')
		all_stars_dict[name_url]=name.text()

rookie_list = []
#visit rookie page
for year in xrange(1947,2016):
	print year
	time.sleep(1)
	rookie_dict = {}
	rookie_url = "http://www.stat-nba.com/award/item11isnba1season{0}.html".format(year)
	req = requests.get(rookie_url)
	req.encoding = "utf-8"

	#analyze 
	doc = pq(req.text)
	names = doc('td[class*="normal player_name_out change_color col1"]')

	#get name and url
	for  name in names.items():
		name_url = name.find('a').attr('href')
		rookie_dict[name_url] = name.text()
	rookie_list.append([year, rookie_dict])

for data in rookie_list:
	nobody = True
	for url in data[1]:
		if url in all_stars_dict:
			nobody = False
			break
	if nobody:
		dic=data[1]
		for j in dic:
			print str(data[0])+" "+dic[j]+"\n"


		


