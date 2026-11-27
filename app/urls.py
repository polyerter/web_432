from django.contrib import admin
from django.urls import path
from hello import views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', views.home),
    path('about/', views.about),
    path('math/', views.math),
    path('tasks/', views.tasks),

    path('discriminant/', views.disc_page),
    path('calc_discriminant/', views.calc_discriminant),

    path('sum/', views.sum_page),
    path('calc_sum/', views.calc_sum),
    path('tasks/probability/', views.probability),
    path('tasks/percent/', views.percent),
]
