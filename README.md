# 🛡️ Safe Space: Women Safety AI NextGen

Safe Space is a comprehensive, sophisticated web platform dedicated to women's safety and well-being. Modernized with a unified Django architecture and a premium user interface, the platform offers rapid emergency assistance, support ticketing, legal resource accessibility, and real-time communication tools thoughtfully integrated to empower and protect users.

## ✨ Key Features

- **Global SOS Button:** A persistent, dynamic floating SOS button available on every page for immediate emergency access.
- **Emergency Directory:** Quick access to essential contacts, helplines, and nearby safe spaces.
- **Complaint Management System:** A robust backend pipeline (powered by the `ContactTicket` model) to seamlessly capture, manage, and process user support tickets and evidence.
- **Real-time Chat Interface:** A modernized chat UI featuring intuitive input areas and clear formatting for sharing location data.
- **Voice Capabilities:** Integrated voice backend modules designed for rapid interaction. 
- **Modern UI/UX:** A stunning, highly responsive frontend design employing a unified design system, modern aesthetics, and clean routing.

## 🛠️ Technology Stack

- **Frontend:** HTML5, modern Vanilla CSS (custom design variables, polished animations), JavaScript
- **Backend:** Django (Python)
- **Database:** SQLite (Django default) / Configurable via settings

## 📁 Project Structure

```text
WOMEN_SAFETY_AI_NEXTGEN/
├── women_safety/       # Main Django project settings and base routing
├── support/            # Support ticket, complaint, and contact backend app
├── users/              # User authentication and profile management
├── voice/              # Voice backend and processing modules
├── templates/          # Django unified HTML templates (index, chat, emergency, etc.)
├── static/             # Static assets (global CSS, images, icons)
└── manage.py           # Django CLI execution script
```

## 🚀 Local Setup & Installation

Follow these steps to get the project running locally on your machine:

**1. Clone the repository**
```bash
git clone https://github.com/SHEEBHA2212/WOMEN_SAFETY_AI_NEXTGEN.git
cd WOMEN_SAFETY_AI_NEXTGEN
```

**2. Create a virtual environment**
```bash
python -m venv venv
```

**3. Activate the virtual environment**
- **Windows:**
  ```powershell
  .\venv\Scripts\activate
  ```
- **macOS/Linux:**
  ```bash
  source venv/bin/activate
  ```

**4. Install required packages**
Ensure Django and any other Python dependencies are installed.
```bash
pip install django
```

**5. Apply Database Migrations**
Prepare your local database with the latest schema changes.
```bash
python manage.py makemigrations
python manage.py migrate
```

**6. Start the Development Server**
```bash
python manage.py runserver
```
Finally, navigate to `http://localhost:8000/` in your web browser to explore the platform!

## 🤝 Contributing
Contributions, issues, and feature requests are always welcome! Feel free to explore the code and propose updates to make Safe Space even better.

---
*Built to empower and protect. Made with ❤️ for a safer tomorrow.*