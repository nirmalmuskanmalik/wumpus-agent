Wumpus World Logic Agent (Web App)
A dynamic web-based Knowledge-Based AI Agent that navigates a Wumpus World grid using percepts and basic logical inference to avoid hazards and find gold.

Features
Dynamic grid size (user-defined)
Random placement of:
Pits
Wumpus 
Gold

----------------------------------------------------------------

Real-time percept generation:
Breeze (near pit)
Stench (near Wumpus)
Agent movement simulation

----------------------------------------------------------------

Game termination conditions:
Finds Gold (Win)
Falls into Pit (Lose)
Meets Wumpus (Lose)
Step counter + live status display
Web-based interactive visualization

----------------------------------------------------------------

Tech Stack
Backend: Python (Flask)
Frontend: HTML, CSS, JavaScript
API: REST (Flask endpoints)
Communication: Fetch API

----------------------------------------------------------------

Project Structure

wumpus_agent/
│
├── backend/
│   ├── app.py
│   ├── agent.py
│
├── frontend/
│   ├── index.html
│   ├── script.js
│   ├── style.css
│
└── README.md

----------------------------------------------------------------

How to Run Locally
1. Install dependencies
Bash

pip install flask flask-cors
2. Run backend
Bash

cd backend
python app.py
3. Run frontend
Open frontend/index.html using Live Server (VS Code)

---------------------------------------------------------------

API Endpoints:
POST /init → Initializes grid

GET /step → Moves agent one step

---------------------------------------------------------------

Project Goal:
To simulate a Knowledge-Based Agent that uses percepts and logical reasoning to safely navigate an unknown environment and reach a goal while avoiding hazards.

Status Features
Current Position
Steps Taken
Percepts (Breeze, Stench)
Game Result (Win/Lose/Playing)

----------------------------------------------------------------

Author
NIRMAL MUSKAN