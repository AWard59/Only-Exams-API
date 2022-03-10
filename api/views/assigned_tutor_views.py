from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import PermissionDenied
from rest_framework import generics, status
from django.shortcuts import get_object_or_404

from ..models.assigned_tutors import Assigned_Tutor
from ..serializers import AssignedTutorReadSerializer, AssignedTutorSerializer

# Create your views here.

class AssignedTutorsView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = AssignedTutorSerializer

    def get(self, request, pk):
        """Index request"""
        assigned_tutors = Assigned_Tutor.objects.filter(course=pk)
        serializer = AssignedTutorReadSerializer(
            assigned_tutors, many=True).data
        return Response({'assigned_tutors': serializer})

    def post(self, request):
        """Create request"""
        print('req', request.data['assign'])
        serializer = AssignedTutorSerializer(data=request.data['assign'])
        print('serializer', serializer)
        if serializer.is_valid():
            serializer.save()
            return Response({'assigned_tutors': serializer.data}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AssignedTutorsDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, pk):
        """Show request"""
        assigned_tutor = get_object_or_404(Assigned_Tutor, pk=pk)
        serializer = AssignedTutorReadSerializer(assigned_tutor).data
        return Response({'assigned_tutor': serializer})

    def delete(self, request, pk):
        """Delete request"""
        assigned_tutor = get_object_or_404(Assigned_Tutor, pk=pk)
        assigned_tutor.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def patch(self, request, pk):
        """Update Request"""
        assigned_tutor = get_object_or_404(Assigned_Tutor, pk=pk)
        serializer = AssignedTutorSerializer(assigned_tutor, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'assigned_tutor': serializer.data})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
