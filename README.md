# BookMyRoom - Backend

## 📌 Introduction

BookMyRoom is a Django-powered backend that manages hostel bookings for events like Mood Indigo and Techfest. It handles room allocation, tracks availability in real time, and enforces capacity limits smoothly.

Our backend has functionality for hostels, rooms, bookings and users.

## 🚀 Features

- List key features of your backend.
- Mention any unique functionalities.

## 🏗 Tech Stack

- **Backend**: Django
- **Database**: SQLite
- **Authentication**: JWT Authentication

---

## 📦 Installation & Setup

```bash
# Clone the repository
git clone https://github.com/sreehariX/bookmyroom-backend/tree/master

# Navigate to the project directory
cd bookmyroom-backend

# Install dependencies
pip install -r requirements.txt

# Creating a superuser
py manage.py createsuperuser

# Run the backend
py manage.py runserver
```

## 📦 User APIs

### 1. **GET /api/users/**

This endpoint retrieves the details of the logged-in users.

#### **Response**

```json
[
  {
    "id": 1,
    "username": "testUser1",
    "email": "testuser1@gmail.com",
    "phone_number": "1234567890",
    "event": "Mood Indigo"
  },
  {
    "id": 2,
    "username": "testUser2",
    "email": "testuser2@gmail.com",
    "phone_number": "1234567890",
    "event": "Mood Indigo"
  },
  {
    "id": 3,
    "username": "testUser3",
    "email": "testuser3@gmail.com",
    "phone_number": "1234567890",
    "event": "Mood Indigo"
  }
]
```

### 2. **POST /api/register/**

This endpoint allows a new user to register. You must provide the required details, including username, email, phone number, event, and password.

#### **Request Body**

```json
{
  "username": "newUser123",
  "email": "newuser123@example.com",
  "password": "password123",
  "password2": "password123"
}
```

#### **Response Created**

```json
{
  "access": "[access_token]",
  "refresh": "[refresh_token]",
  "user": {
    "username": "newUser123",
    "email": "newuser123@example.com"
  },
  "message": "Registration successful"
}
```

If any validation fails, an error message is returned.

```json
"error": "Username already exists"
or
"error": "Email already exists"
or
"error": "Passwords do not match"
```

### 3. **POST /api/login/**

This endpoint allows users to log in to the platform using their **username** and **password**.

#### **Request Body**

```json
{
  "username": "newUser123",
  "password": "password123"
}
```

#### **Response Created**

```json
{
  "refresh": "[refresh_token]",
  "access": "[acess_token]"
}
```

OR, for invalid credentials :

```json
{
  "detail": "No active account found with the given credentials"
}
```

### 4. **POST /api/logout**

This endpoint allows users to log out of the platform.

#### **Request Body**

```json
{
  "refresh": "[refresh_token]"
}
```

#### **Response**

If the user is logged out successfully:

```json
{
  "message": "Successfully logged out"
}
```

## 📦 Hostels APIs

### 1. **GET /api/hostels/**

This endpoint retrieves a list of all hostels with details such as available rooms, total rooms, location, and hostel type.

#### **Response**

```json
[
  {
    "id": 1,
    "total_available_rooms": 100,
    "name": "1",
    "location": "near sac",
    "total_rooms": 100,
    "hostel_type": "Male"
  },
  {
    "id": 2,
    "total_available_rooms": 2,
    "name": "16",
    "location": "near h15",
    "total_rooms": 100,
    "hostel_type": "Male"
  }
]
```

### 2. **POST /api/hostels/**

This endpoint allows **superusers (admins)** to create a new hostel.

#### **Request Body**

```json
{
  "name": "10", // Hostel name/number
  "location": "Near Gate",
  "total_rooms": 500,
  "hostel_type": "Female"
}
```

#### **Response**

If Successful,

```json
{
  "message": "Hostel created successfully"
}
```

If the user is not a superuser/admin:

```json
{
  "message": "Permission denied. Only superusers can create a hostel."
}
```

## 📦 Rooms APIs

### 1. **GET /api/rooms/**

This endpoint retrieves a list of all rooms with details such as room number, available capacity for Mood Indigo and TechFest, people already booked, and availability status.

#### **Response (200 OK)**

```json
[
  {
    "id": 1,
    "available_capacity_moodIndigo": 1,
    "available_capacity_techFest": 3,
    "hostel_name": "16",
    "room_number": "101",
    "capacity": 3,
    "people_booked_moodIndigo": 2,
    "people_booked_techFest": 0,
    "availability_status_moodIndigo": "available",
    "availability_status_techFest": "available",
    "hostel": 3
  },
  {
    "id": 2,
    "available_capacity_moodIndigo": 0,
    "available_capacity_techFest": 3,
    "hostel_name": "16",
    "room_number": "102",
    "capacity": 3,
    "people_booked_moodIndigo": 3,
    "people_booked_techFest": 0,
    "availability_status_moodIndigo": "booked",
    "availability_status_techFest": "available",
    "hostel": 3
  },
  {
    "id": 3,
    "available_capacity_moodIndigo": 3,
    "available_capacity_techFest": 3,
    "hostel_name": "1",
    "room_number": "101",
    "capacity": 3,
    "people_booked_moodIndigo": 0,
    "people_booked_techFest": 0,
    "availability_status_moodIndigo": "available",
    "availability_status_techFest": "available",
    "hostel": 2
  }
]
```

### 2. **POST /api/rooms/**

This endpoint allows the creation of a new room in a specific hostel. Only authorized users (e.g., admins) can add rooms.

#### **Request Body**

```json
{
  "room_number": "101",
  "capacity": 4,
  "people_booked_moodIndigo": 0,
  "people_booked_techFest": 0,
  "availability_status_moodIndigo": "available",
  "availability_status_techFest": "available",
  "hostel": "16"
}
```

#### **Response**

If Successful,

```json
{
  "id": 1,
  "room_number": "101",
  "capacity": 4,
  "people_booked_moodIndigo": 0,
  "people_booked_techFest": 0,
  "availability_status_moodIndigo": "available",
  "availability_status_techFest": "available",
  "hostel": "16"
}
```

In case of missing or invalid fields:

```json
{
  "error": "Invalid input, please check the fields."
}
```

## 📦 Bookings APIs

### 1. **GET /api/bookings/**

This endpoint retrieves a list of all bookings for a specific event, displaying details like the resident name, room number, and the user associated with each booking.

#### **Response (200 OK)**

```json
[
    {
        "event": "Mood Indigo",
        "resident_name": "rohit",
        "room": 3, // this is the room id
        "user": {
            "id": 5,
            "username": "admin2",
            "email": "",
            "phone_number": null,
            "event": "Mood Indigo"
        }
    }
    {
        "event": "Mood Indigo",
        "resident_name": "mohit",
        "room": 4,
        "user": {
            "id": 5,
            "username": "admin2",
            "email": "",
            "phone_number": null,
            "event": "Mood Indigo"
        }
    }
]

```

### 2. **POST /api/bookings/**

This API is used to create a new booking for an event. The user must provide the event name, resident name, hostel name, and room number.

#### **Request Body**

```json
{
  "event": "Techfest", // (e.g., "Techfest", "Mood Indigo")
  "resident_name": "Arnav", // Name of the person who is going to stay
  "hostel_name": "16", // Name of the hostel where the room is located
  "room_number": "101" // Room number in the specified hostel
}
```

#### **Response**

If Successful,

```json
{
  "event": "Mood Indigo",
  "resident_name": "Arnav",
  "room": 3, // Room id associated with the room
  "user": {
    "id": 5,
    "username": "admin2",
    "email": "",
    "phone_number": "1234567890",
    "event": "Mood Indigo"
  }
}
```

In case of missing or invalid fields:

```json
{
  "error": "Invalid input, please check the fields."
}
```
