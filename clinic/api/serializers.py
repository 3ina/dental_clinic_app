from rest_framework import serializers
from clinic import models


class ClinicSerializer(serializers.ModelSerializer):


    class Meta:
        model = models.Clinic
        fields = "__all__"


class TestimonialSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Testimonial
        exclude = ("clinic",)

class DoctorSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Doctor
        exclude = ("clinic")