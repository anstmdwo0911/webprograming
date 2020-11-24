from django.urls import path
from . import views

app_name='notion'

urlpatterns=[
    # path('',views.index, name='index'),
    path('',views.notion, name='notion'),
    # path('notion/',views.notion ,name='notion'),
    path('notion/<int:pk>/', views.post, name="post"),
    path('create/', views.create, name='create'),
    path('<int:pk>/delete/', views.delete, name='delete'),
    # path('notion/<int:pk>/pw/', views.pw, name='pw'),
]