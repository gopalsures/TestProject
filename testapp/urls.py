from django.urls import path
from testapp import views
from django.conf import settings

urlpatterns = [

    path('hom/',views.home_view,name ='homepage'),
    path('courscre/',views.course_creat_view),
    path('lessoncre/',views.lesson_creat_view),
    path('courslist/',views.CourseListView.as_view()),
    path('lessonlist/',views.LessonListView.as_view()),
    path('cupdate/<int:id>/', views.update_course),
    #path('cdetail/<int:pk>/',views.CourseDetailView.as_view(template_name='testapp/course_detail.html')),

    path('cdelete/<int:id>/',views.delete_course),
    path('cdetail/',views.course_detail),
    path('lesupdate/<int:id>/',views.update_lesson),
    path('lesdelete/<int:id>/',views.delete_lesson),

]
