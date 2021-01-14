from django.urls import path

from core.user.views import UserChangeGroup

app_name = 'user'

urlpatterns = [
    ## FORMULARIOS EMPLEADO ##
    path('change/group/<int:pk>/', UserChangeGroup.as_view(), name='user_change_group'),
]
