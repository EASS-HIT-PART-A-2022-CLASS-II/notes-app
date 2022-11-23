import json
from fastapi import FastAPI, Path
from model import Note
from mongoengine import connect
from pydantic import BaseModel
import os

app = FastAPI()
connect(db=os.getenv("db"), host="mongodb://notes-app-DB", port=int(os.getenv("db_port")))

class NewNote(BaseModel):
    note_id: int
    title: str
    description: str

def update_node_id_counter():
    if Note.objects.count() == 0:
        return 1
    else:
        return Note.objects.order_by("-note_id").first().note_id + 1

app.node_id_counter = update_node_id_counter()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/notes")
async def get_notes():
    return json.loads(Note.objects.order_by("+note_id").to_json())

@app.get("/notes/{note_id}")
async def get_note(note_id: int = Path(..., gt=0)):
    return json.loads(Note.objects.get(note_id=note_id).to_json())

@app.get("/search_note")
async def search_note(title):
    return json.loads(Note.objects.filter(title__icontains=title).to_json())

@app.post("/notes")
async def add_note(note: NewNote):
    note.note_id = app.node_id_counter
    app.node_id_counter += 1
    Note(note_id=note.note_id,
         title=note.title,
         description=note.description).save()
    return "Note successfully added :)"

@app.delete("/delete_note")
async def delete_note(note_id):
    Note.objects.get(note_id=note_id).delete()
    app.node_id_counter = update_node_id_counter()
    return "Note successfully deleted :)"

@app.put("/update_note/{note_id}")
async def update_note(note: NewNote, note_id: int = Path(..., gt=0)):
    curr_note = Note.objects.get(note_id = note_id)
    curr_note.title = note.title
    curr_note.description = note.description
    curr_note.save()
    return "Note successfully updated :)"

