the backend for Alonzo Help Desk, an internal FAQ and Q&A system for users to ask and answer questions, upvote helpful answers, and tag content for easy discovery. All data is stored using JSON files — no database.
Architecture
Framework: FastAPI
Storage: JSON files
Models: Pydantic
Functionality: RESTful API for everything

Entities & Fields
❓ Question
{
  "id": "uuid",
  "title": "How to reset my password?",
  "content": "I'm unable to reset my password using the link...",
  "tags": ["account", "password"],
  "created_by": "user@example.com",
  "created_at": "2025-04-03T10:00:00Z",
  "is_answered": true,
  "views": 12,
  "answer_ids": ["uuid1", "uuid2"]
}

📝 Answer
{
  "id": "uuid",
  "question_id": "uuid",
  "content": "Go to settings > Security > Reset Password.",
  "created_by": "admin@example.com",
  "created_at": "2025-04-03T10:05:00Z",
  "upvotes": 4,
  "is_accepted": true
}
API Endpoints
📘 Question APIs
GET /questions: List all questions
Optional filters: tag, is_answered, search=<term>
Optional sort: created_at, views, answers_count
GET /questions/{id}: Get a question and its answers
POST /questions: Create a new question
PUT /questions/{id}: Update title/content/tags
DELETE /questions/{id}: Delete a question
PATCH /questions/{id}/increment-view: Increase view count by 1
📝 Answer APIs
POST /questions/{question_id}/answers: Add answer to question
PUT /answers/{id}: Edit answer
DELETE /answers/{id}: Delete answer
PATCH /answers/{id}/upvote: Upvote an answer
PATCH /answers/{id}/accept: Mark answer as accepted
 Tag APIs
GET /tags: List all tags with count of questions per tag
GET /tags/{tag}/questions: Get all questions for a tag
🔐 Authentication
No real user system — created_by is a free-form string (e.g., email) passed in payload
You may later replace this with actual auth
🗃️ JSON File Storage
questions.json → stores list of all questions
answers.json → stores list of all answers
Ensure all file operations are read-safe/write-safe (you can use file locks or load/save patterns).
🛠️ Example File Structure
alonzo_helpdesk/
├── main.py
├── models/
│   ├── question.py
│   └── answer.py
├── routers/
│   ├── questions.py
│   ├── answers.py
│   └── tags.py
├── data/
│   ├── questions.json
│   └── answers.json
| - README.md
| - requirements.txt
