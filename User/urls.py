from django.urls import path # type:ignore
from .views import UserListCreate, UserRetrieveUpdateDelete

urlpatterns = [
    path('user/', UserListCreate.as_view(), name='user-list-create'),
    path('user/<int:pk>/', UserRetrieveUpdateDelete.as_view(), name='user-detail'),
]
