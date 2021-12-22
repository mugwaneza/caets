from django.contrib import messages
from django.contrib.staticfiles.storage import staticfiles_storage
from django.core.paginator import Paginator
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, redirect
from django.templatetags.static import static
from django.utils.crypto import get_random_string
import os

# Create your views here.
import gnupg
from pprint import pprint
from admin_app.models import guest_application, department
from caets.settings import BASE_DIR
from index_app.models import visitor_chat, visitor_chat_message


def Home(request ):

        return render(request, 'index.html', )

def About(request ):

        return render(request, 'about.html', )


def Booking(request ):


    if request.method == 'POST':

            dataDict = dict()
            data = guest_application()
            data.dept_id = request.POST.get('department')
            data.fullname = request.POST.get('fullname')
            data.village = request.POST.get('village')
            data.sector = request.POST.get('sector')
            data.district = request.POST.get('district')
            data.tel_no = request.POST.get('tel')
            data.nid = request.POST.get('nid')
            data.visit_reason = request.POST.get('visit_reason')
            data.save()

            messages.success(request, 'Booking is sent successfully')
            return HttpResponseRedirect('booking',dataDict)
    else:

        alldepts = department.objects.filter().all()
        allguests = guest_application.objects.filter().all()
        paginator = Paginator(allguests, 10)
        page_number = request.GET.get('page')
        allguests = paginator.get_page(page_number)
        # while it is get method
        return render(request, 'external_guest_application.html', {'alldepts' : alldepts, 'allguests':allguests})


def SearchBooking(request ):

        phone = request.POST.get('search')

        searchres = guest_application.objects.filter(tel_no= phone)

        return render(request, 'searchresults.html', {'searchres' : searchres})


def ClientChatPost(request ):


    if request.method == 'POST':

        #Save user chat name and email
        visitorchat = visitor_chat()
        visitorchat.names = request.POST.get('name')
        visitorchat.email = request.POST.get('email')
        visitorchat.save()   #Save to visitor chat table
        done_by = visitor_chat.objects.latest('id')  #Get the user last inserted id

        # gpg = gnupg.GPG(gnupghome='C:/Users/alexis.mugwaneza/Desktop/crypto/')
        # gpg.encoding = 'utf-8'
        # Pphrase = get_random_string(length=32)
        #
        # input_data = gpg.gen_key_input(key_type="RSA", key_length=1024, name_email='testgpguser@mydomain.com',
        # passphrase=Pphrase)    #Specifying parameters while creating the key

        # keyids = gpg.gen_key(input_data)   # generate PKI Key
        # ascii_armored_public_keys = gpg.export_keys(keyids) # same as gpg.export_keys(keyids, False)
        # ascii_armored_private_keys = gpg.export_keys(keyids, True) # True => private keys
        #

        #Save user chat encrypted message
        visitorchatmessage =  visitor_chat_message()

        gpg = gnupg.GPG(gnupghome='C:/Users/alexis.mugwaneza/Desktop/crypto')

        unencrypted_string = 'Who are you? How did you get in my house?'
        encrypted_data = gpg.encrypt(unencrypted_string, 'testgpguser@mydomain.com')
        encrypted_string = str(encrypted_data)
        print ( 'encrypted string well: ', encrypted_string)

        message = request.POST.get('message')
        email =   request.POST.get('email')

        # encrypted_data = gpg.encrypt(message, email) # Encrypt a string
        # encrypted_mess = str(encrypted_data)

        visitorchatmessage.posted_by_id = done_by
        visitorchatmessage.encrypted_message = encrypted_string
        visitorchatmessage.encrypted_file_path = 'C:/Users/alexis.mugwaneza/Desktop/crypto'
        visitorchatmessage.save()



        return redirect('chatpost')

        #Pass chat info to the database

    else:
    #
    #
    #
    #     # return HttpResponse(import_result.results)
        return render(request, 'index.html')



def Test(request):

    gpg = gnupg.GPG(gnupghome='C:/Users/alexis.mugwaneza/Desktop/crypto')
    unencrypted_string = 'Who are you? How did you get in my house?'
    encrypted_data = gpg.encrypt(unencrypted_string, 'testgpguser@mydomain.com')
    encrypted_string = str(encrypted_data)
    print( 'ok: ', encrypted_data.ok)
    print ( 'status: ', encrypted_data.status)
    print ( 'stderr: ', encrypted_data.stderr)
    print ( 'unencrypted_string: ', unencrypted_string)
    print ( 'encrypted_string: ', encrypted_string)

    return render(request, 'index.html')
