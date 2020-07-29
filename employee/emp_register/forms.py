from django.forms import ModelForm
from .models import Employee

class EmployeeForm(ModelForm):
    class Meta:
        model = Employee
        fields = '__all__'
        labels = {
            'emp_code':'EMP. Code',
            'fullname':'Full Name'
        }


    def __init__(self, *args, **kwargs):
        super(EmployeeForm, self).__init__(*args, **kwargs)
        self.fields['designation'].empty_label = 'Select'
        self.fields['emp_code'].required = False
        self.fields['emp_code'].widget.attrs['placeholder'] = 'Employee Code'
        self.fields['fullname'].widget.attrs['placeholder'] = 'Full Name'
        self.fields['mobile'].widget.attrs['placeholder'] = 'Mobile Number'
        self.fields['email'].widget.attrs['placeholder'] = 'Email Address'
