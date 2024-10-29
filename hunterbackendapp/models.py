from django.db import models

class Enquiry(models.Model):
    ENQUIRY_CHOICES = [
        ('Knowledge', 'Knowledge'),
        ('Jobs', 'Jobs'),
        ('HRMS', 'HRMS'),
    ]
    
    full_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    enquiry_regarding = models.CharField(max_length=50, choices=ENQUIRY_CHOICES)  # Added choices here
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.full_name




class Internship(models.Model):
    id = models.AutoField(primary_key=True)  # Primary key for the Internship table
    course_name = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    duration = models.CharField(max_length=50)
    course_type = models.CharField(max_length=50)

    def __str__(self):
        return self.course_name

class StudentFeedback(models.Model):
    student_feedback_id = models.AutoField(primary_key=True)  # Primary key for the StudentFeedback table
    student_name = models.CharField(max_length=100)
    feedback = models.TextField()

    def __str__(self):
        return self.student_name
