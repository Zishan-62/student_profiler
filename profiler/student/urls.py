from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path ('register', views.register , name='register'),
    path ('login', views.login1  , name='login'),
    
    # path ('store',views.home,name='store'),
    path ('faculty',views.faculty,name='faculty'),
    path('student_profiler/<int:id>',views.student_profiler,name='student_profiler'),
    path('faculty_view/<str:Roll_no>', views.faculty_view , name='faculty_view'),
    path('logout',views.logout_user,name='logout')
]
