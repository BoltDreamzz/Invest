from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.http import JsonResponse

from .models import InvestmentPlan, Property, Investment

# Create your views here.
def index(request):
    messages.success(request, "Hey bro whats up !")
    return render(request, "core/index.html")

def investmentPlans(request):
    messages.success(request, "Hey have you invested today ?")

    properties = Property.objects.all()
    plans = InvestmentPlan.objects.all()

    return render(request, "core/plans.html", {
        'plans': plans,
        'properties': properties,

    })
    
def plan_detail(request, property_id):
    property = get_object_or_404(Property, pk=property_id)
    
    return render(request, "core/plan_detail.html", {
        'property': property,
    })

def property_list(request):
    properties = Property.objects.all()
    return render(request, 'core/property_list.html', {'properties': properties})

def invest(request, property_id):
    property = get_object_or_404(Property, id=property_id)
    if request.method == 'POST':
        amount = request.POST['amount']
        Investment.objects.create(user=request.user, property=property, amount=amount)
        return JsonResponse({'message': 'Investment successful'}, status=200)
    return render(request, 'core/invest.html', {'property': property})


def blog(request):
    messages.success(request, "Get the latest updates")
    return render(request, "core/blog.html")
