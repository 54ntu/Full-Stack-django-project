from django.shortcuts import render,redirect
from .models import Task
from .forms import todoAppForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

from django.views import View
from django.contrib.auth import login,logout,authenticate


class LoginView(View):
    def get(self,request):
        return render(request,'LoginPage.html')
    
    def post(self,request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('index')
        return redirect('login')



class RegisterView(View):
    def get(self,request):
        return render(request,'registrationPage.html')
    
    def post(self,request):
        first_name = request.POST.get('firstname')
        last_name =request.POST.get('lastname')
        email    = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')

        try:
            user = User.objects.create_user(first_name=first_name,last_name=last_name,email=email,username=username,password=password)
            if user is not None: # this line of code will check the previous available user or not
                user.is_active=True
                user.save()
                return redirect('login')
            return redirect('register')
        except:
            return redirect('register')
        


class LogoutView(View):
    def get(self,request):
        logout(request)
        return redirect('login')



# Create your views here.
@login_required(login_url='/login')
def index(request):
    task_obj = Task.objects.all()
    context = {
        "task": task_obj
    }
    return render(request,'ListItem.html',context)



@login_required(login_url='/login')
def taskCreate(request):
    form = todoAppForm()
    print("task details : ",form)
    context = {"form":form}
    if request.method =="POST":
        task_obj = Task() #this line will create the object of task model
        task_obj.title = request.POST.get('title')
        task_obj.description = request.POST.get('description')
        task_obj.created = request.POST.get('created')
        task_obj.user = request.user
        print('user name : ', task_obj.user)
        task_obj.save()
        return redirect('index')
    return render(request,'taskCreate.html',context)



@login_required(login_url='/login')
def detailPage(request,id):
    task_obj = Task.objects.get(id=id)
    context ={
        "task": task_obj,
    }
    return render(request,"detailPage.html",context)


@login_required(login_url='/login')
def taskEdit(request,id):
    task = Task.objects.get(id=id)
    context = {'task':task}
    return render(request,'taskEdit.html',context)


# @login_required(login_url='/login')
def updatePage(request):
    if request.method =="POST":
        instance = Task.objects.get(id=request.POST.get('id'))
        data = todoAppForm(data=request.POST,instance=instance)
        if data.is_valid():
            data.save()
            return redirect('index')
        return redirect('index')
    return redirect('index')



@login_required(login_url='/login')
def deletePage(request,id):
    task = Task.objects.get(id=id)
    task.delete()
    return redirect('index')