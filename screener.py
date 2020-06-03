import urllib.request
import configparser

# user_agent = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7'

# url = "https://finviz.com/chart.ashx?s=m&ty=c&t=ddog"
# headers={'User-Agent':user_agent,} 

# request=urllib.request.Request(url,None,headers) 
# response = urllib.request.urlopen(request)
# output = open("file01.png","wb")
# output.write(response.read())
# output.close()

configParser = configparser.RawConfigParser()
configParser.read('config.ini')

details_dict = dict(configParser.items('alphavantage_api'))
print(details_dict['url'])


