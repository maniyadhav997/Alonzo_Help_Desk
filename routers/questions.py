from fastapi import APIRouter, HTTPException
from models.question_model import Question
from models.answer_model import Answer
from utils.file_handler import load_json, save_json
from uuid import uuid4, UUID
from datetime import datetime, timezone
from typing import Optional
from pathlib import Path

router = APIRouter()
questions_path = Path("data/questions.json")
answers_path = Path("data/answers.json")

@router.get("/")
def list_questions(
    tag: Optional[str] = None,
    is_answered: Optional[bool] = None,
    search: Optional[str] = None,
    sort: Optional[str] = None
):
    questions = load_json(questions_path)

    if tag:
        questions = [q for q in questions if tag in q.get("tags", [])]
    
    if is_answered is not None:
        questions = [q for q in questions if q.get("is_answered") == is_answered]

    if search:
        search = search.lower()
        questions = [
            q for q in questions
            if search in q.get("title", "").lower() or search in q.get("content", "").lower()
        ]

    if sort == "created_at":
        questions.sort(key=lambda x: x.get("created_at", ""), reverse=True)
    elif sort == "views":
        questions.sort(key=lambda x: x.get("views", 0), reverse=True)
    elif sort == "answers_count":
        questions.sort(key=lambda x: len(x.get("answer_ids", [])), reverse=True)

    return questions

@router.get("/{id}")
def get_question(id: UUID):
    questions = load_json(questions_path)
    answers = load_json(answers_path)

    for q in questions:
        if str(q["id"]) == str(id):
            q_answers = [a for a in answers if str(a["question_id"]) == str(id)]
            return {"question": q, "answers": q_answers}

    raise HTTPException(status_code=404, detail="Question not found")

@router.post("/")
def create_question(q: Question):
    questions = load_json(questions_path)
    question = q.model_dump()

    question["id"] = str(uuid4())
    question["created_at"] = datetime.now(timezone.utc).isoformat()
    question["views"] = 0
    question["is_answered"] = False
    question["answer_ids"] = []

    questions.append(question)
    save_json(questions_path, questions)
    return question

@router.put("/{id}")
def update_question(id: UUID, data: dict):
    questions = load_json(questions_path)
    for q in questions:
        if str(q["id"]) == str(id):
            q.update({k: v for k, v in data.items() if k in {"title", "content", "tags"}})
            save_json(questions_path, questions)
            return q
    raise HTTPException(status_code=404, detail="Question not found")

@router.delete("/{id}")
def delete_question(id: UUID):
    questions = load_json(questions_path)
    new_questions = [q for q in questions if str(q["id"]) != str(id)]

    if len(new_questions) == len(questions):
        raise HTTPException(status_code=404, detail="Question not found")

    save_json(questions_path, new_questions)
    return {"message": "Question deleted"}

@router.patch("/{id}/increment-view")
def increment_view(id: UUID):
    questions = load_json(questions_path)
    for q in questions:
        if str(q["id"]) == str(id):
            q["views"] += 1
            save_json(questions_path, questions)
            return {"views": q["views"]}
    raise HTTPException(status_code=404, detail="Question not found")
