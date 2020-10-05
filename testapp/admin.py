from django.contrib import admin

# Register your models here.
from testapp.models import Course, Lesson
class CourseAdmin(admin.ModelAdmin):
    list_display=('course_title','course_desc','course_images')

class LessonAdmin(admin.ModelAdmin):
    list_display=('lesson_title','lesson_descri','course')

admin.site.register(Course,CourseAdmin)
admin.site.register(Lesson,LessonAdmin)
