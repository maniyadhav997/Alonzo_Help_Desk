from fastapi import FastAPI
from routers import questions, answers, tags

import json

app = FastAPI()


app.include_router(questions.router, prefix='/questions', tags=["Questions"])
app.include_router(answers.router, prefix='/answers', tags=["Answers"])
app.include_router(tags.router, prefix='/tags', tags=["Tags"])

