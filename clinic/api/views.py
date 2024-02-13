from rest_framework import generics
from clinic.api import serializers as ser


class TestimonialList(generics.ListAPIView):
    serializer_class = ser.TestimonialSerializer


class TestimonialRetrieve(generics.RetrieveAPIView):
    serializer_class = ser.TestimonialSerializer

