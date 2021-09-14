from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Absence, Course
from .forms import AbsenceCreateForm
# Create your views here.
"""
#@login_required
def home(request):
    context = {
        'absences': Absence.objects.all()
    }
    return render(request, 'absence/student_home.html', context)
"""

def home(request):
    context = {
        'courses': Course.objects.all(),
        'absences': Absence.objects.all()#(username=request.user.username)
    }
    return render(request, 'absence/student_home.html', context)

@login_required
def choose_course(request):
    context = {
        'courses': Course.objects.all()#(username=request.user.username)
    }
    return render(request, 'absence/show_courses.html', context)

def test_choose_course(request, pk=None):
    if pk:
        course = Course.objects.get(pk=pk)
    args = {'course': course}
    return render(request, 'absence/testpk.html', args)

@login_required
def about(request):
    context = {
        'courses': Course.objects.filter(users_available=request.user),
        #'absence': Absence.objects.all()
        'absences': Absence.objects.filter(username=request.user).order_by('course')
    }
    return render(request, 'absence/about.html', context)

class AbsenceListView(LoginRequiredMixin, ListView):
	model = Absence
	template_name = 'absence/student_home.html'	#it is looking for a template of this format:  <app>/<model>_<viewtype>.html
	context_object_name = 'absences'
	ordering = ['course']
	#paginate_by = 5


class UserAbsenceListView(ListView):
	model = Absence
	template_name = 'absence/user_absence.html'	#it is looking for a template of this format:  <app>/<model>_<viewtype>.html
	context_object_name = 'absences'
	paginate_by = 2

	def get_queryset(self):
		user = get_object_or_404(User, username=self.kwargs.get('username')) #!!!!!!!gets username from url !!!!!!
		return Absence.objects.filter(username=user).order_by('course')
"""

class UserAbsenceListView(ListView):
	model = Absence
	template_name = 'absence/user_absence.html'	#it is looking for a template of this format:  <app>/<model>_<viewtype>.html
	context_object_name = 'absences'
	paginate_by = 2

	def get_queryset(self):
		user = get_object_or_404(User, username={"username": self.request.user.username}) #!!!!!!!gets username from url !!!!!!
		return Absence.objects.filter(username=user).order_by('it_number')
"""
class CourseAbsenceListView(ListView):
	model = Absence
	template_name = 'absence/course_absence.html'	#it is looking for a template of this format:  <app>/<model>_<viewtype>.html
	context_object_name = 'absence'
	paginate_by = 3

	def get_queryset(self):
		course = get_object_or_404(Course, course_name=self.kwargs.get('course_name')) #!!!!!!!gets username from url !!!!!!
		return Absence.objects.filter(username=request.user, course_name=course).order_by('-date_of_absence')


class AbsenceDetailView(LoginRequiredMixin, DetailView):
    model = Absence

class AbsenceCreateView(LoginRequiredMixin, CreateView):
    model = Absence
    #form = AbsenceCreateForm
    fields = ['course', 'username', 'it_number', 'student_name', 'professor_name', 'date_of_absence' ]
    #form.fields["course"].queryset = Course.objects.filter(users_available=8)
"""
    def get_form_kwargs(self):
        kwargs = super(AbsenceCreateView, self).get_form_kwargs()
        kwargs.update({'foo_id': self.kwargs.get('foo_id')})
        return kwargs
"""

class AbsenceUpdateView(LoginRequiredMixin,UserPassesTestMixin, UpdateView):
    model = Absence
    fields = ['course', 'username', 'it_number', 'student_name', 'professor_name', 'date_of_absence', 'absences_left', 'is_failed' ]

    def form_valid(self, form):
        form.instance.username = self.request.user
        return super().form_valid(form)

    def test_func(self):
        absence = self.get_object()
        if self.request.user == absence.username:
            return True
        return False

class AbsenceDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
	model = Absence
	success_url = "/absence"

	def test_func(self):	#via the UserPassesTestMixin import we ensure that only the author of the post can update it
		absence = self.get_object()
		if self.request.user == absence.username:
			return True
		return False
