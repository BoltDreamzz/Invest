from django.urls import path

from . import views

app_name = "core"

urlpatterns = [
    path("", views.index, name="index"),
    path("plans/", views.investmentPlans, name="plans"),
    path("blog/", views.blog, name="blog"),

    # 
    path("plan-detail/<int:property_id>/", views.plan_detail, name="plan_detail"),
    # path("splash/", views.splash, name="splash"),
]












