from django.urls import path
from .views import RegisterPageView, TaskListView
from .views import TaskDetailView
from .views import TaskCreateView
from .views import TaskEditView
from .views import TaskDeleteView
from .views import CustomLoginView
from django.contrib.auth.views import LogoutView
from .views import customLogoutView



urlpatterns = [
    path('login/',CustomLoginView.as_view(), name ='login'),
    path('logout/', customLogoutView, name='logout'),
    path('register/',RegisterPageView.as_view(), name ='register'),

    path('', TaskListView.as_view(), name='tasks'),
    path('task/<int:pk>', TaskDetailView.as_view(), name='taskDetail' ),
    path('create-task', TaskCreateView.as_view(), name='createTask' ),
    path('task-update/<int:pk>', TaskEditView.as_view(), name='taskEdit' ),
    path('task-delete/<int:pk>', TaskDeleteView.as_view(), name='taskDelete' ),

]
