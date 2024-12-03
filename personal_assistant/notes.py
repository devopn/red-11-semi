import json
from datetime import datetime


class Note:
    def __init__(self, note_id, title, content, timestamp=None):
        self.id = note_id
        self.title = title
        self.content = content
        self.timestamp = timestamp or datetime.now().strftime("%d-%m-%Y %H:%M:%S")

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "content": self.content,
            "timestamp": self.timestamp,
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            note_id=data["id"],
            title=data["title"],
            content=data["content"],
            timestamp=data["timestamp"],
        )


class NoteManager:
    FILE_NAME = "notes.json"

    def __init__(self):
        self.notes = self.load_notes()

    def load_notes(self):
        try:
            with open(self.FILE_NAME, "r", encoding="utf-8") as file:
                data = json.load(file)
                return [Note.from_dict(note) for note in data]
        except (FileNotFoundError, json.JSONDecodeError):
            return []

    def save_notes(self):
        with open(self.FILE_NAME, "w", encoding="utf-8") as file:
            json.dump([note.to_dict() for note in self.notes], file, ensure_ascii=False, indent=4)

    def create_note(self, title, content):
        new_id = max((note.id for note in self.notes), default=0) + 1
        new_note = Note(note_id=new_id, title=title, content=content)
        self.notes.append(new_note)
        self.save_notes()
        return new_note

    def list_notes(self):
        return self.notes

    def get_note_by_id(self, note_id):
        return next((note for note in self.notes if note.id == note_id), None)

    def update_note(self, note_id, title=None, content=None):
        note = self.get_note_by_id(note_id)
        if note:
            if title:
                note.title = title
            if content:
                note.content = content
            note.timestamp = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
            self.save_notes()
            return note
        return None

    def delete_note(self, note_id):
        self.notes = [note for note in self.notes if note.id != note_id]
        self.save_notes()

    def export_to_csv(self, filename):
        import csv

        with open(filename, "w", newline="", encoding="utf-8") as file:
            writer = csv.DictWriter(file, fieldnames=["id", "title", "content", "timestamp"])
            writer.writeheader()
            for note in self.notes:
                writer.writerow(note.to_dict())

    def import_from_csv(self, filename):
        import csv

        with open(filename, "r", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            for row in reader:
                self.create_note(
                    title=row["title"],
                    content=row["content"],
                )
