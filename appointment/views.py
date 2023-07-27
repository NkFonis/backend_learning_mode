from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework import serializers
from rest_framework.response import Response


# Create your views here.

class DoctorSerializer(serializers.ModelSerializer):
    specialty = serializers.CharField(max_length=255)

    def __str__(self) -> str:
        return self.specialty

class PatientSerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=100)
    email=serializers.EmailField()
    phone_number=serializers.IntegerField()
    date=serializers.DateTimeField(auto_now_add=True)
    choosen_time=serializers.DateTimeField()
    Sym_Des=serializers.CharField()


@api_view(['POST'])
def Patient(request):
    try:
        serializedata = PatientSerializer(data=request.data)

        if serializedata.is_valid():
            serializedata.save()
            return Response("Appointment Booked")
        
        else:
            return Response(serializedata.errors)
        
    except BaseException as e:
        return Response(str(e))