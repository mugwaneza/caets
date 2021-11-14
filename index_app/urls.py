from django.urls import path
from index_app.views import Home, Booking, About, SearchBooking


urlpatterns =[

path('', Home,name='home'),
path('booking', Booking,name='booking'),
path('search/booking>', SearchBooking,name='searchb'),

]