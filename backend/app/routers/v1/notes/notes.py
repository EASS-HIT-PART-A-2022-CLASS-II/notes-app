from fastapi import APIRouter, Body
from db.repository.notes import ( retrieve_notes, add_note, retrieve_note, update_note, delete_note, retrieve_notes_by_title )
from models.note import ( Note, ResponseModel, ErrorResponseModel )
from fastapi.encoders import jsonable_encoder

router = APIRouter()

@router.get("/")
async def get_notes():
    notes = await retrieve_notes()
    if notes:
        return ResponseModel(notes, "Notes data retrieved successfully")
    return ResponseModel(notes, "Empty list returned")

@router.get("/{id}")
async def get_note_data(id: str):
    note = await retrieve_note(id)
    if note:
        return ResponseModel(note, "Student data retrieved successfully")
    return ErrorResponseModel("An error occurred.", 404, "Student doesn't exist.")

@router.get("/search_notes")
async def search_notes(title: str):
    notes = await retrieve_notes_by_title(title)
    if notes:
        return ResponseModel(notes, "Notes data retrieved successfully")
    return ResponseModel(notes, "Empty list returned")

@router.post("/")
async def add_note_data(note: Note = Body(...)):
    note = jsonable_encoder(note)
    new_note = await add_note(note)
    return ResponseModel(new_note, "Student added successfully.")

@router.delete("/{id}")
async def delete_note_data(id: str):
    deleted_note = await delete_note(id)
    if deleted_note:
        return ResponseModel(
            "Note with ID: {} removed".format(id), "Note deleted successfully"
        )
    return ErrorResponseModel(
        "An error occurred", 404, "Note with id {0} doesn't exist".format(id)
    )

@router.put("/{id}")
async def update_note_data(id: str, req: Note = Body(...)):
    req = {k: v for k, v in req.dict().items() if v is not None}
    updated_note = await update_note(id, req)
    if updated_note:
        return ResponseModel(
            "Note with ID: {} update is successfully".format(id),
            "Note updated successfully",
        )
    return ErrorResponseModel(
        "An error occurred",
        404,
        "There was an error updating the note data.",
    )