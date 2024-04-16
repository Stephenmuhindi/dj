from django.urls import path

from . import views

app_name = 'conversations'

urlpatterns = [
    path('', views.inbox, name='inbox'),
    path('<int:pk>/', views.detail, name='detail'),
    path('new/<int:kheja_pk>/', views.new_conversations, name='new'),
]