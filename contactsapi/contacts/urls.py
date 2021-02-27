from django.urls import path
from .views import ContactsList, ContactsDetailView


urlpatterns = [
    path('', ContactsList.as_view()),
    path('<int:id>', ContactsDetailView.as_view())
]
