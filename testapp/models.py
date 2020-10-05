from django.db import models
from django.urls import reverse



# Create your models here..
class Course(models.Model):
    course_title=models.CharField(max_length=25)
    course_desc=models.TextField()
    course_images=models.ImageField (upload_to='media')

    def __str__(self):
        return self.course_title
    def get_absolute_url(self):
        return reverse('hom')


class Lesson(models.Model):
    lesson_title=models.CharField(max_length=30)
    lesson_descri=models.TextField()
    course=models.ForeignKey(Course,on_delete=models.CASCADE)

    def __str__(self):
        return self.lesson_title

    def get_absolute_url(self):
        return reverse('courscre')
