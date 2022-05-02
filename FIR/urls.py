from django.urls import path

from FIR import views

urlpatterns = [
    path('',views.home),
    path('readdata',views.login),
    path('insert',views.insertpage),  #details and complaint page
    path('insertdata',views.insert_data),
    path('displaydata',views.display_data),
    path('hqcontacts',views.hq_contacts),
    path('update\<int:id>',views.update_data, name='update'),
]