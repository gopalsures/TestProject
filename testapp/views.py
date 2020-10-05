from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from testapp.models import Course, Lesson
from testapp.forms import CourseForm,LessonForm, UserRegistrationForm
from django.urls import reverse
from django.views.generic import ListView,UpdateView,DeleteView,DetailView
from django.contrib.auth.decorators import login_required

# Create your views here.
def user_registration(request):
    form = UserRegistrationForm()
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.cleaned_data.get('username')
            form.save()
            return redirect('/testapp/hom/')

    return render(request,'testapp/userreg.html',{'form':form})



def home_view(request):
    return render(request,'testapp/index.html')

@login_required
def  course_creat_view(request):
    form1=CourseForm()
    if request.method=='POST':
        form1=CourseForm(request.POST or None,request.FILES)
        if form1.is_valid():
            form1.save()
        return lesson_creat_view(request)
    return render(request,'testapp/coursecreat.html',{'form1': form1})

@login_required
def  lesson_creat_view(request):
    form=LessonForm()
    if request.method=='POST':
        form=LessonForm(request.POST)
        if form.is_valid():
            form.save()
        return home_view(request)
    return render(request,'testapp/lessoncre.html',{'form': form})


class CourseListView(ListView):
    model=Course

class LessonListView(ListView):
    model=Lesson

def delete_course(request,id):
    obj=Course.objects.get(pk=id)
    obj.delete()
    return redirect('/testapp/courslist/')


def update_course(request,id):
    obj=Course.objects.get(pk=id)

    if request.method =='POST':
        obj.course_title =request.POST.get('course_title')
        obj.course_desc =request.POST.get('course_desc')
        obj.save()
        return redirect('/testapp/courslist/')
    return render(request,'testapp/course_update.html',{'obj':obj})


def course_detail(request):
    obj=Course.objects.all()
    return render(request,'testapp/course_detail.html')


def delete_lesson(request,id):
    obj=Lesson.objects.get(pk=id)
    obj.delete()
    return redirect('/testapp/lessonlist/')


def update_lesson(request,id):
    obj=Lesson.objects.get(pk=id)

    if request.method =='POST':
        obj.lesson_title =request.POST.get('lesson_title')
        obj.lesson_descri =request.POST.get('lesson_descri')
        obj.save()
        return redirect('/testapp/lessonlist/')
    return render(request,'testapp/lesson_update.html',{'obj':obj})
