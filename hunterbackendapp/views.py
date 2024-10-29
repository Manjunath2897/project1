from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Enquiry
from .serializers import EnquirySerializer

@api_view(['POST'])
def enquiry_view(request):
    if request.method == 'POST':
        serializer = EnquirySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


from rest_framework import generics
from .models import Internship, StudentFeedback
from .serializers import InternshipSerializer, StudentFeedbackSerializer

class InternshipList(generics.ListCreateAPIView):
    queryset = Internship.objects.all()
    serializer_class = InternshipSerializer

class StudentFeedbackList(generics.ListCreateAPIView):
    queryset = StudentFeedback.objects.all()
    serializer_class = StudentFeedbackSerializer
