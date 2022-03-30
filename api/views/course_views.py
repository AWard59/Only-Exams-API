from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import PermissionDenied
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework import generics, status
from django.shortcuts import get_object_or_404

from ..models.course import Course
from ..serializers import CourseSerializer

# Create your views here.
class CourseView(generics.ListCreateAPIView):
    permission_classes=(IsAuthenticated,)
    serializer_class = CourseSerializer
    parser_classes = (MultiPartParser, FormParser)

    def get(self, request):
        """Index request"""
        # Filter the courses by owner, so you can only see your owned courses
        courses = Course.objects.filter(owner=request.user.id)
        # Run the data through the serializer
        serializer = CourseSerializer(courses, many=True).data
        return Response({ 'courses': serializer })

    def post(self, request, format=None):
        """Create request"""
        # Add user to request data object
        request.data._mutable = True
        request.data['owner'] = request.user.id
        request.data._mutable = False
        # Serialize/create course
        serializer = CourseSerializer(data=request.data)
        # If the course data is valid according to our serializer...
        if serializer.is_valid():
            # Save the created course & send a response
            serializer.save()
            return Response({ 'course': serializer.data }, status=status.HTTP_201_CREATED)
        # If the data is not valid, return a response with the errors
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CourseDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes=(IsAuthenticated,)
    def get(self, request, pk):
        """Show request"""
        # Locate the course to show
        course = get_object_or_404(Course, pk=pk)
        # Only want to show owned courses?
        if request.user != course.owner:
            raise PermissionDenied('Unauthorized, you do not own this mango')

        # Run the data through the serializer so it's formatted
        serializer = CourseSerializer(course).data
        return Response({'course': serializer})

    def delete(self, request, pk):
        """Delete request"""
        # Locate course to delete
        course = get_object_or_404(Course, pk=pk)
        # Check the course's owner against the user making this request
        if request.user != course.owner:
            raise PermissionDenied('Unauthorized, you do not own this mango')
        # Only delete if the user owns the  mango
        course.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def partial_update(self, request, pk):
        """Update Request"""
        # get_object_or_404 returns a object representation of our course
        course = get_object_or_404(Course, pk=pk)
        # Check the course's owner against the user making this request
        if request.user != course.owner:
            raise PermissionDenied('Unauthorized, you do not own this mango')

        # Ensure the owner field is set to the current user's ID
        request.data['course']['owner'] = request.user.id
        # Validate updates with serializer
        serializer = CourseSerializer(course, data=request.data['course'], partial=True)
        if serializer.is_valid():
            # Save & send a 204 no content
            serializer.save()
            return Response({'course': serializer.data})
        # If the data is not valid, return a response with the errors
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CourseViewStudent(generics.ListCreateAPIView):
    permission_classes=(IsAuthenticated,)
    serializer_class = CourseSerializer

    def get(self, request):
        """Index request"""
        courses = Course.objects.all()
        # Run the data through the serializer
        serializer = CourseSerializer(courses, many=True).data
        return Response({ 'courses': serializer })

class CourseDetailViewStudent(generics.RetrieveUpdateDestroyAPIView):
    permission_classes=(IsAuthenticated,)
    def get(self, request, pk):
        """Show request"""
        course = get_object_or_404(Course, pk=pk)
        # Run the data through the serializer so it's formatted
        serializer = CourseSerializer(course).data
        return Response({'course': serializer})
