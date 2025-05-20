from django.contrib.auth.models import AbstractUser

from django.db import models
from django.db.models import Model, DO_NOTHING


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
    recruiter_details =models.ForeignKey(Giver,on_delete=models.SET_NULL,null=True,blank=True)
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

class ApplyForJob(models.Model):
    job_details = models.ForeignKey(JobVacancy,on_delete=models.CASCADE)
    seeker_details = models.ForeignKey(Seeker,on_delete=models.CASCADE,null=True,blank=True)
    name = models.CharField(max_length=100)
    Email = models.EmailField()
    Resume = models.FileField()
    portifolio_link =models.CharField()
    cover_letter=models.TextField()

class Saved(models.Model):
    job_details = models.ForeignKey(JobVacancy,on_delete=models.DO_NOTHING)
    seeker_details = models.ForeignKey(Seeker,on_delete=models.DO_NOTHING)





class StatusOfJob(models.Model):
    job_details = models.ForeignKey(JobVacancy,on_delete=models.DO_NOTHING)
    seeker_details = models.ForeignKey(Seeker, on_delete=models.DO_NOTHING)
    status_choices = [
        (0, 'Pending'),
        (1, 'Hired'),
        (2, 'Not Selected'),
    ]
    status = models.IntegerField(choices=status_choices, default=0)





class Message(models.Model):
    job_details = models.ForeignKey(JobVacancy,on_delete=models.DO_NOTHING)
    seeker_details = models.ForeignKey(Seeker,on_delete=models.DO_NOTHING,null=True,blank=True)
    recruiter_details =models.ForeignKey(Giver,on_delete=models.DO_NOTHING,null=True,blank=True)
    recruiter_message = models.TextField(null=True,blank=True)
    seeker_message = models.TextField(null=True,blank=True)
    date = models.DateTimeField(auto_now=True)


