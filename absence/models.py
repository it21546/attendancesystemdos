from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.

POSTUND_CHOICES = [
    ("Προπτυχιακό", "Προπτυχιακό"),
    ("Μεταπτυχιακό", "Μεταπτυχιακό"),
]

DEPARTMENT_CHOICES = [
	("Πληροφορικής και Τηλεματικής", "Πληροφορικής και Τηλεματικής"),
	("Διαιτολογίας-Διατροφής", "Διαιτολογίας-Διατροφής"),
	("Γεωγραφίας", "Γεωγραφίας"),
    ("Οικονομίας και Βιώσιμης Ανάπτυξης", "Οικονομίας και Βιώσιμης Ανάπτυξης"),
]

class Course(models.Model):
    course_name = models.CharField(max_length = 100)
    users_available = models.ManyToManyField(User)
    post_und = models.CharField(max_length = 100, choices = POSTUND_CHOICES, default = '')
    department = models.CharField(max_length = 100, choices = DEPARTMENT_CHOICES, default = 'Πληροφορικής και Τηλεματικής')

    def __str__(self):
        return self.course_name


class Absence(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    username = models.ForeignKey(User, on_delete=models.CASCADE) #CharField(max_length = 100, null=True, blank=True)
    professor_name = models.CharField(max_length = 100)
    student_name = models.CharField(max_length = 100)
    it_number = models.CharField(max_length = 100)
    date_of_absence = models.DateTimeField(default=timezone.now)
    absences_left = models.IntegerField(default=0)
    is_failed = models.BooleanField(default=False)


    def __str__(self):
        return self.it_number

    def get_absolute_url(self):
        return reverse('absence-detail', kwargs={'pk': self.pk})
