from django.contrib import messages
from django.core.paginator import Paginator
from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from admin_app.models import guest_application, department


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
