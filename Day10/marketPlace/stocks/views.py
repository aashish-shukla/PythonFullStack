from django.http import HttpResponse
from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Stock, Portfolio
from .serializers import StockSerializer, PortfolioSerializer

# # Create your views here.
# import requests
#
# headers = {
#     'Content-Type': 'application/json'
# }
#
#
# requestResponse = requests.get("https://api.tiingo.com/tiingo/daily/aapl?token=fced443141e501d554d0b38c4a34bba085172b1e", headers=headers )
# print(requestResponse.json())

# def fun(request) :
#     page  = '''
#     <!DOCTYPE html>
# <html lang="en">
# <head>
#     <meta charset="UTF-8">
#     <title>Title</title>
# </head>
# <body>
# <h1>Stock Market App</h1>
# <p>Lorem ipsum dolor sit amet, consectetur adipisicing elit. Blanditiis commodi dignissimos dolor, ducimus enim harum in ipsum iure laboriosam minus, natus odit officiis omnis optio quibusdam quo, sapiente sunt voluptatibus!</p>
# <ul>
#     <li>s1</li>
#     <li>s2</li>
#     <li>s3</li>
# </ul>
# </body>
# </html>
#     '''
#     return  HttpResponse(page)

def fun(request) :
    return render(request ,  'index.html')

def fun1(request) :
    return render(request ,  'market.html')

# New API views
class StockViewSet(viewsets.ModelViewSet):
    queryset = Stock.objects.all()
    serializer_class = StockSerializer

class PortfolioViewSet(viewsets.ModelViewSet):
    queryset = Portfolio.objects.all()
    serializer_class = PortfolioSerializer

@api_view(['GET'])
def api_overview(request):
    api_urls = {
        'Stocks List': '/api/stocks/',
        'Stock Detail': '/api/stocks/{id}/',
        'Portfolio List': '/api/portfolio/',
        'Portfolio Detail': '/api/portfolio/{id}/',
    }
    return Response(api_urls)