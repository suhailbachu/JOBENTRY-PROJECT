from django.shortcuts import render, redirect

from prjctapp.models import Giver, JobVacancy, Seeker


def adminDash(request):


    return render(request,'admin/adminDash.html')


def adminJobVac(request):
    job_data = JobVacancy.objects.all()
    return render(request,"admin/job/job_vacancies.html",{"job_data":job_data})

def admin_giver_details(request):
    giver_data = Giver.objects.all()
    return render(request,"admin/admingiver/giverDetails.html",{"giver_data":giver_data})


def admin_seeker_details(request):
    seeker_data = Seeker.objects.all()
    return render(request,"admin/adminseeker/seekerDetails.html",{"seeker_data":seeker_data})


def seeker_admin_dlt(request,id):
    data = Seeker.objects.get(id=id)
    data.delete()
    return redirect("admin_seeker_details")

def giver_admin_dlt(request,id):
    data =Giver.objects.get(id=id)
    data.delete()
    return redirect("admin_giver_details")