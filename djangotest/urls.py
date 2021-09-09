
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('addproject/', views.addproject, name='addproject'),
    path('show/', views.show, name='show'),
    path('deletedata/<int:id>', views.deletedata, name='deletedata'),
    path('<int:id>', views.editdata, name='editdata')
]
