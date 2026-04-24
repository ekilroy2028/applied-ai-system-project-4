🐾 PawPal+

PawPal+ is a smart pet care management system that helps pet owners organize and prioritize daily responsibilities such as feeding, walking, medications, and appointments.

Built using Python and object-oriented programming (OOP), PawPal+ combines clean system design with algorithmic scheduling logic and an interactive Streamlit interface.

🚀 Features
🐶 Pet & Task Management
Add multiple pets under one owner
Assign tasks with time and frequency (once, daily, weekly)
Track task completion status
⏰ Smart Scheduling
Automatically sorts tasks by time
Displays a clean daily schedule
🔍 Filtering
Filter tasks by:
Pet name
Completion status
🔁 Recurring Tasks
Daily and weekly tasks regenerate automatically after completion
⚠️ Conflict Detection
Detects tasks scheduled at the same time
Provides warnings instead of breaking the system
🧠 Smarter Scheduling
- Sorts tasks automatically by time
- Detects scheduling conflicts
- Supports daily and weekly recurring tasks
- Filters tasks by pet and completion status


The system is built using four main classes:

Task → Represents an individual activity
Pet → Stores pet details and task list
Owner → Manages multiple pets
Scheduler → Handles sorting, filtering, recurrence, and conflicts
🖥️ How to Run the Project
1. Run CLI Demo
python main.py
2. Run Streamlit App
streamlit run app.py
🧪 Testing PawPal+

Run the automated test suite with:

python -m pytest
✅ Tests Cover:
Task completion behavior
Adding tasks to pets
Sorting correctness
Conflict detection
Recurring task generation

Confidence Level: ⭐⭐⭐⭐⭐ (5/5)
All core features are tested and working reliably.

📸 Demo

(Add your screenshot here)

<a href="/course_images/ai110/paw_screenshot.png" target="_blank">
  <img src='/course_images/ai110/paw_screenshot.png' title='PawPal App' width='' alt='PawPal App' />
</a>
<a href="/course_images/ai110/pawpal_screenshot.png" target="_blank">
  <img src='/course_images/ai110/pawpal_screenshot.png' title='PawPal App' alt='PawPal App'/>
</a>

🧩 Smarter Scheduling

PawPal+ includes algorithmic improvements that make it more than a simple task list:

Uses Python’s sorted() with lambda functions for efficient time-based ordering
Implements lightweight conflict detection using hash maps
Automates recurring tasks using datetime and timedelta
Keeps logic modular through a dedicated Scheduler class
📦 Tech Stack
Python
Object-Oriented Programming (OOP)
Streamlit
Pytest
👩‍💻 Author

Elizabeth Kilroy