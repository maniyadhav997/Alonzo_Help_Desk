from fastapi import APIRouter, HTTPException
from models.user_model import User
from utils.file_handler import load_json, save_json
from pathlib import Path
from uuid import UUID

router = APIRouter()
users_path = Path("data/users.json")
questions_path = Path("data/questions.json")
answers_path = Path("data/answers.json")

@router.post("")
def update_user_favorites(user: User):
    users = load_json(users_path)
    user_dict = user.dict()
    found = False

    for u in users:
        if u["email"] == user.email:
            u["favorite_questions"] = [str(qid) for qid in user.favorite_questions]
            u["favorite_answers"] = [str(aid) for aid in user.favorite_answers]
            found = True
            break

    if not found:
        user_dict["favorite_questions"] = [str(qid) for qid in user.favorite_questions]
        user_dict["favorite_answers"] = [str(aid) for aid in user.favorite_answers]
        users.append(user_dict)

    save_json(users_path, users)
    return {"message": "User favorites updated"}

@router.get("/{email}")
def get_user_favorites(email: str):
    users = load_json(users_path)
    questions = load_json(questions_path)
    answers = load_json(answers_path)

    for u in users:
        if u["email"] == email:
            fav_questions = [q for q in questions if q["id"] in u["favorite_questions"]]
            fav_answers = [a for a in answers if a["id"] in u["favorite_answers"]]
            return {
                "email": email,
                "favorite_questions": fav_questions,
                "favorite_answers": fav_answers
            }

    raise HTTPException(status_code=404, detail="User not found")
