from django.urls import path
from App import views


urlpatterns = [
    path('',views.emp_form,name = 'emp_insert'),  #get and post for insert operation 
    path('list/',views.emp_list,name = 'emp_list'), #get operation for displaying all records
    path('<int:id>/',views.emp_form,name = 'emp_update'), #get and post for update operation
    path('delete/<int:id>/',views.emp_delete,name = 'emp_delete') #post method for deleating operation. 
]