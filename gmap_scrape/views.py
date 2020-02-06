from django.shortcuts import render, redirect
import datetime
from django.http.response import HttpResponse
from .forms import DollarForm
from bs4 import BeautifulSoup
import requests
import time
# Create your views here.
def index(request):
    now = datetime.datetime.now()
    url = 'https://info.finance.yahoo.co.jp/fx/detail/?code=USDJPY=FX'#FXリアルタイム
    res = requests.get(url)
    soup = BeautifulSoup(res.text, 'html.parser')
    yen = soup.find(id='USDJPY_detail_bid').text
    dollar = request.POST.get('dollar') or 1.0 #! 左がFalseだったら右を返す
                            #? ⬆ dollarはmodels.pyのフォーム
    variable = {
    #'form': DollarForm(),
    'get': request.POST.get('dollar') or 1.0,
    'yen': soup.find(id='USDJPY_detail_bid').text,
    'kekka': float(dollar) * float(yen),
    'dt_now': now.strftime('%Y/%m/%d %H:%M:%S')
    }
    return render(request, 'gmap_scrape/index.html', variable)

def form(request):
    form = DollarForm(request.POST)  
    return render(request, 'gmap_scrape/form.html', {'form': form})

#def form(request):
    

#def index(request):
#    form = DollarForm()
#    return render(request, 'gmap_scrape/index.html', {'form': form})


