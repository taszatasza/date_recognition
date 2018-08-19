#!/usr/bin/python
# coding=utf-8
import math
import re

def date_recogniotion(text):

    for key, value in {'a':'ą','e':'ę','z':'ź','z':'ż','c':'ć','s':'ś','o':'ó','n':'ń','l':'ł'}.items():
    	text=text.replace(value,key)
    #print ('Przeszukiwany tekst: ', text)

    tab_slow = text.split(" ")

    slownik = {1:['^jeden$', 'pierwsz','styczen', 'stycznia'], 2:['^dwa$', 'dwu','drugi','luty', 'lutego'], 3:['^trzy$', 'trzeci','marzec', 'marca'], 4:['^cztery$', 'czwart','kwiecien', 'kwietnia'], 5:['^piec$', 'piat','maj', 'maja'], 6:['^szesc$', 'szost','czerwiec', 'czerwca'], 7:['^siedem$', 'siodm','lipiec', 'lipca'], 8:['^osiem$', 'osm','sierpien', 'sierpnia'], 9:['^dziewiec$', 'dziewiat','wrzesien', 'wrzesnia'],\
    11:['jedenascie', 'jedenast','listopad', 'listopada'], 12:['dwanascie', 'dwunast','grudzien', 'grudnia'], 13:['trzynascie', 'trzynast'], 14:['czternascie', 'czternast'], 15:['pietnascie', 'pietnast'], 16:['szesnascie', 'szesnast'], 17:['siedemnascie', 'siedemnast'], 18:['osiemnascie', 'osiemnast'], 19:['dziewietnascie', 'dziewietnast'],\
    10:['dziesiec', 'dziesiat','pazdziernik', 'pazdziernika'], 20:['dwadziescia', 'dwudziest'], 30:['trzydziesci', 'trzydziest'], 40:['czterdziesci', 'czterdziest'], 50:['piecdziesiat'], 60:['szescdziesiat'], 70:['siedemdziesiat'], 80:['osiemdziesiat'], 90:['dziewiecdziesiat'],\
    100:['sto', 'setn'], 200:['dwiescie', 'dwusetn'], 300:['trzysta', 'trzysetn'], 400:['czterysta', 'czterysetn'], 500:['piecset', 'piecsetn'], 600:['szescset', 'szescsetn'], 700:['siedemset', 'siedemsetn'], 800:['osiemset', 'osiemsetn'], 900:['dziewiecset', 'dziewiecsetn'],\
    1000:['tysiac', 'tysiace', 'tysieczn']}

    wzorzec = r'jeden\b|pierwsz|styczen|stycznia|dwa\b|dwu\b|drugi|luty|lutego|trzy\b|trzeci|marzec|marca|cztery\b|czwart|kwiecien|kwietnia|piec\b|piat|maj|maja|szesc\b|szost|czerwiec|czerwca|siedem\b|siodm|lipiec|lipca|osiem\b|osm|sierpien|sierpnia|dziewiec\b|dziewiat|wrzesien|wrzesnia|\
    |jedenascie|jedenast|listopad|listopada|dwanascie|dwunast|grudzien|grudnia|trzynascie|trzynast|czternascie|czternast|pietnascie|pietnast|szesnascie|szesnast|siedemnascie|siedemnast|osiemnascie|osiemnast|dziewietnascie|dziewietnast|\
    |dziesiec|dziesiat|pazdziernik|pazdziernika|dwadziescia|dwudziest|trzydziesci|trzydziest|czterdziesci|czterdziest|piecdziesiat|szescdziesiat|siedemdziesiat|osiemdziesiat|dziewiecdziesiat|\
    |sto|setn|dwiescie|dwusetn|trzysta|trzysetn|czterysta|czterysetn|piecset|piecsetn|szescset|szescsetn|siedemset|siedemsetn|osiemset|osiemsetn|dziewiecset|dziewiecsetn|\
    |tysiac|tysiace|tysieczn'

    wz = re.compile(wzorzec)
    tab_dopasowanie=[]
    tab_dopasowanie = re.findall(wz, text)
    #print('Dopasowane slowa: ', tab_dopasowanie)

    tab=[]
    day=0
    month=0
    year=0

    for i in tab_dopasowanie:
    	data_czesc=""
    	for key, value in slownik.items():
    			for s in value:
    				if re.match(s,i):
    						data_czesc=key
    	tab.append(data_czesc)
    #print ('tab = ', tab)

    if (tab[0]>=20 and tab[0]<=31):
        day = tab[0]+tab[1]
        month = tab[2]
    else:
        day = tab[0]
        month = tab[1]

    for i in range(len(tab)):
        if (tab[i]==1000):
            if (tab[tab.index(1000)-1]==2):
                year=tab[i]*tab[i-1]
                for z in range(i+1,len(tab)):
    				year=year+tab[z]
            else:
                year=tab[i]
                for z in range(i+1,len(tab)):
                    year=year+tab[z]

        elif (tab[i]==19):
            if tab[-1]!=19 and tab[0]!=19:
                year=tab[i]*100
                for z in range(i+1,len(tab)):
                    year=year+tab[z]

        elif (tab[i]==20):
            if tab[-1]!=20 and tab[0]!=20:
                year=tab[i]*100
                for z in range(i+1,len(tab)):
                    year=year+tab[z]

    #print str(day)+","+str(month)+","+str(year)

    wynik = {'day':day, 'month':month, 'year':year}
    print wynik
