from django import forms
from django.contrib.auth.models import User
from .models import Course, Absence

class AbsenceCreateForm(forms.ModelForm):
    model = Absence
    fields = ['course', 'username', 'it_number', 'student_name', 'professor_name', 'date_of_absence' ]
"""
        def __init__(self, *args, **kwargs):
            foo_id = kwargs.pop('foo_id')
            super(AbsenceCreateForm, self).__init__(*args, **kwargs)
            self.fields['course'].queryset = Course.objects.filter(foo_id=foo_id)
"""
