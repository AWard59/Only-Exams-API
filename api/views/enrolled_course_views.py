from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import PermissionDenied
from rest_framework import generics, status
from django.shortcuts import get_object_or_404

from ..models.enrolled_course import Enrolled_Course
from ..serializers import EnrolledCourseReadSerializer, EnrolledCourseSerializer

# Create your views here.
class EnrolledCourseView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = EnrolledCourseSerializer

    def get(self, request):
        """Index request"""
        enrolled_courses = Enrolled_Course.objects.filter(student=request.user.id)
        serializer = EnrolledCourseReadSerializer(enrolled_courses, many=True).data
        return Response({'enrolled_courses': serializer})

    def post(self, request, pk):
        """Create request"""
        serializer = EnrolledCourseSerializer(data=request.data['enrol'])
        if serializer.is_valid():
            serializer.save()
            return Response({'enrolled_courses': serializer.data}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class EnrolledStudentView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = EnrolledCourseSerializer

    def get(self, request, pk):
        """Index request"""
        enrolled_students = Enrolled_Course.objects.filter(
            course=pk)
        serializer = EnrolledCourseReadSerializer(
            enrolled_students, many=True).data
        return Response({'enrolled_students': serializer})

class EnrolledCourseDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, pk):
        """Show request"""
        enrolled_course = get_object_or_404(Enrolled_Course, pk=pk)
        serializer = EnrolledCourseReadSerializer(enrolled_course).data
        return Response({'enrolled_course': serializer})

    def delete(self, request, pk):
        """Delete request"""
        enrolled_course = get_object_or_404(Enrolled_Course, pk=pk)
        enrolled_course.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def patch(self, request, pk):
        """Update Request"""
        enrolled_course = get_object_or_404(Enrolled_Course, pk=pk)
        serializer = EnrolledCourseSerializer(
            enrolled_course, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'enrolled_course': serializer.data})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
