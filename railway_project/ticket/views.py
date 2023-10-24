from django.shortcuts import render, redirect, get_object_or_404
from .models import Train, Passenger, Schedule, Ticket

def train_list(request):
    trains = Train.objects.all()
    return render(request, 'ticket_booking/train_list.html', {'trains': trains})

def book_ticket(request, train_id, schedule_id):
    if request.method == 'POST':
        # Get the selected schedule and train
        schedule = get_object_or_404(Schedule, pk=schedule_id)
        train = get_object_or_404(Train, pk=train_id)

        # Check if there are available seats for this schedule
        if schedule.available_seats > 0:
            # Assuming you have a logged-in user, you can get the passenger here
            passenger = request.user.passenger  # Replace this with your authentication logic

            # Create a new ticket for the passenger
            ticket = Ticket(train=train, schedule=schedule, passenger=passenger)
            ticket.save()

            # Reduce the available seats for the schedule
            schedule.available_seats -= 1
            schedule.save()

            # Redirect to a success page or any other relevant page
            return redirect('ticket_booking:success_page')  # Replace 'success_page' with your success page URL name

    # If the request method is not POST or the booking failed, you can render a form or an error message.
    return render(request, 'ticket_booking/booking_form.html', {'schedule_id': schedule_id, 'train_id': train_id})

def schedule_detail(request, schedule_id):
    schedule = Schedule.objects.get(pk=schedule_id)
    return render(request, 'ticket_booking/schedule_detail.html', {'schedule': schedule})

def success_page(request):
    return render(request, 'ticket_booking/success_page.html')

