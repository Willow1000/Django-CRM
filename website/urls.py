from django.urls import path
from . import views

from django.conf.urls import handler404,handler500,handler403
from django.shortcuts import render

def custom_404_view(request, exception):
    return render(request, "404.html", status=404)

def custom_500_view(request):
    return render(request, "500.html", status=500)

def custom_403_view(request, exception):
    return render(request, "403.html", status=403)

handler404 = custom_404_view
handler500 = custom_500_view
handler403 = custom_403_view

urlpatterns = [
    path('',views.home,name=
         'home'),
    path('logout/',views.logout_user, name='logout'),
    path('register/',views.register_user, name='register'),
    path('records/',views.ListRecords.as_view(), name='records'),
    path('records/<int:pk>/',views.GetRecord.as_view(), name='record'),
    path('delete/record/<int:pk>/',views.DeleteRecord.as_view(), name='delete'),
    path('update/record/<int:pk>/',views.UpdateRecord.as_view(), name='update'),
    path('create/record/',views.CreateRecord.as_view(), name='create'),
]