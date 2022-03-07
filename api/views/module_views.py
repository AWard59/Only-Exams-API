from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import PermissionDenied
from rest_framework import generics, status
from django.shortcuts import get_object_or_404

from ..models.module import Module
from ..serializers import ModuleSerializer

# Create your views here.

class ModuleView(generics.ListCreateAPIView):
    permission_classes = ()
    serializer_class = ModuleSerializer

    def get(self, request, pk):
        """Index request"""
        # Get all the mangos:
        # modules = Module.objects.all()
        modules = Module.objects.filter(course=pk)
        serializer = ModuleSerializer(modules, many=True).data
        return Response({'modules': serializer})

    def post(self, request, pk):
        """Create request"""
        serializer = ModuleSerializer(data=request.data['module'])
        if serializer.is_valid():
            serializer.save()
            return Response({'module': serializer.data}, status=status.HTTP_201_CREATED)
        # If the data is not valid, return a response with the errors
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ModuleDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, pk):
        """Show request"""
        # Locate the mango to show
        module = get_object_or_404(Module, pk=pk)
        # Only want to show owned mangos?
        if request.user != module.owner:
            raise PermissionDenied('Unauthorized, you do not own this mango')

        # Run the data through the serializer so it's formatted
        serializer = CourseSerializer(module).data
        return Response({'module': serializer})

    def delete(self, request, pk):
        """Delete request"""
        # Locate mango to delete
        module = get_object_or_404(Module, pk=pk)
        # Check the mango's owner against the user making this request
        if request.user != module.owner:
            raise PermissionDenied('Unauthorized, you do not own this mango')
        # Only delete if the user owns the  mango
        module.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def partial_update(self, request, pk):
        """Update Request"""
        # Locate Mango
        # get_object_or_404 returns a object representation of our Mango
        module = get_object_or_404(Module, pk=pk)
        # Check the mango's owner against the user making this request
        if request.user != module.owner:
            raise PermissionDenied('Unauthorized, you do not own this mango')

        # Ensure the owner field is set to the current user's ID
        request.data['module']['owner'] = request.user.id
        # Validate updates with serializer
        serializer = CourseSerializer(
            module, data=request.data['module'], partial=True)
        if serializer.is_valid():
            # Save & send a 204 no content
            serializer.save()
            return Response({'module': serializer.data})
        # If the data is not valid, return a response with the errors
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
