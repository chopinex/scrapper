from django.shortcuts import render
from django.http import HttpResponse
from .models import Trabajos

import requests
from bs4 import BeautifulSoup
from getpass import getpass

# Create your views here.
def hello(request):
    '''
    base_url='https://pe.computrabajo.com'
    HEADERS = {'User-Agent' :'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:47.0) Gecko/20100101 Firefox/47.0'}
    r = requests.get(base_url,headers=HEADERS)

    soup = BeautifulSoup(r.content, 'html.parser')
    s= soup.find_all('ul',class_='lS')

    content=[]
    for tags in s:
        content=content + tags.find_all('a')

    endpoints=[]
    for link in content:
        endpoints.append(link.get('href'))

    jobs=[]
    places=[]
    for ep in endpoints:
        r = requests.get(base_url+ep,headers=HEADERS)
        soup = BeautifulSoup(r.content, 'html.parser')

        ss=soup.find_all('article')
    
        for link in ss:
            jobs=jobs+link.find_all('h1')
            places=places+link.find_all('p',class_='fs16')

    Trabajos.objects.all().delete()

    for i in range(len(jobs)):
        pl=''.join(places[i].find_all(recursive=False,text=True)).strip()
        Trabajos(descripcion=jobs[i].text,lugar=pl).save()
    '''
    trabajos = Trabajos.objects.all()
    return render(request,'index.html',{'trabajos':trabajos})

