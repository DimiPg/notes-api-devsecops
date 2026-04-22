from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="Notes DevSecOps API")

notes_db: list[dict] = []


class NoteCreate(BaseModel):
    title: str
    content: str


@app.get("/health")
def health():
    return {"status": "ok"}


@app.get("/notes")
def get_notes():
    return {"notes": notes_db}


@app.post("/notes", status_code=201)
def create_note(note: NoteCreate):
    new_note = {
        "id": len(notes_db) + 1,
        "title": note.title,
        "content": note.content,
    }
    notes_db.append(new_note)
    return new_note