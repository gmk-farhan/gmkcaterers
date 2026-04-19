Readme

GMK Caterers Web Application
A full-stack catering service web application built using Flask and MySQL, designed to handle customer interactions such as registrations, orders, feedback, and service browsing.

Overview
This project is a dynamic catering website that allows users to:
    Browse catering services (weddings, corporate events, private parties)
    Place event orders
    Submit feedback and testimonials
    Contact the business
    Register and log in as users
It combines a Flask backend with HTML/CSS/JS/jQuery frontend templates and a MySQL database for persistent storage.

Features
    User registration and login system
    Event booking (weddings, corporate, private parties)
    Feedback and testimonial submission
    Contact form
    Menu and service pages
    Form validation using regex
    Database integration with SQLAlchemy

Tech Stack
Backend:
    Python (Flask)
    Flask-SQLAlchemy
Frontend:
    HTML
    CSS
    JavaScript
    jQuery
Database:
    MySQL

Run the Application by using this command
    python app.py
Open your browser and go to:
http://127.0.0.1:5000/

Sitemap:
project/
├── app.py
├── static/
│   ├── css files
│   ├── images
│   └── JavaScript files
├── templates/
│   ├── index.html
│   ├── about.html
│   ├── contact.html
│   ├── order.html
│   ├── testimonial.html
│   └── other pages

Key Modules
User_info - Handles user registration data
Order - Stores event booking details
Feedback - Stores testimonials
Contact - Stores user messages

Validation Rules

Name         | Minimum 3 alphabetic characters              
Phone Number | Must start with `07` and be 11 digits        
Username     | 8–20 characters, includes `_ @ $`           
Password     | Starts with capital letter, min 8 characters 
Email        | Valid email format                          
Confirm Pass | Must match password
Event        | Minimum 3 alphabetic characters
Venue        | Minimum 3 alphabetic characters