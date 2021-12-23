from django.urls import path
from admin_app.views import Test
from index_app.views import Home, Booking, About, SearchBooking, ClientChatPost


urlpatterns =[

path('', Home,name='home'),
path('booking', Booking,name='booking'),
path('search/booking', SearchBooking,name='searchb'),
path('client/chat/post', ClientChatPost,name='chatpost'),
path('test', Test,name='test'),

]