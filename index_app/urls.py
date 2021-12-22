from django.urls import path
from index_app.views import Home, Booking, About, SearchBooking, ClientChatPost, Test


urlpatterns =[

path('', Home,name='home'),
path('booking', Booking,name='booking'),
path('search/booking', SearchBooking,name='searchb'),
path('client/chat/post', ClientChatPost,name='chatpost'),
path('test', Test,name='test'),

]