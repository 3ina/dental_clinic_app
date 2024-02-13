from rest_framework import serializers
from clinic import models


class ClinicSerializer(serializers.ModelSerializer):


    class Meta:
        model = models.Clinic
        fields = "__all__"