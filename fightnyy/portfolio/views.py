from django.shortcuts import render
from .models import PortFolio
# Create your views here.
def portfolio(request):
    portfolios=PortFolio.objects
    return render(request,'portfolio/portfoliohome.html',{'portfolios':portfolios})