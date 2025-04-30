from django.urls import path
from prjctapp import views, jobgiver_views, jobSeeker_views, admin_views

urlpatterns = [
    path("",views.home,name='home'),
    path("dash",views.dash,name='dash'),
    path("jobs",views.jobs,name='jobs'),
    path("jobMoreInfo/<int:id>/",views.jobMoreInfo,name='jobMoreInfo'),
    path("loginpage",views.login,name="login"),
    path("reggiver",views.reggiver,name="reggiver"),
    path("regseeker",views.regseeker,name="regseeker"),

    #admin
    path("adminDash",admin_views.adminDash,name='adminDash'),
    path("adminJobVac",admin_views.adminJobVac,name="adminJobVac"),
    path("admin_giver_details",admin_views.admin_giver_details,name="admin_giver_details"),
    path("admin_seeker_details",admin_views.admin_seeker_details,name="admin_seeker_details"),
    path("giver_admin_dlt/<int:id>",admin_views.giver_admin_dlt, name="giver_admin_dlt"),
    path("seeker_admin_dlt/<int:id>", admin_views.seeker_admin_dlt, name="seeker_admin_dlt"),

#giver

    path("giverDash",views.giverDash,name='giverDash'),
    path("postedjobs",jobgiver_views.postedjobs,name="postedjobs"),
    path("job_dlt/<int:id>/",jobgiver_views.job_dlt,name="job_dlt"),
    path("seekerDash",views.seekerDash,name='seekerDash'),
    path("giver_add",jobgiver_views.giver_add,name='giver_add'),
    path("add_jobs",jobgiver_views.add_jobs, name="add_jobs"),
    path("jobList",views.jobList,name="jobList"),
    path("save",jobSeeker_views.save,name="save"),
    path("UnSave/<int:id>/",jobSeeker_views.UnSave,name="UnSave"),
    path("addToSave/<int:id>/",jobSeeker_views.addToSave, name="addToSave"),
    path("apply_job/<int:id>/",jobSeeker_views.apply_job,name="apply_job"),
    path("request_applications/<int:id>/",jobgiver_views.request_applications,name='request_applications'),
    path("seeker_add",jobSeeker_views.seeker_add,name="seeker_add"),
    path("login_page",views.login_page,name="login_page"),

    path("logout",views.logout_view,name="logout")

    ]