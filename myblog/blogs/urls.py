from django.urls import path

from . import views

# set the application namespace
# https://docs.djangoproject.com/en/2.0/intro/tutorial03/
app_name = 'blogs'

urlpatterns = [
    # ex: /
    path('', views.IndexView.as_view(), name='index'),

    # ex: /post/create/
    path('post/create/', views.CreateView.as_view(), name='create'),

    # ex: /post/1/
    path('post/<int:pk>/', views.DetailView.as_view(), name='detail'),

    # ex: /post/1/update/
    path('post/<int:pk>/update/', views.UpdateView.as_view(), name='update'),

    # ex: /post/1/delete
    path('post/<int:pk>/delete/', views.DeleteView.as_view(), name='delete'),

    # ex: /post/help/
    path('post/help/', views.help, name='help'),
]
