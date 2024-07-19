from django.contrib import admin
from django.urls import path
from employees import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.department_tree_view, name='department_tree'),
]