from db import database
from bson.objectid import ObjectId

# init
notes_collection = database.collection

# helpers
def note_helper(note)-> dict:
    return {
        "id": str(note["_id"]),
        "title": note["title"],
        "description": note["description"]
    }

# Retrieve all notes present in the database
async def retrieve_notes():    
    notes = []
    async for note in notes_collection.find():
        notes.append(note_helper(note))
    return notes

# Add a new note into to the database
async def add_note(note_data: dict) -> dict:
    note = await notes_collection.insert_one(note_data)
    new_note = await notes_collection.find_one({"_id": note.inserted_id})
    return note_helper(new_note)

# Retrieve a note with a matching ID
async def retrieve_note(id: str) -> dict:
    note = await notes_collection.find_one({"_id": ObjectId(id)})
    if note:
        return note_helper(note)

async def retrieve_notes_by_title(title: str):
    notes = []
    async for note in notes_collection.find({title: title}):
        notes.append(note_helper(note))
    return notes

# Update a note with a matching ID
async def update_note(id: str, data: dict):
    # Return false if an empty request body is sent.
    if len(data) < 1:
        return False
    note = await notes_collection.find_one({"_id": ObjectId(id)})
    if note:
        updated_note = await notes_collection.update_one(
            {"_id": ObjectId(id)}, {"$set": data}
        )
        if updated_note:
            return True
        return False

# Delete a note from the database
async def delete_note(id: str):
    note = await notes_collection.find_one({"_id": ObjectId(id)})
    if note:
        await notes_collection.delete_one({"_id": ObjectId(id)})
        return True