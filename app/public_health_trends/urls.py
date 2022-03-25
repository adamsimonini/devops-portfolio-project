"""public_health_trends URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import include, path

import api.api_views


urlpatterns = [
    path('admin/', admin.site.urls), 
    path('api/', include('api.urls')),
    # path('region/', api.api_views.RegionList.as_view()),
    # path('health_region/', api.api_views.HealthRegionList.as_view()),
    # path('diseases/', api.api_views.DiseasesList.as_view()),
    # path('weatherstations/', api.api_views.WeatherStationsList.as_view()),
    # path('province/', api.api_views.ProvinceList.as_view()),
    # path('api/disease/', include('api.urls')),
    # path('', admin.site.urls),
]
