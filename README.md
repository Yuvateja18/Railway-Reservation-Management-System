# 🚆 Railway Reservation Management System (Python CLI)

This is a simple Python-based Railway Reservation Management System that allows users to search for trains between two stations on a specific day and choose their preferred coach class. The script simulates a train database and interacts with the user via the command line.

📋 Features
🗺️ View Available Origin & Destination Stations

🔍 Search for Trains by origin, destination, and day of travel

🛏️ Coach Preference Selection (Sleeper or AC)

💰 Fare & Seat Information Display

📅 Filters Trains Based on Travel Day

💡 How It Works
The script maintains a static list of trains, each with:

Train number and name

Origin and destination stations

Operating days

Coach types with available seats and fare

The user is prompted to:

Choose an origin station

Choose a valid destination station from that origin

Enter the day of travel

Enter their coach preference (Sleeper/AC)

The system filters the matching trains based on user input and displays:

Train number, name

Selected coach details: available seats and fare

