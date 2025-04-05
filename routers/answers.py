from fastapi import APIRouter, HTTPException
from utils.file_handler import load_json, save_json
from uuid import uuid4, UUID
from datetime import datetime
from pathlib import Path

router = APIRouter()
answers_path = Path("data/answers.json")
questions_path = Path("data/questions.json")

@router.post("/{question_id}/answers")
def add_answer(question_id: UUID, answer_data: dict):
    answers = load_json(answers_path)
    questions = load_json(questions_path)

    question_found = None
    for q in questions:
        if str(q["id"]) == str(question_id):
            question_found = q
            break

    if not question_found:
        raise HTTPException(status_code=404, detail="Question not found")

    new_answer = {
        "id": str(uuid4()),
        "question_id": str(question_id),
        "content": answer_data.get("content", "").strip(),
        "created_by": answer_data.get("created_by", "").strip(),
        "created_at": datetime.utcnow().isoformat(),
        "upvotes": 0,
        "is_accepted": False
    }

    answers.append(new_answer)
    question_found["answer_ids"].append(new_answer["id"])
    question_found["is_answered"] = True

    save_json(answers_path, answers)
    save_json(questions_path, questions)
    return new_answer

@router.put("/{id}")
def edit_answer(id: UUID, data: dict):
    answers = load_json(answers_path)
    for a in answers:
        if str(a["id"]) == str(id):
            a["content"] = data.get("content", a["content"]).strip()
            save_json(answers_path, answers)
            return a
    raise HTTPException(status_code=404, detail="Answer not found")

@router.delete("/{id}")
def delete_answer(id: UUID):
    answers = load_json(answers_path)
    new_answers = [a for a in answers if str(a["id"]) != str(id)]
    if len(new_answers) == len(answers):
        raise HTTPException(status_code=404, detail="Answer not found")
    save_json(answers_path, new_answers)
    return {"message": "Answer deleted"}

@router.patch("/{id}/upvote")
def upvote_answer(id: UUID):
    answers = load_json(answers_path)
    for a in answers:
        if str(a["id"]) == str(id):
            a["upvotes"] += 1
            save_json(answers_path, answers)
            return {"upvotes": a["upvotes"]}
    raise HTTPException(status_code=404, detail="Answer not found")

@router.patch("/{id}/accept")
def accept_answer(id: UUID):
    answers = load_json(answers_path)
    for a in answers:
        if str(a["id"]) == str(id):
            a["is_accepted"] = True
            save_json(answers_path, answers)
            return {"message": "Answer accepted"}
    raise HTTPException(status_code=404, detail="Answer not found")
