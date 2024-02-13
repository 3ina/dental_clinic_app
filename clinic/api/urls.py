from django.urls import path
from clinic.api import views


urlpatterns = [
    path("testimonial/",views.TestimonialList.as_view(),name="testimonial-list"),
    path("testimonial/<int:pk>/", views.TestimonialRetrieve.as_view(), name="testimonial-retrieve"),
]