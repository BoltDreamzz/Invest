from django.contrib import admin
from .models import Investment, InvestmentPlan, Property

# Register your models here.
admin.site.register(Property)
admin.site.register(InvestmentPlan)
admin.site.register(Investment)

