from django.urls import path

from .views.user_views import SignUpView, SignInView, SignOutView, ChangePasswordView, UpdateProfileView, TutorView
from .views.course_views import CourseView, CourseDetailView, CourseViewStudent, CourseDetailViewStudent
from .views.module_views import ModuleView, ModuleDetailView
from .views.assigned_tutor_views import AssignedTutorsView, CourseViewTutor
from .views.enrolled_course_views import EnrolledCourseView, EnrolledStudentView
from .views.completed_module_views import CompletedModuleView

urlpatterns = [
  	# Restful routing
    # AUTH views
    path('sign-up/', SignUpView.as_view(), name='sign-up'),
    path('sign-in/', SignInView.as_view(), name='sign-in'),
    path('sign-out/', SignOutView.as_view(), name='sign-out'),
    path('change-password/', ChangePasswordView.as_view(), name='change-password'),
    path('profile/', UpdateProfileView.as_view(), name='profile'),
    # Author views
    path('courses/', CourseView.as_view(), name='courses'),
    path('courses/create/', CourseView.as_view(), name='create-course'),
    path('courses/modules/create/', ModuleView.as_view(), name='create-module'),
    path('courses/modules/<int:pk>/', ModuleDetailView.as_view(), name='edit-module'),
    path('courses/<int:pk>/tutors/', AssignedTutorsView.as_view(), name='tutors-get'),
    path('tutors/', TutorView.as_view(), name='tutors'),
    path('tutors/assign/', AssignedTutorsView.as_view(), name='tutors-assign'),
    # Tutor views
    path('courses/assigned/', CourseViewTutor.as_view(), name='courses-assigned'),
    path('courses/<int:pk>/enrolled/', EnrolledStudentView.as_view(), name='enrolled_students'),
    # Student views
    path('courses/available/', CourseViewStudent.as_view(), name='courses-available'),
    path('courses/<int:pk>/enrol/', EnrolledCourseView.as_view(), name='enrol_course'),
    path('courses/enrolled/', EnrolledCourseView.as_view(), name='enrolled_courses' ),
    path('courses/modules/<int:pk>/complete/', CompletedModuleView.as_view(), name='complete-module'),
    path('courses/<int:pk>/modules/completed/', CompletedModuleView.as_view(), name='view-completed-modules'),
    path('courses/<int:pk>/view/', CourseDetailViewStudent.as_view(), name='enrolled-course-detail'),
    # Generic views
    path('courses/<int:pk>/', CourseDetailView.as_view(), name='course_detail'),
    path('courses/<int:pk>/modules/', ModuleView.as_view(), name='view-modules'),
]
