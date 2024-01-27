from django.urls import path
from . import views


urlpatterns=[
    path('register', views.registerpage, name='register'),
    path('login', views.loginpage, name='login'),
    path('logout', views.logoutpage, name='logout'),
    path('', views.homepage, name='index'),
    path('new-question', views.newQuestionpage, name='new-question'),
    path('question/<int:id>', views.questionpage, name='question'),
    path('reply', views.replyPage, name='reply')
]