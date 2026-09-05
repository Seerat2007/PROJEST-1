# Weather App

A responsive weather application that allows users to search for a city and view real-time weather information through a clean and user-friendly interface.

## Features

- Search weather by city name
- Display current temperature
- Show humidity and wind speed
- Display weather conditions
- Fetch live weather data using an external API
- Responsive design for desktop and mobile screens
- Error handling for invalid city names and unavailable data

## Tech Stack

### Frontend
- HTML
- CSS
- TypeScript
- Vite

### Backend
- Python
- Flask
- Flask-CORS

### API
- Open-Meteo Weather API

## Project Architecture

The application follows a frontend-backend architecture:

1. The user selects a city in the frontend.
2. The frontend sends a request to the Flask backend.
3. The backend fetches weather data from the Open-Meteo API.
4. The backend processes the response.
5. The frontend displays the weather information to the user.

## Folder Structure

```text
PROJECT-1/
│
├── backend/
│   ├── app.py
│   ├── requirements.txt
│   └── .venv/
│
├── frontend/
│   ├── index.html
│   ├── main.ts
│   ├── styles.css
│   ├── vite.config.ts
│   ├── package.json
│   └── vite-env.d.ts
│
├── .gitignore
└── README.md