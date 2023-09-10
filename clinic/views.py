from django.conf import settings
from django.shortcuts import render
from .models import Clinic , Doctor , Service , Testimonial
from django.views.decorators.http import require_POST
from django.core.mail import send_mail, get_connection
from django.contrib import messages
import re
# Create your views here.


def index(req):
    clinic = Clinic.objects.get(name="den_clinic")
    all_doctor = Doctor.objects.all()
    doctors = Doctor.objects.all()[:1]
    times = clinic.time_opening.all()
    services = Service.objects.all()
    about = clinic.about.get(clinic__name="den_clinic")
    testmonials = Testimonial.objects.all()
    index = True
    context = {
        "clinic" : clinic,
        "doctors" : doctors,
        "times" : times,
        "services" : services,
        "about" : about,
        "testimonials" : testmonials,
        "index" : index,
        "all_doctor" : all_doctor,

    }

    return render(req, 'clinic/index.html', context)


def about(req):
    clinic = Clinic.objects.get(name="den_clinic")
    about = Clinic.objects.get(name="den_clinic").about.get()
    about_active = True

    context = {
        "about":about,
        "clinic" : clinic,
        "about_active" : about_active
    }

    return render(req, 'clinic/about.html', context)


def service(req):

    clinic = Clinic.objects.get(name="den_clinic")
    services = Service.objects.all()
    service_active = True
    context = {
        "clinic" : clinic,
        "services" : services,
        "service_active" : service_active
    }

    return  render(req, "clinic/services.html",context=context)


def contact(req):
    clinic = Clinic.objects.get(name="den_clinic")
    contact_active = True
    context = {
        'clinic' : clinic,
        "contact_active" : contact_active
    }

    return  render(req,'clinic/contact.html',context)


def pricing_plan(req):
    clinic = Clinic.objects.get(name="den_clinic")
    services = Service.objects.all()

    context = {
        'clinic':clinic,
        'services' : services,
        'pages' : True,
        'pricing_plan_active' :True
    }

    return render(req,"clinic/pricing_plan.html",context)


def dentist(req):
    clinic = Clinic.objects.get(name="den_clinic")
    doctors = Doctor.objects.all()
    context = {
        "clinic":clinic,
        "doctors" : doctors,
        'pages' : True,
        'our_dentist_active' : True
    }
    return render(req,"clinic/dentist.html",context)

def testimonial(request):
    clinic = Clinic.objects.get(name="den_clinic")
    testmonials = Testimonial.objects.all()
    context = {
        "clinic" : clinic,
        "testmonials":testmonials,
        "pages" : True,
        'testimonial_active' : True
    }
    return render(request,"clinic/testimonial.html",context)


@require_POST
def appointment(request):

    service_id = request.POST['service_id']
    service_name = Service.objects.get(pk=service_id).name
    doctor_id = request.POST['doctor_id']
    doctor_name = Doctor.objects.get(pk=doctor_id).name
    name = request.POST['name']
    email = request.POST['email']
    date = request.POST['date']
    time = request.POST['time']
    regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'

    clinic = Clinic.objects.get(name="den_clinic")
    context = {
        "clinic": clinic,

    }

    if re.fullmatch(regex, email):
        text = f"""
            name : {name}
            email : {email}
            service : {service_name}
            doctor  : {doctor_name}
            date  : {date}
            time : {time}
            
        """

        send_mail("appointment",text,"3inaroydl@gmail.com",("dentalapp109@gmail.com",))
        messages.success(request,"your message is send , we will call you soon")
        return render(request, 'clinic/email_sending.html', context)
    else:
        messages.error(request, "message doesn't send ")
        return render(request, 'clinic/email_sending.html', context)



def appointment_page(request):

    if request.method == "POST":
        appointment(request)
    elif request.method == "GET":
        clinic = Clinic.objects.get(name="den_clinic")
        context = {"clinic": clinic,
                   "doctors": Doctor.objects.all(),
                   "services" : Service.objects.all(),
                   "pages" : True,
                   "appointment_page_active" : True
                   }
        return render(request,'clinic/appointment.html',context)


def search(request):
    service_id = request.POST['service_id']
    service_name = Service.objects.get(pk=service_id)
    doctors = Doctor.objects.filter(services__name=service_name)
    clinic = Clinic.objects.get(name="den_clinic")
    context = {
        "clinic": clinic,
        "doctors": doctors
    }
    return render(request, "clinic/dentist.html", context)


def contact_us(request):
    name =request.POST['name']
    email = request.POST['email']
    subject = request.POST['subject']
    message = request.POST['message']
    clinic = Clinic.objects.get(name="den_clinic")
    context = {
        "clinic": clinic,

    }

    regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'

    if re.fullmatch(regex, email):
        text = f"""
            name : {name}
            email : {email}
            message : {message}

        """

        send_mail(f"{subject}", text, "3inaroydl@gmail.com", ("dentalapp109@gmail.com",))
        messages.success(request, "your message is send , we will call you soon")
        return render(request, 'clinic/email_sending.html', context)
    else:
        messages.error(request, "message doesn't send ")
        return render(request, 'clinic/email_sending.html', context)



