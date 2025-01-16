# Railway Ticket Booking System

A Django-based Railway Ticket Booking System that allows users to view available trains, schedule details, and book tickets. The project includes an admin interface to manage trains, schedules, passengers, and tickets.

## Features

- **View Trains**: List of available trains.
- **Train Schedule Details**: View departure and arrival times for each train.
- **Book Tickets**: Users can book tickets for available trains based on schedule.
- **Admin Panel**: Manage trains, schedules, passengers, and tickets.
- **Success Page**: Shows a confirmation after booking a ticket.

## Models

- **Train**: Represents a train with details such as name, number, and capacity.
- **Passenger**: Represents a passenger with details such as name, email, and phone.
- **Station**: Represents a station with details such as name and city.
- **Route**: Represents a route between two stations with distance.
- **Schedule**: Represents a train schedule with departure and arrival times.
- **Ticket**: Represents a ticket for a passenger, associated with a specific train and schedule.

