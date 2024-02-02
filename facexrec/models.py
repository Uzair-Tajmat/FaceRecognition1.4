from django.db import models

# Create your models here.
class Department(models.Model):
    course_name=models.CharField(max_length=50)
    def __str__(self) ->str:
        return self.course_name

    class Meta:
        ordering= ['course_name']

class Year(models.Model):
    year=models.CharField(max_length=50)
    def __str__(self) ->str:
        return self.year

    class Meta:
        ordering= ['year']

class Div(models.Model):
    div=models.CharField(max_length=50)
    def __str__(self) ->str:
        return self.div

    class Meta:
        ordering= ['div']


class Student(models.Model):

    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    enroll = models.CharField(max_length=50)
    roll_no=models.CharField(max_length=50)
    
    course_name = models.ForeignKey("Department", on_delete=models.CASCADE)
    year =models.ForeignKey("Year", on_delete=models.CASCADE)
    div=models.ForeignKey("Div", on_delete=models.CASCADE)
    encodeimage=models.FileField(upload_to="encode", max_length=500 ,null=True,default=None)

    
    def __str__(self) ->str:
        return f'{self.first_name} {self.last_name}'

    class Meta:
        ordering= ['first_name','last_name']

class Present(models.Model):
    enroll=models.CharField(max_length=50)
    def __str__(self) ->str:
        return self.enroll

    class Meta:
        ordering= ['enroll']

class Report(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField(max_length=254)
    discription=models.CharField(max_length=1000)
    def __str__(self) ->str:
        return self.enroll

    class Meta:
        ordering= ['name']