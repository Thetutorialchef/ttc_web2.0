from django.shortcuts import render


# Create your views here.

def portfolio(response):
    return render(response, "portfolio/portfolio.html", {})
