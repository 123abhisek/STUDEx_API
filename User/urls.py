from django.urls import path # type:ignore
from .views import SignupListCreate, SignupRetrieveUpdateDelete

urlpatterns = [
    path('user/', SignupListCreate.as_view(), name='signup-list-create'),
    path('user/<int:pk>/', SignupRetrieveUpdateDelete.as_view(), name='signup-detail'),
]
