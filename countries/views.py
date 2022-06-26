from django.shortcuts import render
import requests

# Create your views here.
def home(request):
    return render(request, 'countries/home.html')

def wiki(request):
    data = requests.get("https://restcountries.com/v3.1/all").json()
    # countries_data = sorted(data.keys())
    return render(request, 'countries/countries.html',{'data':data,"total":len(data)})