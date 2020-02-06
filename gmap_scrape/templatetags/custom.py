from django import template
from bs4 import BeautifulSoup
import requests
import time
import datetime
import cgi
#from django.http import HttpResponse
#from .forms import DollarForm
#from django.shortcuts import render

register = template.Library()
'''
# カスタムタグとして登録する
@register.simple_tag
def multply(value1, value2):
    return value1 * value2
'''

now = datetime.datetime.now()
dt_now = now.strftime('%Y/%m/%d %H:%M:%S')
dollar = 44.5
#dollar = cgi.FieldStorage()
#dollar = request.POST.get('dollar')
#dollar = float(input('dollar:'))

#@register.simple_tag
#def dollar_form(request):
#    global dollar
#    dollar = cgi.FieldStorage()





@register.simple_tag
def print_dollar():
    global yen
    url = 'https://info.finance.yahoo.co.jp/fx/detail/?code=USDJPY=FX'#FXリアルタイム
    res = requests.get(url)
    soup = BeautifulSoup(res.text, 'html.parser')
    #この関数内のyenはグローバル関数だよと宣言
    yen = soup.find(id='USDJPY_detail_bid').text
    #yen2 = dollar * float(yen)
    #return 'hoge'+dt_now+'hoge'
    return '現在(' + dt_now + ')のレートは1ドル' + str(yen) + '円です。' 


@register.simple_tag
def print_yen():
    #dollar = request.POST.get('dollar')

    #url = 'https://info.finance.yahoo.co.jp/fx/detail/?code=USDJPY=FX'#FXリアルタイム
    #res = requests.get(url)
    #soup = BeautifulSoup(res.text, 'html.parser')
    #yen = soup.find(id='USDJPY_detail_bid').text
    yen2 = dollar * float(yen)
    return str(dollar) + 'ドルは' + str(yen2) + '円です。'




