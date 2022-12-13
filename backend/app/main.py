from fastapi import FastAPI
from core.config import settings
from routers.v1.notes.notes import router as NotesRouter

app = FastAPI(title=settings.PROJECT_NAME, version=settings.PROJECT_VERSION)
app.include_router(NotesRouter, tags=["Notes"], prefix="/v1/notes")

@app.get("/")
async def root():
    return {"message": "This will be the main window of the Notes APP!!"}
