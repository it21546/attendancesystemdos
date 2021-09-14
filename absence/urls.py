from django.urls import path
from .views import (
    AbsenceListView,
    AbsenceDetailView,
    AbsenceCreateView,
    AbsenceUpdateView,
    AbsenceDeleteView,
    UserAbsenceListView,
    CourseAbsenceListView
    )
from . import views

urlpatterns = [
    path('', AbsenceListView.as_view(), name='absence-home'),
    path('user/<str:username>', UserAbsenceListView.as_view(), name='user-absences'),
    path('course/<str:course>', CourseAbsenceListView.as_view(), name='course-absences'),
    path('absence/<int:pk>/', AbsenceDetailView.as_view(), name='absence-detail'),
    path('absence/new/', AbsenceCreateView.as_view(), name='absence-create'),
    path('show_courses/', views.choose_course, name='show-courses'),
    path('show_courses/<int:pk>/', views.test_choose_course, name='show-courses-pk'),
    path('absence/<int:pk>/update/', AbsenceUpdateView.as_view(), name='absence-update'),
    path('absence/<int:pk>/delete/', AbsenceDeleteView.as_view(), name='absence-delete'),
    path('about/', views.about, name='absence-about'),


]
