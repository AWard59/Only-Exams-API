from django.contrib.auth import get_user_model
from rest_framework import serializers

from .models.course import Course
from .models.module import Module
from .models.user import User
from .models.assigned_tutors import Assigned_Tutor
from .models.enrolled_course import Enrolled_Course
from .models.completed_module import Completed_Module

# Course Serializers
class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'

class CourseAssignedTutorsSerializer(CourseSerializer):
  tutors = CourseSerializer(read_only=True, many=True)

# Module Serializer
class ModuleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Module
        fields = ('id', 'course', 'name', 'content', 'completed')

# User Serializers
class UserSerializer(serializers.ModelSerializer):
    # This model serializer will be used for User creation
    # The login serializer also inherits from this serializer
    # in order to require certain data for login
    class Meta:
        # get_user_model will get the user model (this is required)
        # https://docs.djangoproject.com/en/3.2/topics/auth/customizing/#referencing-the-user-model
        model = get_user_model()
        fields = ('id', 'email', 'password', 'first_name', 'last_name', 'is_student', 'is_tutor', 'is_author')
        extra_kwargs = {'password': {'write_only': True, 'min_length': 5}}

    # This create method will be used for model creation
    def create(self, validated_data):
        return get_user_model().objects.create_user(**validated_data)

    def update(self, validated_data):
        return get_user_model().objects.partial_update(**validated_data)

class UserRegisterSerializer(serializers.Serializer):
    # Require email, password, and password_confirmation for sign up
    email = serializers.CharField(max_length=300, required=True)
    password = serializers.CharField(required=True)
    password_confirmation = serializers.CharField(
        required=True, write_only=True)
    is_student = serializers.BooleanField(required=True)
    is_tutor = serializers.BooleanField(required=True)
    is_author = serializers.BooleanField(required=True)

    def validate(self, data):
        # Ensure password & password_confirmation exist
        if not data['password'] or not data['password_confirmation']:
            raise serializers.ValidationError(
                'Please include a password and password confirmation.')

        # Ensure password & password_confirmation match
        if data['password'] != data['password_confirmation']:
            raise serializers.ValidationError(
                'Please make sure your passwords match.')
        # if all is well, return the data
        return data

class ChangePasswordSerializer(serializers.Serializer):
    model = get_user_model()
    old = serializers.CharField(required=True)
    new = serializers.CharField(required=True)

class UpdateProfileSerializer(serializers.ModelSerializer):
    # first_name = serializers.CharField(max_length=100)
    # last_name = serializers.CharField(max_length=100)
    user = UserSerializer
    class Meta:
        model = User
        fields = ('first_name', 'last_name')

# Assign Tutor Serializers
class TutorSerializer(serializers.ModelSerializer):
    class Meta:
      model = User
      fields = ('email', 'id')

class AssignedTutorSerializer(serializers.ModelSerializer):
    class Meta:
      model = Assigned_Tutor
      fields = '__all__'

class AssignedTutorReadSerializer(serializers.ModelSerializer):
    course = CourseSerializer()
    tutor = TutorSerializer()
    class Meta:
      model = Assigned_Tutor
      fields = ['id', 'course', 'tutor']

# Enrol Course Serializers
class StudentSerializer(serializers.ModelSerializer):
    class Meta:
      model = User
      fields = ['id', 'email']

class EnrolledCourseSerializer(serializers.ModelSerializer):
    class Meta:
      model = Enrolled_Course
      fields = '__all__'

class EnrolledCourseReadSerializer(serializers.ModelSerializer):
    course = CourseSerializer()
    student = StudentSerializer()
    class Meta:
      model = Enrolled_Course
      fields = ['course', 'student']

# Completed Module Serializers
class CompletedModuleSerializer(serializers.ModelSerializer):
    class Meta:
      model = Completed_Module
      fields = '__all__'

class ModuleCompleteSerializer(serializers.ModelSerializer):
  class Meta:
    model = Module
    fields = ['id']

class CompletedModuleReadSerializer(serializers.ModelSerializer):
    module_complete = ModuleCompleteSerializer()
    class Meta:
      model = Completed_Module
      fields = ['module_complete']
