```markdown
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

```
.
├── main.py
├── routers/
│   ├── question.py
│   ├── answer.py
│   └── tags.py
├── models/
│   ├── question_model.py
│   ├── answer_model.py
│   └── user_model.py
├── utils/
│   └── file_handler.py
├── data/
│   ├── questions.json
│   ├── answers.json
│   └── users.json
```

---

## 🛠️ Setup Instructions

1. **Install dependencies**  
```bash
pip install fastapi uvicorn
```

2. **Run the server**  
```bash
uvicorn main:app --reload
```

3. **API Docs**  
Visit: `http://localhost:8000/docs`

---

## 🧪 Sample Endpoints & Usage

### 🔹 Questions

- **Create a question**
```bash
POST /questions
```

```json
{
  "title": "What is FastAPI?",
  "content": "Can someone explain how FastAPI works?",
  "tags": ["python", "api"],
  "created_by": "admin@example.com",
  "created_at": "2025-04-05T10:00:00",
  "is_answered": false,
  "views": 0,
  "answer_ids": []
}
```

- **List questions**
```bash
GET /questions?tag=python&sort=views
```

- **Get a specific question**
```bash
GET /questions/{id}
```

---

### 🔹 Answers

- **Add answer**
```bash
POST /answers/{question_id}/answers
```

```json
{
  "id": "string",
  "quiestion_id": "string",
  "content": "FastAPI is a modern web framework.",
  "created_by": "user@example.com",
  "is_answerd": false
}
```

- **Upvote answer**
```bash
PATCH /answers/{id}/upvote
```

- **Accept answer**
```bash
PATCH /answers/{id}/accept
```

---

### 🔹 Tags

- **List tags with counts**
```bash
GET /tags
```

- **Get questions by tag**
```bash
GET /tags/{tag}/questions
```

---

### 🔹 Users - Favorite List

- **Add/Update user favorites**
```bash
POST /users/favorites
```

```json
{
  "email": "user@example.com",
  "favorite_questions": ["<question_id_1>", "<question_id_2>"],
  "favorite_answers": ["<answer_id_1>"]
}
```

- **Get user favorites**
```bash
GET /users/favorites/{email}
```

---

## 📦 Data Format

### Example `users.json`

```json
[
  {
    "email": "user@example.com",
    "favorite_questions": ["<uuid>", "<uuid>"],
    "favorite_answers": ["<uuid>"]
  }
]
```

---
