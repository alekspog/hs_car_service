"""hypercar URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from tickets.views import WelcomeView
from tickets.views import MenuView
from tickets.views import ChangeOilView, InflateTiresView, DiagnosticView
from tickets.views import ProcessingView, NextView


urlpatterns = [
    path('', WelcomeView.as_view(), name='welcome'),
    path('welcome/', WelcomeView.as_view(), name='welcome'),
    path('menu/', MenuView.as_view(), name='menu'),
    path('get_ticket/change_oil/', ChangeOilView.as_view(), name='change_oil'),
    path('get_ticket/inflate_tires/', InflateTiresView.as_view(), name='inflate_tire'),
    path('get_ticket/diagnostic/', DiagnosticView.as_view(), name='diagnostic'),
    path('processing', ProcessingView.as_view(), name='processing'),
    path('next/', NextView.as_view(), name='next'),
]
