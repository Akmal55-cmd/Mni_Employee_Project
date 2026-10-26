#App2 Ka urls


from django.urls import path
from .views import *

urlpatterns = [
    path('empdata/',display,name='empdata'),
    path('form/',addEmpData,name='form'),
    path('editdata/<int:id>/',updateEmpData,name='editdata'),
    path('deletedata/<int:id>/',deleteEmpData,name='deletedata')
]
