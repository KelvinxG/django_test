
from django.urls import path 

from . import views  

urlpatterns = [ 
    path('',views.index,name='index'),
    path('<int:id>/',views.delete_todo,name='delete'),
    path('<int:id>/',views.update_todo,name='update'),
]