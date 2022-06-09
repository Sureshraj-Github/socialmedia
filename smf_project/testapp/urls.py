from django.urls import path
from testapp import views
urlpatterns=[
    path('',views.index),
    path('login/',views.login),
    path('profile/',views.profile),
    path('document/',views.document),
    path('view_document/',views.view_document),
    path('view_table/',views.view_table),
]