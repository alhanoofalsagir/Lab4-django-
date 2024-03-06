from django.shortcuts import render
from django.http import HttpResponse

# Tax rate variable
tax_rate = 15
tax=0.15

def default_view(request):
    return render(request, 'tax_app/default.html')

def anyNumber(request, number):
    total_price = float(number) * (1 + tax)
    return HttpResponse(f'The total is  {total_price}')

def tax_rate_view(request):
    return render(request, 'tax_app/tax_rate.html', {'tax_rate': tax_rate})
