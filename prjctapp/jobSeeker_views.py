from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.transaction import commit
from django.shortcuts import redirect, render, get_object_or_404

from prjctapp.forms import LoginUser, SeekerForm, ApplyForm
from prjctapp.models import Seeker, Saved, JobVacancy, Giver, Message, StatusOfJob, ApplyForJob


def seeker_add(request):
    form1 = LoginUser()
    form2 = SeekerForm()


    if request.method == "POST":
        form1 = LoginUser(request.POST)
        form2 = SeekerForm(request.POST,request.FILES)

        if form1.is_valid() and form2.is_valid():
            user = form1.save(commit=False)
            user.is_jobseeker = True
            user.save()
            user1 = form2.save(commit=False)
            user1.user = user
            user1.save()
            return  redirect("/")
    return render(request,'jobSeeker/RegisterSeeker.html',{"form1":form1 , "form2":form2})

@login_required(login_url="home")
def save(request):
    user_data = request.user
    seeker_data = Seeker.objects.get(user=user_data)
    save_data = Saved.objects.filter(seeker_details = seeker_data)
    return render(request,'jobSeeker/SavedJobs.html',{'save_data':save_data})


@login_required(login_url="home")
def addToSave(request,id):
    job_data = JobVacancy.objects.get(id=id)
    user_data = request.user
    seeker_data = Seeker.objects.get(user=user_data)
    saved_jobs = Saved.objects.filter(job_details = job_data,seeker_details = seeker_data)
    if saved_jobs.exists():
        messages.info(request,"this job is already Saved")
        return redirect("jobList")
    else:
        save_data = Saved()
        save_data.job_details = job_data
        save_data.seeker_details = seeker_data
        job_data.save()
        save_data.save()
        messages.info(request, "Job Saved")
        return redirect("jobList")
    return render(request,'jobSeeker/jobList.html')
@login_required(login_url="home")
def UnSave(request,id):
    job_data= Saved.objects.get(id=id)
    job_data.delete()
    messages.info(request,"Un Saved")
    return  redirect("save")

@login_required(login_url="home")
def apply_job(request,id):
    user_data = request.user

    job_data = JobVacancy.objects.get(id=id)
    seeker_data= Seeker.objects.get(user=user_data)

    form = ApplyForm()
    if request.method == 'POST':
        form = ApplyForm(request.POST,request.FILES)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.job_details = job_data
            obj.seeker_details = seeker_data
            obj.save()
            return redirect('jobList')
    return render(request,"jobSeeker/applyform.html",{'form':form , 'job_data':job_data})


def JobStatus(request,id):
    user_data = request.user
    seeker_data = Seeker.objects.get(user=user_data)
    job_data = JobVacancy.objects.get(id=id)
    status_data = StatusOfJob()
    status_data.job_details = job_data
    status_data.seeker_details = seeker_data
    status_data.save()
    return render('jobList',id=id)


def applied_jobs(request,id):
    seeker =request.user.seeker
    applications = ApplyForJob.objects.filter(seeker_details=seeker)
    return render(request,'jobSeeker/applied_jobs.html',{'applications':applications})
