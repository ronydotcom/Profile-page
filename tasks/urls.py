from django.urls import path 
from tasks.views import*


urlpatterns = [
    # autrh
    path('',register_page,name='register_page'),
    path('login/',login_page,name='login_page'),
    path('logout/',logout_page,name='logout_page'),
    
    # home
    path('home/',home_page,name='home_page'),
    
    # task
    path('task-list/',task_list,name='task_list'),
    path('add-task/',add_task,name='add_task'),
    path('update-task/<str:t_id>/',update_task,name='update_task'),
    path('delete-task/<str:t_id>/',delete_task,name='delete_task'),
    path('view-task/<str:t_id>/',view_task,name='view_task'),
    path('profile_page/',profile_page,name='profile_page'),
    path('update_profile/',update_profile,name='update_profile'),
    path('product_list/',product_list,name='product_list'),
    path('add_product/',product_list,name='product_list'),
]