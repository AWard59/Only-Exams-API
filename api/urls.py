from django.urls import path
from .views.course_views import CourseView, CourseDetailView
from .views.module_views import ModuleView
from .views.user_views import SignUpView, SignInView, SignOutView, ChangePasswordView, UpdateProfileView, TutorView

urlpatterns = [
  	# Restful routing
    path('sign-up/', SignUpView.as_view(), name='sign-up'),
    path('sign-in/', SignInView.as_view(), name='sign-in'),
    path('sign-out/', SignOutView.as_view(), name='sign-out'),
    path('change-password/', ChangePasswordView.as_view(), name='change-password'),
    path('courses/', CourseView.as_view(), name='courses'),
    path('courses/create/', CourseView.as_view(), name='create-course'),
    path('courses/<int:pk>/', CourseDetailView.as_view(), name='course_detail'),
    path('courses/<int:pk>/modules/', ModuleView.as_view(), name='view-modules'),
    path('courses/<int:pk>/modules/create/', ModuleView.as_view(), name='create-module'),
    path('tutors/', TutorView.as_view(), name='profile'),
    path('profile/', UpdateProfileView.as_view(), name='profile'),
]
