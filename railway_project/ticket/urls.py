from django.urls import path
from . import views

app_name = 'ticket_booking'  # Set the app name

urlpatterns = [
    path('trains/', views.train_list, name='train_list'),
    path('schedule/<int:schedule_id>/', views.schedule_detail, name='schedule_detail'),
    path('book/<int:train_id>/<int:schedule_id>/', views.book_ticket, name='book_ticket'),
    path('success/', views.success_page, name='success_page'),  # Add this URL for the success page
]
