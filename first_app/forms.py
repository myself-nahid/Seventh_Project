from django import forms
from first_app.models import StudentModel

class StudentForm(forms.ModelForm):
    class Meta:
        model = StudentModel
        fields = '__all__'
        labels = {
            'roll' : 'Student Roll',
            'name' : 'Student Name',
            'father_name' : 'Student Father Name',
            'address' : 'Student Address'
        }