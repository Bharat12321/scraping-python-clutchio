import re
import requests
import time
from bs4 import BeautifulSoup


class Scraper:
    def __init__(self):
        dataSource = {
			# "Top App Developers in Delhi":"https://clutch.co/in/app-developers/delhi",
			# "Top UX Designers in Delhi":"https://clutch.co/in/agencies/ui-ux/delhi",
			# "Top Mobile App Developers in India":"https://clutch.co/directory/mobile-application-developers-india",   
			# "Top Mobile App Development Companies":"https://clutch.co/directory/mobile-application-developers",
			"Top Web Design Companies":"https://clutch.co/web-designers",
			# "Top Education App Developers":"https://clutch.co/app-developers/education"
			}    	
        self.__datasource = dataSource
        return

    def parsing(self, url):
    	url = url
    	headers = {'User-Agent':'Mozilla/5.0'}
    	page = requests.get(url)
    	soup = BeautifulSoup(page.text, "html.parser")
    	regex = re.compile('company-name')
    	content_lis = soup.find_all('h3', attrs={'class': regex})
    	content = []
    	for a in content_lis:
    		content.append(a.text.split('\n')[1].strip())
    	return content

    def processing(self):
   		dataSource = self.__datasource
   		for i in dataSource:
   			topic = i
   			topic_url = dataSource[i]
   			topic_parsed = i.lower().replace(" ", "_")

   			print("-----------------------------------------------------------------")
   			print("topic_url:- ", topic_url)
   			print("topic_parsed:- ", topic_parsed)
   			print("topic:- ", topic)
   			print("-----------------------------------------------------------------")

   			counter = 453
   			ranked = 0
   			searching_continue = True
   			while searching_continue:
   				data = self.parsing("{}?page={}".format(topic_url,counter))
   				counter = counter+1
   				res_list = [i for i in range(len(data)) if data[i] == "Nickelfox"]
   				print("\nLength of data:- ", len(data))
   				print("Companies in page {} :- {}".format(counter,data))
   				ranked = ranked+len(data)
   				if res_list and len(res_list) > 0:
   					if counter >= 1:
	   					ranked = ranked+res_list[0]-len(data)
	   				else:
	   					ranked = ranked+res_list[0]
   					print("-----------------------------------------------------------------------------------------------------")
   					print("Nickelfox is in page {} for title \"{}\" and Ranked of Nickelfox:- {}".format(counter, i, ranked))
   					print("-----------------------------------------------------------------------------------------------------")
   					searching_continue = False
   				time.sleep(3)

ob = Scraper()
ob.processing()