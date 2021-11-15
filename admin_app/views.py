from datetime import datetime
from django.contrib import messages
from django.contrib.auth import logout
from django.contrib.auth.hashers import make_password, check_password
from django.db.models import Q
from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from admin_app.Serializers import MembersSerializer, AttendanceSerializer

from admin_app.models import department, roles, guest_application, members_personalinfo, finance_info, profiles, users,attendance



# Create your views here.
def Login (request):      #Admin Login

 if request.session.get('admin_session'):
     return redirect("admin")
 else:
    logout(request)  # clear sessions that may be existing previously

    if request.method == 'POST':
      username = request.POST.get('username')
      Iputpassword = request.POST.get('password')


      if users.objects.filter(username=username).exists():   #when username is valid

           user = users.objects.get(username=username)
           hashedpass = user.password
           userId = user.id
           firstname = user.user.fname

           if check_password(Iputpassword, hashedpass) :      #when username is valid and pasword is correct
               request.session['admin_session'] = userId
               request.session['user'] = firstname
               return redirect("admin")
           else:
                messages.error(request, 'Sorry invalid username or password  !')
                return render(request, 'admin_dashboard/login.html')

      else:
         messages.error(request, 'Sorry unknown username !')
         return render(request, 'admin_dashboard/login.html')

    else:
     return render(request, 'admin_dashboard/login.html')

def Logout(request):
    logout(request)
    return render(request, 'admin_dashboard/login.html')

def FindMemberById(request, mid):

    member = MembersSerializer(members_personalinfo.objects.filter(Q(id=mid)) , many=True)

    return JsonResponse(member.data,  safe=False)


def AddUser(request ):

 if not request.session.get('admin_session'):
    return render(request, 'admin_dashboard/login.html')

 else:
    # if request is not post, initialize an empty form
    if request.method == 'POST':

        dataDict = dict()
        if users.objects.filter(username=request.POST.get('username')).exists():   #check if  username already exist
             messages.error(request, 'Username was already taken')
             return HttpResponseRedirect('/welcome/user', dataDict)
        else:
            # get form inputs and save it
            data = users()
            data.username = request.POST.get('firstname')
            data.username = request.POST.get('username')
            Plain_password = request.POST.get('password')
            data.password = make_password(Plain_password)
            data.user_id = request.POST.get('role')
            data.save()

            messages.success(request, 'Account was created successfully')
            return HttpResponseRedirect('/welcome/user',dataDict)
    else:

        data = users.objects.filter().all()
        paginator = Paginator(data, 10)
        page_number = request.GET.get('page')
        allregistered_admins = paginator.get_page(page_number)
        all_roles = MembersSerializer(members_personalinfo.objects.filter(~Q(role__rolename='Student')) , many=True)

        # while it is get method
        return render(request, 'admin_dashboard/users.html', {'all_roles' : all_roles, 'allregistered_admins' : allregistered_admins})



def AddMember(request ):

 if not request.session.get('admin_session'):
    return render(request, 'admin_dashboard/login.html')

 else:
    # if request is not post, initialize an empty form
    if request.method == 'POST':

        dataDict = dict()

        if members_personalinfo.objects.filter(email=request.POST.get('email')).exists():   #check if  email already exist
             messages.error(request, 'Email was already used')
             return HttpResponseRedirect('member', dataDict)

        if members_personalinfo.objects.filter(tel_no=request.POST.get('phoneno')).exists():   #check if  Phone number already exist
            messages.error(request, 'Phone number already used')
            return HttpResponseRedirect('member', dataDict)
        else:
            # get form inputs and save it
            data = members_personalinfo()
            data.role_id = request.POST.get('rolename')
            data.dept_id = request.POST.get('department')
            data.fname = request.POST.get('firstname')
            data.lname = request.POST.get('lastname')
            data.tel_no = request.POST.get('tel')
            data.email = request.POST.get('email')
            data.address = request.POST.get('address')
            data.save()
            #Save to mongo db user_id which is last inserted id in postgresql profile picture , comment etc
            obj = members_personalinfo.objects.latest('id')
            doc = profiles()
            doc.user_id= obj.pk;
            doc.image= request.FILES['profile']
            doc.save()


            messages.success(request, 'A member is successfully')
            return HttpResponseRedirect('member',dataDict)
    else:

        alldepts = department.objects.filter().all()
        allroles = roles.objects.filter().all()

        data = members_personalinfo.objects.filter().all()
        paginator = Paginator(data, 10)
        page_number = request.GET.get('page')
        allmembers = paginator.get_page(page_number)
        # while it is get method
        return render(request, 'admin_dashboard/members.html', {'allmembers' : allmembers, 'alldepts':alldepts, 'allroles':allroles})


def UpdateMemberById(request ):

 if not request.session.get('admin_session'):
    return render(request, 'admin_dashboard/login.html')

 else:
    # if request is not post, initialize an empty form
    if request.method == 'POST':

        dataDict = dict()


        mid = request.POST.get('mid')

        # get form inputs and update it

        # MyTable.objects.filter(pk=some_value).update(field1='some value')

        data = members_personalinfo.objects.get(id=mid);
        data.role_id = request.POST.get('rolename')
        data.dept_id = request.POST.get('department')
        data.fname = request.POST.get('firstname')
        data.lname = request.POST.get('lastname')
        data.tel_no = request.POST.get('tel')
        data.email = request.POST.get('email')
        data.address = request.POST.get('address')
        data.save()



        messages.success(request, 'A member successfully updated')
        return HttpResponseRedirect('member',dataDict)
    else:

        alldepts = department.objects.filter().all()
        allroles = roles.objects.filter().all()

        data = members_personalinfo.objects.filter().all()
        paginator = Paginator(data, 10)
        page_number = request.GET.get('page')
        allmembers = paginator.get_page(page_number)
        # while it is get method
        return render(request, 'admin_dashboard/members.html', {'allmembers' : allmembers, 'alldepts':alldepts, 'allroles':allroles})

def DeleteMemberById(request, mid ):

 if not request.session.get('admin_session'):
    return render(request, 'admin_dashboard/login.html')

 else:
    # if request is not post, initialize an empty form
    if request.method == 'POST':

        dataDict = dict()

        # get routes  objects  and delete it
        members_personalinfo.objects.filter(id=mid).delete();
        messages.warning(request, 'A member successfully deleted')
        return HttpResponseRedirect('member',dataDict)
    else:

        alldepts = department.objects.filter().all()
        allroles = roles.objects.filter().all()

        data = members_personalinfo.objects.filter().all()
        paginator = Paginator(data, 10)
        page_number = request.GET.get('page')
        allmembers = paginator.get_page(page_number)
        # while it is get method
        return render(request, 'admin_dashboard/members.html', {'allmembers' : allmembers, 'alldepts':alldepts, 'allroles':allroles})



def AddGuest(request ):

 if not request.session.get('admin_session'):
    return render(request, 'admin_dashboard/login.html')

 else:

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

            messages.success(request, 'Booking is created successfully')
            return HttpResponseRedirect('guest',dataDict)
    else:

        alldepts = department.objects.filter().all()
        allguests = guest_application.objects.filter().all()
        paginator = Paginator(allguests, 10)
        page_number = request.GET.get('page')
        allguests = paginator.get_page(page_number)
        # while it is get method
        return render(request, 'admin_dashboard/guests.html', {'alldepts' : alldepts, 'allguests':allguests})


def ApproveGuestById(request, id ):

 if not request.session.get('admin_session'):
    return render(request, 'admin_dashboard/login.html')

 else:

    if request.method == 'POST':

          dataDict = dict()
          data = guest_application.objects.filter(id=id).update(status='1')

          if data>0:

            attend = attendance()
            attend.guest_id = id
            attend.checkin_time = datetime.now()
            attend.save()

            messages.success(request, 'Application is  successfully approved')
            return HttpResponseRedirect('view/guest',dataDict)
    else:

        alldepts = department.objects.filter().all()
        allguests = guest_application.objects.filter().all()
        paginator = Paginator(allguests, 10)
        page_number = request.GET.get('page')
        allguests = paginator.get_page(page_number)
        # while it is get method
        return render(request, 'admin_dashboard/guests.html', {'alldepts' : alldepts, 'allguests':allguests})


def RejectGuestById(request, id ):

 if not request.session.get('admin_session'):
    return render(request, 'admin_dashboard/login.html')

 else:

    if request.method == 'POST':

          dataDict = dict()
          data = guest_application.objects.filter(id=id).update(status='-1')
          messages.info(request, 'Application is  successfully rejected')
          return HttpResponseRedirect('view/guest',dataDict)
    else:

        alldepts = department.objects.filter().all()
        allguests = guest_application.objects.filter().all()
        paginator = Paginator(allguests, 10)
        page_number = request.GET.get('page')
        allguests = paginator.get_page(page_number)
        # while it is get method
        return render(request, 'admin_dashboard/guests.html', {'alldepts' : alldepts, 'allguests':allguests})

def AddDepartment(request ):

 if not request.session.get('admin_session'):
    return render(request, 'admin_dashboard/login.html')
 else:
    # if request is not post, initialize an empty form
    if request.method == 'POST':

        dataDict = dict()
        if department.objects.filter(depname=request.POST.get('department')).exists():   #check if  department already exist
             messages.error(request, 'Department was already registered')
             return redirect('department')
        else:
            # get form inputs and save it
            data = department()
            data.depname = request.POST.get('department')
            data.description = request.POST.get('description')
            data.save()

            messages.success(request, 'Department was created successfully')
            return redirect('department')
    else:

        data = department.objects.filter().all()
        paginator = Paginator(data, 10)
        page_number = request.GET.get('page')
        alldepartments = paginator.get_page(page_number)

        return render(request, 'admin_dashboard/departments.html', {'alldepartments' : alldepartments} )

def AddRole(request ):

 if not request.session.get('admin_session'):
    return render(request, 'admin_dashboard/login.html')

 else:
    # if request is not post, initialize an empty form
    if request.method == 'POST':

        dataDict = dict()

        if roles.objects.filter(rolename=request.POST.get('rolename')).exists():   #check if  rolename already exist
             messages.error(request, 'role name was already registered')
             return redirect('role')
        else:
            # get form inputs and save it
            data = roles()
            data.rolename = request.POST.get('rolename')
            data.description = request.POST.get('description')
            data.save()

            messages.success(request, 'Role was created successfully')
            return redirect('role')
    else:

        data = roles.objects.filter().all()
        paginator = Paginator(data, 10)
        page_number = request.GET.get('page')
        allroles = paginator.get_page(page_number)
        return render(request, 'admin_dashboard/roles.html', {'allroles' : allroles} )


def ViewAttendance(request ):

 if not request.session.get('admin_session'):
    return render(request, 'admin_dashboard/login.html')

 else:


        all_attendees_checkedin = AttendanceSerializer(attendance.objects.filter(Q(checkout_time="")), many=True )
        all_attendees_checkedout = AttendanceSerializer(attendance.objects.filter(~Q(checkout_time="")), many=True )



        return render(request, 'admin_dashboard/attendance.html', {'all_attendees_checkedin' : all_attendees_checkedin, 'all_attendees_checkedout' : all_attendees_checkedout})

def ViewFinanceInfo(request ):

 # if not request.session.get('user_session'):
 #    return render(request, 'admin_dashboard/login.html')
 #
 # else:
    # if request is not post, initialize an empty form
    if request.method == 'POST':

        dataDict = dict()

        if finance_info.objects.filter(user_id=request.POST.get('student')).exists():   #check if student already exist
             messages.error(request, 'Student info already exist in finance, better update')
             return HttpResponseRedirect('/finance/info', dataDict)

        else:
            # get form inputs and save it
            data = finance_info()
            data.user_id = request.POST.get('student')
            data.paid_amount = request.POST.get('amount')
            data.balance = request.POST.get('balance')
            data.save()

            messages.success(request, 'Account was created successfully')
            return HttpResponseRedirect('/finance/info',dataDict)
    else:

        all_students = MembersSerializer(members_personalinfo.objects.filter(Q(role__rolename='Student')) , many=True)
        data = finance_info.objects.filter().all()
        paginator = Paginator(data, 10)
        page_number = request.GET.get('page')
        allfinance = paginator.get_page(page_number)
        # while it is get method

        return render(request, 'admin_dashboard/finance_info.html',{'allfinance': allfinance, 'all_students': all_students} )
        # return JsonResponse( all_students.data, safe=False)




def Test(request):

    message = members_personalinfo.objects.filter(id=1).delete()

    return  message