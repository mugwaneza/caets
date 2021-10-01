from django.urls import path
from index_app.views import Home


urlpatterns =[

path('', Home,name='home'),

]