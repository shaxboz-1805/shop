from django.urls import path
from users.views import *

urlpatterns = [
    path('sign_up/', sign_up, name='sign_up' ),
    path('sign_in/', sign_in, name='sign_in' ),
    path('sign_out/', sign_out, name='sign_out' ),
    path('edit_profile/', edit_profile, name='edit_profile' ),
    path('reset_password/', reset_password, name='reset_password' ),
]

