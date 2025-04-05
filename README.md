# 🧠 Alonzo Help Desk - FastAPI Q&A System

This is a simple internal FAQ and Q&A system built with **FastAPI**, using **JSON files for storage**. It supports managing questions, answers, tags, and user favorite lists.

---

## 🚀 Features

- Add, update, delete questions
- Add, update, delete answers
- Upvote and accept answers
- Filter and sort questions by tags, views, answer count, etc.
- Manage tags dynamically from questions
- Add/retrieve favorite questions and answers per user

---

## 📁 Project Structure
alonzo-helpdesk-api/
│
├── app/
│   ├── main.py                      # FastAPI app entry point
│   │
│   ├── routers/                     # Route handlers
│   │   ├── answer.py
│   │   ├── question.py
│   │   ├── tags.py
│   │   └── user.py
│   │
│   ├── models/                      # Pydantic models
│   │   ├── answer_model.py
│   │   ├── question_model.py
│   │   └── user_model.py
│   │
│   ├── utils/                       # Reusable utilities
│   │   └── file_handler.py
│
├── data/                            # JSON storage files
│   ├── questions.json
│   ├── answers.json
│   └── users.json
│
├── README.md
├── requirements.txt

---

## 📦 Setup Instructions

1. **Clone the Repository**
   ```bash
   git clone <your-repo-url>
   cd alonzo-helpdesk-api
Install Dependencies

bash
Copy
Edit
pip install fastapi uvicorn
Run the API

bash
Copy
Edit
uvicorn main:app --reload
Open in Browser

Swagger UI: http://localhost:8000/docs

ReDoc: http://localhost:8000/redoc

📘 API Endpoints
🔹 Questions
GET /questions - List questions (filters: tag, is_answered, search, sort)

GET /questions/{id} - Get a specific question with answers

POST /questions - Create a question

PUT /questions/{id} - Update question title/content/tags

DELETE /questions/{id} - Delete a question

PATCH /questions/{id}/increment-view - Increment question views

🔹 Answers
POST /answers/{question_id}/answers - Add an answer to a question

PUT /answers/{id} - Edit answer content

DELETE /answers/{id} - Delete an answer

PATCH /answers/{id}/upvote - Upvote an answer

PATCH /answers/{id}/accept - Accept an answer

🔹 Tags
GET /tags - List all tags with count

GET /tags/{tag}/questions - List questions with a given tag

🔹 User Favorites
POST /users/favorites - Add favorite question/answer for user (by email)

GET /users/{email}/favorites - Get a user’s favorite question & answer IDs

📄 Sample users.json
json
Copy
Edit
[
  {
    "email": "user@example.com",
    "favorite_questions": ["question-uuid"],
    "favorite_answers": ["answer-uuid"]
  }
]
🛠 Technologies Used
FastAPI for building the RESTful API

Pydantic for data validation

UUID for unique object identification

JSON file-based persistence

🙌 Contribution
Feel free to fork this repo and open a pull request for improvements or feature suggestions!

📫 Contact
For questions or issues, feel free to reach out at yadavmani8543@gmail.com.

