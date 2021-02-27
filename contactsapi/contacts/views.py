from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .serializers import ContactSerializer
from rest_framework import permissions
from .models import Contact

# Does creating and listing all


class ContactsList(ListCreateAPIView):

    serializer_class = ContactSerializer
    permission_classes = (permissions.IsAuthenticated,)
    # ListCreateAPIView Helps in creation and retrieving of the instance
    # These are methods from the parent class i am overriding

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def get_queryset(self):
        return Contact.objects.filter(owner=self.request.user)


class ContactsDetailView(RetrieveUpdateDestroyAPIView):

    serializer_class = ContactSerializer
    permission_classes = (permissions.IsAuthenticated)
    lookup_field = "id"
    # ListCreateAPIView Helps in creation and retrieving of the instance
    # These are methods from the parent class i am overriding

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def get_queryset(self):
        return Contact.objects.filter(owner=self.request.user)
