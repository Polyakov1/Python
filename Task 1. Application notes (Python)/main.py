import json
import os
from time import gmtime, strftime


class Note:
    def __init__(self, id, title, content, timestamp):
        self.id = id
        self.title = title
        self.content = content
        self.timestamp = timestamp

class NotesApp:
    def __init__(self):
        self.notes = []
        self.filepath = "notes.json"

        if os.path.exists(self.filepath):
            self.load_notes()

    def load_notes(self):
        with open(self.filepath, "r") as file:
            notes_data = json.load(file)

            for note_data in notes_data:
                note = Note(note_data["id"], note_data["title"], note_data["content"], note_data["timestamp"])
                self.notes.append(note)

    def save_notes(self):
        notes_data = []
        
        for note in self.notes:
            note_data = {
                "id": note.id,
                "title": note.title,
                "content": note.content,
                "timestamp": note.timestamp
            }
            notes_data.append(note_data)

        with open(self.filepath, "w") as file:
            json.dump(notes_data, file, indent=4)

    def add_note(self, title, content):
        new_id = len(self.notes) + 1
        timestamp = strftime("%Y-%m-%d %H:%M:%S", gmtime())
        new_note = Note(new_id, title, content, timestamp)
        self.notes.append(new_note)
        self.save_notes()

    def edit_note(self, note_id, title, content):
        for note in self.notes:
            if note.id == note_id:
                note.title = title
                note.content = content
                note.timestamp = strftime("%Y-%m-%d %H:%M:%S", gmtime())
                self.save_notes()
                return True

        return False

    def delete_note(self, note_id):
        for note in self.notes:
            if note.id == note_id:
                self.notes.remove(note)
                self.save_notes()
                return True

        return False

    def display_notes(self):
        for note in self.notes:
            print(f"ID: {note.id}")
            print(f"Title: {note.title}")
            print(f"Content: {note.content}")
            print(f"Timestamp: {note.timestamp}")
            print("---")

app = NotesApp()

while True:
    print("1. Add Note")
    print("2. Edit Note")
    print("3. Delete Note")
    print("4. Display Notes")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        title = input("Enter note title: ")
        content = input("Enter note content: ")
        app.add_note(title, content)

    elif choice == "2":
        note_id = input("Enter note ID: ")
        title = input("Enter new title: ")
        content = input("Enter new content: ")

        if not app.edit_note(int(note_id), title, content):
            print("Note not found.")

    elif choice == "3":
        note_id = input("Enter note ID: ")

        if not app.delete_note(int(note_id)):
            print("Note not found.")

    elif choice == "4":
        app.display_notes()

    elif choice == "5":
        break

    else:
        print("Invalid choice. Please try again.")
