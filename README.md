# Simple-Login-Page

 
This project implements a **simple login and registration system** using **Python Flask** as the backend and **Tkinter** as the GUI frontend. The system securely stores user credentials in an **SQLite database** and uses **bcrypt** for password hashing to enhance security. Users can register new accounts and log in through a user-friendly Tkinter interface, which communicates with the Flask backend.

The project consists of two main components:  
1. **Backend (Flask + SQLite)**  
   - Handles user registration and authentication.  
   - Stores user credentials securely using bcrypt hashing.  
   - Provides API endpoints (`/register` and `/login`) for communication with the frontend.

2. **Frontend (Tkinter GUI)**  
   - Provides a graphical interface for user login and registration.  
   - Sends user credentials to the backend via HTTP requests.  
   - Displays success or error messages based on the backend response.  

This system is a lightweight and secure solution for user authentication, suitable for small applications that require local credential storage. 🚀
