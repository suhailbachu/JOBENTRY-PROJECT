from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from prjctapp.models import JobVacancy, Giver, Seeker


# Create your views here.
def home(request):
    return render(request, 'index.html')

def jobs(request):
    return render(request,'jobs.html')
# def login(request):
#     return render(request,'login.html')

def dash(request):
    return render(request,'dashnew.html')
def reggiver(request):
    data = Giver.objects.all()
    return render(request,'jobgiver/registerGiver.html',{'data':data})


def regseeker(request):
    job_data = JobVacancy.objects.all()
    # nameFilter = NameFilter(request.GET, queryset=job_data)

    # product_data = nameFilter.qs
    return render(request,'jobSeeker/RegisterSeeker.html',{'job_data': job_data})


@login_required(login_url="home")
def jobMoreInfo(request,id):
    user_data =request.user
    seeker_data = Seeker.objects.get(user=user_data)
    job_data = JobVacancy.objects.filter(id=id)
    return render(request,'jobSeeker/jobMoreInfo.html',{"job_data":job_data,"seeker_data":seeker_data })

@login_required(login_url="home")
def jobList(request):
    user_data = request.user
    seeker_data = Seeker.objects.get(user=user_data)
    job_data = JobVacancy.objects.all()
    return render(request,'jobSeeker/jobList.html',{"seeker_data":seeker_data , "job_data":job_data})

@login_required(login_url="home")
def giverDash(request):
    return render(request,'jobgiver/giverdash.html')
@login_required(login_url="home")
def seekerDash(request):
    return render(request,'jobSeeker/seekerDash.html')


def login_page(request):
    if request.method =='POST':
        user1 = request.POST.get('uname')
        pass1 =request.POST.get('pass')
        user = authenticate(request,username=user1,password=pass1)
        if user is not None:
            login(request,user)
            if user.is_staff:
                return redirect('adminDash')
            elif user.is_jobgiver:
                return redirect('giverDash')
            elif user.is_jobseeker:
                return redirect('seekerDash')
            else:
                messages.info(request,'ivalid credentials')
    return render(request,'login.html')


def logout_view(request):
    logout(request)
    return redirect("/")
