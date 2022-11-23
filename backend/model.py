from mongoengine import Document, StringField, IntField

class Note(Document):
    note_id = IntField()
    title = StringField()
    description = StringField()
