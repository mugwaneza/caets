from django.http import request
from django.shortcuts import render, redirect

# Create your views here.
def Login (request):      #Admin Login

 # if request.session.get('admin_session'):
 #     return redirect("admin")
 # else:
    # logout(request)  # clear sessions that may be existing previously

    # if request.method == 'POST':
      # username = request.POST.get('username')
      # Iputpassword = request.POST.get('password')
      #
      #
      # if users.objects.filter(username=username).exists():   #when username is valid
      #
      #      user = users.objects.get(username=username)
      #      hashedpass = user.password
      #      userId = user.id
      #      firstname = user.first_name
      #
      #      if check_password(Iputpassword, hashedpass) :      #when username is valid and pasword is correct
      #          request.session['user_session'] = userId
      #          request.session['user'] = firstname
      #          return redirect("user")
      #      else:
      #           messages.error(request, 'Sorry invalid username or password  !')
      #           return render(request, 'admin_dashboard/login.html')
      #
      # else:
      #    messages.error(request, 'Sorry unknown username !')
      #    return render(request, 'admin_dashboard/login.html')

    # else:
     return render(request, 'admin_dashboard/login.html')

# def Logout(request):
#     logout(request)
#     return render(request, 'admin_dashboard/login.html')


def AddUser(request ):

 # if not request.session.get('user_session'):
 #    return render(request, 'admin_dashboard/login.html')
 #
 # else:
    # if request is not post, initialize an empty form
    if request.method == 'POST':

        dataDict = dict()

        # if users.objects.filter(email=request.POST.get('email')).exists():   #check if  email already exist
        #      messages.error(request, 'Email was already used')
        #      return HttpResponseRedirect('/add/user', dataDict)
        #
        # if users.objects.filter(username=request.POST.get('username')).exists():   #check if  username already exist
        #     messages.error(request, 'User name was already used')
        #     return HttpResponseRedirect('/add/user', dataDict)
        # else:
        #     # get form inputs and save it
        #     data = users()
        #     data.first_name = request.POST.get('firstname')
        #     data.last_name = request.POST.get('lastname')
        #     data.email = request.POST.get('email')
        #     data.username = request.POST.get('username')
        #     Plain_password = request.POST.get('password')
        #     data.password = make_password(Plain_password)
        #     data.save()
        #
        #     messages.success(request, 'Account was created successfully')
        #     return HttpResponseRedirect('/add/user',dataDict)
    else:

        # data = users.objects.filter().all()
        # paginator = Paginator(data, 10)
        # page_number = request.GET.get('page')
        # allusers = paginator.get_page(page_number)
        # while it is get method
        # return render(request, 'admin_dashboard/users.html', {'allusers' : allusers})
        return render(request, 'admin_dashboard/users.html', )



def AddMember(request ):

 # if not request.session.get('user_session'):
 #    return render(request, 'admin_dashboard/login.html')
 #
 # else:
    # if request is not post, initialize an empty form
    if request.method == 'POST':

        dataDict = dict()

        # if users.objects.filter(email=request.POST.get('email')).exists():   #check if  email already exist
        #      messages.error(request, 'Email was already used')
        #      return HttpResponseRedirect('/add/user', dataDict)
        #
        # if users.objects.filter(username=request.POST.get('username')).exists():   #check if  username already exist
        #     messages.error(request, 'User name was already used')
        #     return HttpResponseRedirect('/add/user', dataDict)
        # else:
        #     # get form inputs and save it
        #     data = users()
        #     data.first_name = request.POST.get('firstname')
        #     data.last_name = request.POST.get('lastname')
        #     data.email = request.POST.get('email')
        #     data.username = request.POST.get('username')
        #     Plain_password = request.POST.get('password')
        #     data.password = make_password(Plain_password)
        #     data.save()
        #
        #     messages.success(request, 'Account was created successfully')
        #     return HttpResponseRedirect('/add/user',dataDict)
    else:

        # data = users.objects.filter().all()
        # paginator = Paginator(data, 10)
        # page_number = request.GET.get('page')
        # allusers = paginator.get_page(page_number)
        # while it is get method
        # return render(request, 'admin_dashboard/users.html', {'allusers' : allusers})
        return render(request, 'admin_dashboard/members.html', )



def AddGuest(request ):

 # if not request.session.get('user_session'):
 #    return render(request, 'admin_dashboard/login.html')
 #
 # else:
    # if request is not post, initialize an empty form
    if request.method == 'POST':

        dataDict = dict()

        # if users.objects.filter(email=request.POST.get('email')).exists():   #check if  email already exist
        #      messages.error(request, 'Email was already used')
        #      return HttpResponseRedirect('/add/user', dataDict)
        #
        # if users.objects.filter(username=request.POST.get('username')).exists():   #check if  username already exist
        #     messages.error(request, 'User name was already used')
        #     return HttpResponseRedirect('/add/user', dataDict)
        # else:
        #     # get form inputs and save it
        #     data = users()
        #     data.first_name = request.POST.get('firstname')
        #     data.last_name = request.POST.get('lastname')
        #     data.email = request.POST.get('email')
        #     data.username = request.POST.get('username')
        #     Plain_password = request.POST.get('password')
        #     data.password = make_password(Plain_password)
        #     data.save()
        #
        #     messages.success(request, 'Account was created successfully')
        #     return HttpResponseRedirect('/add/user',dataDict)
    else:

        # data = users.objects.filter().all()
        # paginator = Paginator(data, 10)
        # page_number = request.GET.get('page')
        # allusers = paginator.get_page(page_number)
        # while it is get method
        # return render(request, 'admin_dashboard/users.html', {'allusers' : allusers})
        return render(request, 'admin_dashboard/guests.html', )

def AddDepartment(request ):

 # if not request.session.get('user_session'):
 #    return render(request, 'admin_dashboard/login.html')
 #
 # else:
    # if request is not post, initialize an empty form
    if request.method == 'POST':

        dataDict = dict()

        # if users.objects.filter(email=request.POST.get('email')).exists():   #check if  email already exist
        #      messages.error(request, 'Email was already used')
        #      return HttpResponseRedirect('/add/user', dataDict)
        #
        # if users.objects.filter(username=request.POST.get('username')).exists():   #check if  username already exist
        #     messages.error(request, 'User name was already used')
        #     return HttpResponseRedirect('/add/user', dataDict)
        # else:
        #     # get form inputs and save it
        #     data = users()
        #     data.first_name = request.POST.get('firstname')
        #     data.last_name = request.POST.get('lastname')
        #     data.email = request.POST.get('email')
        #     data.username = request.POST.get('username')
        #     Plain_password = request.POST.get('password')
        #     data.password = make_password(Plain_password)
        #     data.save()
        #
        #     messages.success(request, 'Account was created successfully')
        #     return HttpResponseRedirect('/add/user',dataDict)
    else:

        # data = users.objects.filter().all()
        # paginator = Paginator(data, 10)
        # page_number = request.GET.get('page')
        # allusers = paginator.get_page(page_number)
        # while it is get method
        # return render(request, 'admin_dashboard/users.html', {'allusers' : allusers})
        return render(request, 'admin_dashboard/departments.html', )


def ViewAttendance(request ):

 # if not request.session.get('user_session'):
 #    return render(request, 'admin_dashboard/login.html')
 #
 # else:
    # if request is not post, initialize an empty form
    if request.method == 'POST':

        dataDict = dict()

        # if users.objects.filter(email=request.POST.get('email')).exists():   #check if  email already exist
        #      messages.error(request, 'Email was already used')
        #      return HttpResponseRedirect('/add/user', dataDict)
        #
        # if users.objects.filter(username=request.POST.get('username')).exists():   #check if  username already exist
        #     messages.error(request, 'User name was already used')
        #     return HttpResponseRedirect('/add/user', dataDict)
        # else:
        #     # get form inputs and save it
        #     data = users()
        #     data.first_name = request.POST.get('firstname')
        #     data.last_name = request.POST.get('lastname')
        #     data.email = request.POST.get('email')
        #     data.username = request.POST.get('username')
        #     Plain_password = request.POST.get('password')
        #     data.password = make_password(Plain_password)
        #     data.save()
        #
        #     messages.success(request, 'Account was created successfully')
        #     return HttpResponseRedirect('/add/user',dataDict)
    else:

        # data = users.objects.filter().all()
        # paginator = Paginator(data, 10)
        # page_number = request.GET.get('page')
        # allusers = paginator.get_page(page_number)
        # while it is get method
        # return render(request, 'admin_dashboard/users.html', {'allusers' : allusers})
        return render(request, 'admin_dashboard/attendance.html', )


def ViewFinanceInfo(request ):

 # if not request.session.get('user_session'):
 #    return render(request, 'admin_dashboard/login.html')
 #
 # else:
    # if request is not post, initialize an empty form
    if request.method == 'POST':

        dataDict = dict()

        # if users.objects.filter(email=request.POST.get('email')).exists():   #check if  email already exist
        #      messages.error(request, 'Email was already used')
        #      return HttpResponseRedirect('/add/user', dataDict)
        #
        # if users.objects.filter(username=request.POST.get('username')).exists():   #check if  username already exist
        #     messages.error(request, 'User name was already used')
        #     return HttpResponseRedirect('/add/user', dataDict)
        # else:
        #     # get form inputs and save it
        #     data = users()
        #     data.first_name = request.POST.get('firstname')
        #     data.last_name = request.POST.get('lastname')
        #     data.email = request.POST.get('email')
        #     data.username = request.POST.get('username')
        #     Plain_password = request.POST.get('password')
        #     data.password = make_password(Plain_password)
        #     data.save()
        #
        #     messages.success(request, 'Account was created successfully')
        #     return HttpResponseRedirect('/add/user',dataDict)
    else:

        # data = users.objects.filter().all()
        # paginator = Paginator(data, 10)
        # page_number = request.GET.get('page')
        # allusers = paginator.get_page(page_number)
        # while it is get method
        # return render(request, 'admin_dashboard/users.html', {'allusers' : allusers})
        return render(request, 'admin_dashboard/finance_info.html', )