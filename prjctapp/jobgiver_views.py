from django.contrib.auth.decorators import login_required
from django.db.transaction import commit
from django.shortcuts import redirect, render, get_object_or_404

from prjctapp.forms import LoginUser, GiverForm, JobsForm, messageForm
from prjctapp.jobSeeker_views import JobStatus
from prjctapp.models import Giver, JobVacancy, ApplyForJob, Message, StatusOfJob, Seeker
from project_main.asgi import application


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
# def request_applications(request,id):
#     user_data = request.user
#     status_data =Giver.objects.get(user=user_data)
#     job_data = JobVacancy.objects.get(id=id)
#     giver_data = Giver.objects.get(user=user_data)
#     obj= StatusOfJob.objects.filter(job_details__recruiter_details=status_data)
#     job_application = ApplyForJob.objects.filter(job_details=job_data)
#     application_data = StatusOfJob.objects.filter(job_details__recruiter_details=status_data)

    # return render(request,"jobgiver/applicationRequests.html",{"application_data":application_data,"job_data":job_data ,"obj":obj,"job_application":job_application})
def request_applications(request,id):
    applications = ApplyForJob.objects.all().select_related('job_details', 'seeker_details')
    return render(request, 'jobgiver/applicationRequests.html', {'applications': applications})


#
# def request_applications(request, id):
#     user_data = request.user
#     giver_data = Giver.objects.get(user=user_data)
#     job_data = JobVacancy.objects.get(id=id)
#
#     # Get all applications related to this job
#     job_applications = ApplyForJob.objects.filter(job_details=job_data)
#     print(job_applications)
#
#     # Status objects related to this giver/recruiter
#     status_objects = StatusOfJob.objects.filter(job_details__recruiter_details=giver_data)
#     print(job_applications)



    # return render(request, 'jobgiver/applicationRequests.html', {
    #     'job_data': job_data,
    #     'job_application': job_applications,
    #     'obj': status_objects,
    # })


@login_required(login_url="home")
def job_dlt(request,id):
    job_data =JobVacancy.objects.get(id=id)
    job_data.delete()
    return redirect("postedjobs")


# def Hired(request,id):
#     status_data = StatusOfJob.objects.get(id=id)
#     status_data.status = 1
#     status_data.save()
#     return redirect("request_applications")

def Hired(request, id):
    application = get_object_or_404(ApplyForJob, id=id)

    status, created = StatusOfJob.objects.get_or_create(
        job_details=application.job_details,
        seeker_details=application.seeker_details,
        defaults={'status': 1}
    )

    if not created:
        status.status = 1
        status.save()

    return redirect("request_applications", id=application.id)

def NotSelected(request, id):
    application = get_object_or_404(ApplyForJob, id=id)

    status, created = StatusOfJob.objects.get_or_create(
        job_details=application.job_details,
        seeker_details=application.seeker_details,
        defaults={'status': 2}
    )

    if not created:
        status.status = 2
        status.save()

    return redirect("request_applications", id=application.id)

# def Request_view(request):
#     user_data = request.user
#     status_data = Seller.objects.get(user=user_data)
#     obj = StatusOfProduct.objects.filter(product_details__seller_details=status_data)
#     return render(request, "seller/customerRequest.html",{"obj":obj})



def jobs_status(request,id):
    user_data = request.user
    job_data = JobVacancy.objects.all()
    seeker =Seeker.objects.get(user=user_data)
    jobs_status= StatusOfJob.objects.filter(seeker_details=seeker)
    return render(request,"jobSeeker/jobList.html",{"job_data": job_data,'jobs_status':jobs_status})
# def NotSelected(request,id):
#     status_data = StatusOfJob.objects.get(id=id)
#     status_data.status = 2
#     status_data.save()
#     return redirect("request_applications")




# def messagewithSeeker(request,id):
#     form = Message()
#     user_data = request.user
#     recruiter_data = Giver.objects.get(user=user_data)
#
#     status_data = StatusOfJob.objects.get(id=id)
#     seeker_data = status_data.seeker_details
#     job_data = status_data.job_details
#     message_data = Message.objects.filter(job_details=job_data)
#     if request.method == "POST":
#         message_form =  messageForm(request.POST)
#         if message_form.is_valid():
#             obj = message_form.save(commit=False)
#             obj.job_details = job_data
#             obj.seeker_details = seeker_data
#             obj.seller_details = recruiter_data
#             obj.save()
#             return  redirect("messagewithSeeker",id=id)
#         else:
#             print(message_form.errors)
#         print('hello')
#
#     return  render(request,"seller/chatWithCustomer.html",{"form":form,"message_data":message_data,'job_data':job_data, 'seeker_data':seeker_data})

