

from django.urls import path, include

from myapp import views

urlpatterns = [
    path('employee_list/',views.employee_list.as_view(),name='employee_list'),
    path("employee_list_detail/<int:pk>/",views.employee_list_detail.as_view(),name='employee_list_detail'),
    path('employee_list_generic_view/',views.employee_list_generic_view.as_view(),name='employee_list_generic_view'),
    path('employee_list_generic_view_detail/<int:pk>/',views.employee_list_generic_view_detail.as_view(),name='employee_list_generic_view_detail'),

]
