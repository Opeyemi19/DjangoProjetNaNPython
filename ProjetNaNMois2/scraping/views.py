from django.shortcuts import render
from django.http import JsonResponse
import json
import requests
from requests import get
from bs4 import BeautifulSoup


# Create your views here.

def scrappe_view(request):

        url = 'https://www.matchendirect.fr/'
        response = get(url)
        html_soup = BeautifulSoup(response.text, 'html.parser')
        table = html_soup.find('div', attrs={'id': 'livescore'})

        mydata = []
        # mydata1 = []

        for row in table.findAll('div', attrs={'class': 'panel panel-info'}):
                a_desc = row.find('h3', attrs={'class': 'panel-title'}).get_text()
        
                # for el1 in row.findAll('th'):
                #     resultat1 = {}
                #     date_match = el1.find('th').get_text()
                #     resultat1['date_of'] = date_match
                #     mydata1.append(resultat1)

                for value in row.findAll('tr'):
                        result = {}
                        MyTime = value.find('td', attrs={'class': 'lm1'}).get_text()
                        Equip1 = value.find('span', attrs={'class': 'lm3_eq1'}).get_text()
                        Equip2 = value.find('span', attrs={'class': 'lm3_eq2'}).get_text()
                        ScorsMatch = value.find('span', attrs={'class': 'lm3_score'}).get_text()
                        # parier = el.find('a').attr('href').link
                        ParierMatch = value.find('a', href=True).get('href')
                        TypeMatch = value.find('td', attrs={'class': 'lm2'}).get_text()
                        ImageEquip1 = value.find('img', src=True).get('src')
                        
                        # for imagetag in row.findAll('span'):
                        #         ImageEquip1 = value.find('img', attrs={'class': 'hidden-xs'}).get('src')
                                

                        # for a in el.find_all('a', href=True):
                        #         print "Found the URL:", a['href']

                        result['myTime'] = MyTime
                        result['equip1'] = Equip1
                        result['equip2'] = Equip2
                        result['scorsMatch'] = ScorsMatch
                        result['parierMatch'] = ParierMatch
                        result['typeMatch'] = TypeMatch
                        # result['imageEquip1'] = ImageEquip1



                        mydata.append(result)
        data = (mydata)

        return JsonResponse(data, safe=False)# retourn du json
        # return render(request,'Scrapping/scrap2.html',{'result':data})


def scrap_view(request):
        return render(request,'Scrapping/scrap2.html')