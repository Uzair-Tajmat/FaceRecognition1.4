from django.forms import ModelForm
from django import forms 
from .models import Student

class StudentForm(ModelForm):
    encodeimage = forms.FileField(max_length=500, required=False)
    class Meta:
        model = Student
        fields = '__all__'

        widgets={
            'first_name':forms.TextInput(attrs={'class':'form-control'}),
            'last_name':forms.TextInput(attrs={'class':'form-control'}),
            'enroll' :forms.TextInput(attrs={'class':'form-control'}),
            'roll_no': forms.TextInput(attrs={'class':'form-control'}),
            'course_name':forms.Select(attrs={'class':'form-control'}),
            'year':forms.Select(attrs={'class':'form-control'}),
            'div':forms.Select(attrs={'class':'form-control'}),
            'encodeimage':forms.FileInput(attrs={'class':'form-control'})



   
        }