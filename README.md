🧠 Alonzo Help Desk
A lightweight, internal Q&A system built using FastAPI and JSON-based storage. It allows users to manage questions, answers, and tags—and also save favorite questions and answers.

🚀 Features
✅ Add, view, update, and delete questions

✅ Add, edit, delete, upvote, and accept answers

✅ Filter and sort questions by tag, view count, or answer count

✅ View all available tags

✅ Users can maintain a personal list of favorite questions and answers

📁 Project Structure
pgsql
Copy
Edit
alonzo-help-desk/
├── main.py
├── models/
│   ├── question_model.py
│   ├── answer_model.py
│   └── user_model.py
├── routers/
│   ├── question.py
│   ├── answer.py
│   └── tags.py
│   └── user.py
├── utils/
│   └── file_handler.py
└── data/
    ├── questions.json
    ├── answers.json
    └── users.json
🔧 Installation & Run
1. Clone the repo
bash
Copy
Edit
git clone https://github.com/your-username/alonzo-help-desk.git
cd alonzo-help-desk
2. Create a virtual environment
bash
Copy
Edit
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
3. Install dependencies
bash
Copy
Edit
pip install fastapi uvicorn
4. Run the app
bash
Copy
Edit
uvicorn main:app --reload
Open in browser: http://127.0.0.1:8000/docs for Swagger UI.

📬 API Endpoints Summary
📌 Questions
GET /questions: List all questions (filterable)

POST /questions: Create a new question

GET /questions/{id}: View question with answers

PUT /questions/{id}: Edit a question

DELETE /questions/{id}: Delete a question

PATCH /questions/{id}/increment-view: Increase view count

💬 Answers
POST /answers/{question_id}/answers: Add answer to question

PUT /answers/{id}: Edit answer

DELETE /answers/{id}: Delete answer

PATCH /answers/{id}/upvote: Upvote answer

PATCH /answers/{id}/accept: Mark answer as accepted

🏷️ Tags
GET /tags: List all tags with counts

GET /tags/{tag}/questions: List questions by tag

👤 User Favorites
POST /users/{email}/favorites: Add/update favorites

GET /users/{email}/favorites: Get favorite questions/answers

📂 Sample JSON Files
All data is stored in the /data directory in .json files:

questions.json

answers.json

users.json

Each file is automatically updated by API actions.

📌 Dependencies
Python 3.7+

FastAPI

Uvicorn

📞 Contact
Made by [Your Name] — feel free to connect for feedback or ideas!
