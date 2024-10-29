from django.urls import path
from .views import enquiry_view,InternshipList, StudentFeedbackList

urlpatterns = [
    path('api/enquiry', enquiry_view, name='enquiry'),
    path('api/internships/', InternshipList.as_view(), name='internship-list'),
    path('api/feedback/', StudentFeedbackList.as_view(), name='student-feedback-list'),
]
