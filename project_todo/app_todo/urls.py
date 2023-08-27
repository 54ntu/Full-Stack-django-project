from django.urls import path
from . import views
from .views import LoginView,RegisterView,LogoutView

urlpatterns = [
    path('index/',views.index,name='index'),
    path('create/', views.taskCreate,name="task-create"),
    path('detailPage/<int:id>/',views.detailPage,name='detail'),
    path('edit/<int:id>/',views.taskEdit,name='edit'),
    path('delete/<int:id>/',views.deletePage,name='delete'),
    path('update/',views.updatePage,name='update'),
    path('login/',LoginView.as_view(),name='login'),
    path('register/',RegisterView.as_view(),name='register'),
    path('logout/',LogoutView.as_view(),name='logout')

]
