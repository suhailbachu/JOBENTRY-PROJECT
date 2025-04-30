from django.contrib.auth.decorators import login_required
from django.db.transaction import commit
from django.shortcuts import redirect, render

from prjctapp.forms import LoginUser, GiverForm, JobsForm
from prjctapp.models import Giver, JobVacancy, ApplyForJob

@login_required(login_url="home")
def postedjobs(request):
    user_data = request.user
    giver_data = Giver.objects.get(user=user_data)
    job_data = JobVacancy.objects.filter(recruiter_details=giver_data)
    return render(request,'jobgiver/postedJobs.html',{'job_data': job_data})



def giver_add(request):
    form1 = LoginUser()
    form2 = GiverForm()

    if request.method == 'POST':
        form1 =LoginUser(request.POST)
        form2 = GiverForm(request.POST,request.FILES)

        if form1.is_valid() and form2.is_valid():
            user = form1.save(commit=False)
            user.is_jobgiver = True
            user.save()
            user1 = form2.save(commit=False)
            user1.user = user
            user1.save()
            return redirect("/")

    return render(request, 'jobgiver/registerGiver.html', {"form1":form1, "form2":form2})

@login_required(login_url="home")
def add_jobs(request):
    user_data = request.user
    job_recruiter_data = Giver.objects.get(user=user_data)

    form = JobsForm()
    if request.method == 'POST':
        form1 = JobsForm(request.POST)
        if form1.is_valid():
            obj = form1.save(commit=False)
            obj.recruiter_details = job_recruiter_data
            obj.save()
            return redirect("giverDash")
    return render(request,'jobgiver/AddJobs.html',{'form':form})

@login_required(login_url="home")
def request_applications(request,id):
    user_data = request.user
    job_data = JobVacancy.objects.get(id=id)
    giver_data = Giver.objects.get(user=user_data)
    application_data = ApplyForJob.objects.filter(job_details__recruiter_details=giver_data)
    return render(request,"jobgiver/applicationRequests.html",{"application_data":application_data,"job_data":job_data})

@login_required(login_url="home")
def job_dlt(request,id):
    job_data =JobVacancy.objects.get(id=id)
    job_data.delete()
    return redirect("postedjobs")
