from django.urls import path
from clinic import views

app_name = "clinic"
urlpatterns = [
    path("",views.index,name="home"),
    path("about/",views.about,name="about"),
    path("service/",views.service,name="service"),
    path("contact/",views.contact,name="contact"),
    path("pricing_plan/",views.pricing_plan,name="pricing_plan"),
    path("doctors/",views.dentist,name="doctors"),
    path("testimonial/",views.testimonial,name="testimonial"),
    path("appointment/",views.appointment,name="appointment"),
    path("appointment-page/",views.appointment_page,name="appointment_page"),
    path("doctors-search/",views.search,name="search"),
    path("contact_us/",views.contact_us,name="contact_us"),

]