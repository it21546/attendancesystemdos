from django.urls import path
from django.conf.urls import url
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
    path('finalshow_courses/', views.final_choose_course, name='final-view'),
    path('show_courses/<int:pk>/', views.test_choose_course, name='show-courses-pk'),
    path('absence/<int:pk>/update/', AbsenceUpdateView.as_view(), name='absence-update'),
    path('absence/<int:pk>/delete/', AbsenceDeleteView.as_view(), name='absence-delete'),
    path('about/', views.about, name='absence-about'),
    path('ajax_change_course/', views.ajax_change_course, name="ajax_change_course"),
    url(r'^connect/(?P<operation>.+)/(?P<pk>\d+)/$', views.change_course, name='change_course'),


]
