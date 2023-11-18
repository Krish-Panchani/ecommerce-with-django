"""
URL configuration for rrsolution project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path
from rrsolution import view

from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', view.home,name='home'),
    path('home/', view.home,name='home'),
    path('utilities/', view.utilities,name='utilities'),
    path('Investment/', view.Investment,name='Investment'),
    path('realEstate/', view.realEstate,name='realEstate'),
    path('accounts/', view.accounts,name='accounts'),
    path('insurance/', view.insurance,name='insurance'),
    path('accounts/', view.accounts,name='accounts'),
    path('about/', view.about,name='about'),
    path('process/', view.process,name='process'),
    path('contact/', view.contact,name='contact'),
    path('login/', view.login,name='login'),
    path('indpostcode/', view.indpostcode,name='indpostcode'),
    path('measurement/', view.measurement,name='measurement'),
    path('loaneligible/', view.loaneligible,name='loaneligible'),
    path('emicalculator/', view.emicalculator,name='emicalculator'),
    path('timezone/', view.timezone,name='timezone'),
    path('login/', view.login,name='login'),
    path('tdschart/', view.tdschart,name='tdschart'),
    path('isdcode/', view.isdcode,name='isdcode'),
    path('textile/', view.textileview,name='textile'),
    path('jewelry/', view.jewelryview,name='jewelry'),
    path('Vegitable/', view.Vegitableview,name='Vegitable'),
    path('other/', view.otherview,name='other'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)