from django.urls import path
from . import views

urlpatterns = [

    path('', views.index, name='index'),
    path('add_student/', views.add_student, name='add'),
    path('add_student/addrecord/', views.addrecord_student, name='addrecord'),
    path('delete_student/<int:id>', views.delete_student, name='delete'),
    path('update/<int:id>', views.update, name='update'),
    path('update/updaterecord/<int:id>', views.updaterecord, name='updaterecord'),

    path('index_dept/', views.index_dept, name='index_dept'),
    path('index_dept/add_dept/', views.add_dept, name='add_dept'),
    path('index_dept/add_dept/addrecord/', views.addrecord_dept, name='addrecord_dept'),
    path('index_dept/delete_dept/<int:id>', views.delete_dept, name='delete_dept'),
    path('index_dept/update_dept/<int:id>', views.update_dept, name='update_dept'),
    path('index_dept/update_dept/updaterecord_dept/<int:id>', views.updaterecord_dept, name='updaterecord_dept'),


]