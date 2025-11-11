# Intelligent Parking System - Minor Project
🅿️ Intelligent Parking System
An AI-assisted Smart Parking Management System designed to automate parking slot detection, vehicle entry management, and real-time parking updates for users.

🚀 Overview
The Intelligent Parking System (IPS) aims to solve one of the most common urban challenges — finding and managing parking efficiently.
It uses computer vision, Flask-based web application, and real-time data monitoring to:

Detect available parking slots

Display parking layout visually

Manage entry/exit logs

Provide admin dashboard for monitoring

🧠 Features
✅ Real-time parking slot detection
✅ Vehicle entry & exit logging
✅ Admin dashboard for parking overview
✅ Interactive web UI (Flask + HTML/CSS + JS)
✅ Database connectivity for persistent records
✅ Error handling and alert banners for feedback

🧩 Tech Stack
Category	Technology Used
Frontend	HTML5, CSS3, JavaScript, Bootstrap
Backend	Python (Flask Framework)
Database	SQLite / MySQL (configurable)
AI / CV	OpenCV, NumPy (for slot detection)
Others	Git, VS Code, Jinja2 templates

⚙️ Setup Instructions
🔹 Clone the Repository
bash
Copy code
git clone https://github.com/Nisha8817/Intelligent_Parking_System.git
cd Intelligent_Parking_System
🔹 Create Virtual Environment
bash
Copy code
python -m venv venv
venv\Scripts\activate     # for Windows
# or
source venv/bin/activate  # for Linux/Mac
🔹 Install Dependencies
bash
Copy code
pip install -r requirements.txt
🔹 Run the Application
bash
Copy code
python IPS_app.py
Then open your browser and go to:
👉 http://127.0.0.1:5000/

📂 Folder Structure
cpp
Copy code
Intelligent_Parking_System/
│
├── Backend/
│   ├── database.py
│   ├── detection.py
│   └── ...
│
├── static/
│   ├── css/
│   ├── js/
│   └── images/
│
├── templates/
│   ├── index.html
│   ├── admin.html
│   └── ...
│
├── IPS_app.py
├── requirements.txt
└── README.md
📸 Screenshots
(Add your screenshots here after upload)
Example:

scss
Copy code
![Dashboard View](static/images/dashboard.png)
![Slot Detection](static/images/slot_detection.png)


🚧 Future Enhancements
Integration with IoT sensors for real-time slot monitoring

Mobile app version (Flutter / React Native)

License plate recognition for automatic entry

Payment gateway for automated billing


**Contributors Name**: Lokesh Yadav, Nirmal Choudhary, Nisha Mandiwal

