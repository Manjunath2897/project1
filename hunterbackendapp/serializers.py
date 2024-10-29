from rest_framework import serializers
from .models import Enquiry,Internship, StudentFeedback

class EnquirySerializer(serializers.ModelSerializer):
    class Meta:
        model = Enquiry
        fields = '__all__'




class InternshipSerializer(serializers.ModelSerializer):
    class Meta:
        model = Internship
        fields = '__all__'

class StudentFeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentFeedback
        fields = '__all__'
