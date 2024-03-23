from django.core import validators
from django.shortcuts import render,HttpResponseRedirect
from enroll.forms import StudentRegistration
from enroll.models import User
from django.views.generic.base import TemplateView, RedirectView
# Create your views here.


class AddShowTemplateView(TemplateView):
    template_name = 'enroll/addAndShow.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        fm = StudentRegistration()
        stud = User.objects.all()
        context={'form':fm,'stu':stud}
        return context
    
    def post(self, request):
        fm = StudentRegistration(request.POST)
        if fm.is_valid():
            nm = fm.cleaned_data['name']
            em = fm.cleaned_data['email']
            pw = fm.cleaned_data['password']

            reg = User(name = nm, email=em, password=pw)
            reg.save()
            return HttpResponseRedirect('/')
            
# def add_show(request):
#     if request.method=='POST':

#         fm = StudentRegistration(request.POST)
#         if fm.is_valid():
#             nm=fm.cleaned_data['name']
#             em = fm.cleaned_data['email']
#             pw = fm.cleaned_data['password']

#             reg = User(name=nm,email=em,password=pw)
#             reg.save()
#             fm = StudentRegistration()
#     else:
#         fm = StudentRegistration()   
#     stud = User.objects.all()
#     return render(request,'enroll/addAndShow.html',{'form':fm,'stu':stud})


def delete_data(request,id):
    if request.method =="POST":
        data = User.objects.get(pk=id)
        data.delete()

        # all_stu = User.objects.all()
        # for i, User in enumerate(all_stu):
        #     User.st_id=i+1
        #     User.save()
    return HttpResponseRedirect("/")

def update_data(request,id):
    if request.method =="POST":
        stu_data = User.objects.get(pk=id)
        fm = StudentRegistration(request.POST,instance=stu_data)
        fm.save()
    else:
        stu_data = User.objects.get(pk=id)
        fm = StudentRegistration(instance=stu_data)
    return render(request,'enroll/updateStudents.html',{"form":fm})

