from fastapi import APIRouter
from utils.file_handler import load_json
from pathlib import Path
from collections import defaultdict

router = APIRouter()
questions_path = Path("data/questions.json")

@router.get("/")
def list_tags():
    questions = load_json(questions_path)
    tag_counts = defaultdict(int)

    for q in questions:
        for tag in q.get("tags", []):
            tag_counts[tag] += 1

    # Optional: return sorted tags by popularity
    return dict(sorted(tag_counts.items(), key=lambda x: x[1], reverse=True))

@router.get("/{tag}/questions")
def get_questions_by_tag(tag: str):
    questions = load_json(questions_path)
    return [q for q in questions if tag in q.get("tags", [])]
