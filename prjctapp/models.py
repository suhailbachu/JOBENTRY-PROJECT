from django.contrib.auth.models import AbstractUser

from django.db import models
from django.db.models import Model


# Create your models here.
class LoginView(AbstractUser):
    is_jobseeker = models.BooleanField(default=False)
    is_jobgiver = models.BooleanField(default=False)



class Giver(models.Model):
    user = models.ForeignKey(LoginView,on_delete = models.CASCADE,related_name='giver')
    name = models.CharField(max_length=50)
    email = models.EmailField()
    phone_no = models.CharField()
    profile_pic = models.FileField(upload_to='documents/')

    def __str__(self):
        return self.name

class Seeker(models.Model):
    user =models.ForeignKey(LoginView,on_delete = models.CASCADE,related_name='seeker' )
    name= models.CharField(max_length=50)
    email = models.EmailField()
    contact_no= models.CharField()
    profile_pic = models.FileField(upload_to='documents/')


    def __str__(self):
        return self.name



class JobVacancy(models.Model):
    recruiter_details =models.ForeignKey(Giver,on_delete=models.CASCADE)
    job_name = models.CharField(max_length=100)
    job_location = models.CharField(max_length=150)
    job_posted_date = models.DateField(auto_now=True)
    job_time_shift =models.CharField(max_length=50)
    job_discription = models.TextField()
    responsibilities = models.TextField()
    qualifications = models.TextField()
    experience_requiered = models.TextField()
    company_details =models.TextField()
    salary = models.CharField(max_length=15)


class Saved(models.Model):
    job_details = models.ForeignKey(JobVacancy,on_delete=models.DO_NOTHING)
    seeker_details = models.ForeignKey(Seeker,on_delete=models.DO_NOTHING)


class ApplyForJob(models.Model):
    job_details = models.ForeignKey(JobVacancy,on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    Email = models.EmailField()
    Resume = models.FileField()
    portifolio_link =models.CharField()
    cover_letter=models.TextField()