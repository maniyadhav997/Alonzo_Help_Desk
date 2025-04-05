# Alonzo Help Desk API

A simple internal Q&A system built using **FastAPI** and **JSON-based storage**. Users can post questions, submit answers, upvote and accept answers, and manage favorite lists.

---

## Folder Structure

```
alonzo-helpdesk-api/
├── app/
│   ├── main.py                  # App entry
│   ├── routers/                 # All route handlers
│   │   ├── answer.py
│   │   ├── question.py
│   │   ├── tags.py
│   │   └── user.py
│   ├── models/                  # Pydantic models
│   │   ├── answer_model.py
│   │   ├── question_model.py
│   │   └── user_model.py
│   └── utils/                   # File handler
│       └── file_handler.py
├── data/                        # JSON files as database
│   ├── questions.json
│   ├── answers.json
│   └── users.json
├── README.md
├── requirements.txt
```

---

## Features

- Create, update, delete questions & answers
- Search, sort & filter questions
- Upvote & accept answers
- List tags & get questions by tag
- ⭐ Favorite questions & answers per user (by email)

---

## Setup Instructions

1. **Clone the Repo**
   ```bash
   git clone https://github.com/maniyadhav997/Alonzo_Help_Desk.git
   cd Alonzo_Help_Desk
   ```

2. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the App**
   ```bash
   uvicorn app.main:app --reload
   ```

4. **Open Docs**
   - Swagger: http://localhost:8000/docs
   - ReDoc: http://localhost:8000/redoc

---

## API Summary

### Questions
| Method | Endpoint | Description |
|--------|-------------------------------|-------------|
| GET    | `/questions`                 | List/filter/sort questions |
| GET    | `/questions/{id}`            | Retrieve specific question with answers |
| POST   | `/questions`                 | Create a new question |
| PUT    | `/questions/{id}`            | Edit question title/content/tags |
| DELETE | `/questions/{id}`            | Delete a question |
| PATCH  | `/questions/{id}/increment-view` | Increase view count |

### Answers
| Method | Endpoint | Description |
|--------|----------------------------------|-------------|
| POST   | `/answers/{question_id}/answers`| Post an answer |
| PUT    | `/answers/{id}`                 | Edit an answer |
| DELETE | `/answers/{id}`                 | Delete an answer |
| PATCH  | `/answers/{id}/upvote`          | Upvote an answer |
| PATCH  | `/answers/{id}/accept`          | Mark as accepted |

### Tags
| Method | Endpoint | Description |
|--------|----------------------------------|-------------|
| GET    | `/tags`                         | List all tags with frequency |
| GET    | `/tags/{tag}/questions`         | Questions with a specific tag |

### Favorites (User)
| Method | Endpoint | Description |
|--------|--------------------------------------|-------------|
| POST   | `/users/favorites`                  | Add favorite questions/answers |
| GET    | `/users/{email}/favorites`          | Retrieve user's favorite lists |

---

## Sample users.json

```json
[
  {
    "email": "alice@example.com",
    "favorite_questions": ["uuid-question-1", "uuid-question-2"],
    "favorite_answers": ["uuid-answer-1"]
  }
]
```

---

## Requirements

- Python 3.9+
- FastAPI
- Uvicorn

```
# requirements.txt
fastapi
uvicorn
```

---

## Author

Manikanta
yadavmani8543@gmail.com

