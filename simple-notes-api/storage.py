# START GENAI@CLINE
"""
Simple Notes Manager API - Storage Layer
Handles data persistence using JSON files
"""

import json
import os
from typing import List, Optional, Dict, Any
from models import Note


class NotesStorage:
    """
    Storage class for managing notes persistence using JSON files
    
    This class implements the Repository pattern, providing:
    - File-based storage using JSON
    - CRUD operations for notes
    - Search and filtering capabilities
    - Data integrity and error handling
    """
    
    def __init__(self, storage_file: str = "notes.json"):
        """
        Initialize storage with specified JSON file
        
        Args:
            storage_file (str): Path to JSON file for storage
        """
        self.storage_file = storage_file
        self._ensure_storage_file()
    
    def _ensure_storage_file(self) -> None:
        """Create storage file if it doesn't exist"""
        if not os.path.exists(self.storage_file):
            with open(self.storage_file, 'w') as f:
                json.dump([], f)
    
    def _load_notes(self) -> List[Dict[str, Any]]:
        """
        Load notes from JSON file
        
        Returns:
            List[Dict]: List of note dictionaries
        """
        try:
            with open(self.storage_file, 'r') as f:
                data = json.load(f)
                return data if isinstance(data, list) else []
        except (json.JSONDecodeError, FileNotFoundError):
            # If file is corrupted or missing, return empty list
            return []
    
    def _save_notes(self, notes_data: List[Dict[str, Any]]) -> bool:
        """
        Save notes to JSON file
        
        Args:
            notes_data (List[Dict]): List of note dictionaries
            
        Returns:
            bool: True if successful, False otherwise
        """
        try:
            # Create backup before saving
            if os.path.exists(self.storage_file):
                backup_file = f"{self.storage_file}.backup"
                with open(self.storage_file, 'r') as src, open(backup_file, 'w') as dst:
                    dst.write(src.read())
            
            # Save new data
            with open(self.storage_file, 'w') as f:
                json.dump(notes_data, f, indent=2, ensure_ascii=False)
            return True
        except Exception as e:
            print(f"Error saving notes: {e}")
            return False
    
    def create_note(self, note: Note) -> bool:
        """
        Create a new note in storage
        
        Args:
            note (Note): Note instance to save
            
        Returns:
            bool: True if successful, False otherwise
        """
        try:
            notes_data = self._load_notes()
            notes_data.append(note.to_dict())
            return self._save_notes(notes_data)
        except Exception as e:
            print(f"Error creating note: {e}")
            return False
    
    def get_note_by_id(self, note_id: str) -> Optional[Note]:
        """
        Retrieve a note by its ID
        
        Args:
            note_id (str): Unique identifier of the note
            
        Returns:
            Optional[Note]: Note instance if found, None otherwise
        """
        notes_data = self._load_notes()
        for note_data in notes_data:
            if note_data.get('id') == note_id:
                return Note.from_dict(note_data)
        return None
    
    def get_all_notes(self) -> List[Note]:
        """
        Retrieve all notes from storage
        
        Returns:
            List[Note]: List of all notes
        """
        notes_data = self._load_notes()
        notes = []
        for note_data in notes_data:
            try:
                notes.append(Note.from_dict(note_data))
            except Exception as e:
                print(f"Error loading note {note_data.get('id', 'unknown')}: {e}")
        return notes
    
    def update_note(self, note_id: str, updates: Dict[str, Any]) -> bool:
        """
        Update an existing note
        
        Args:
            note_id (str): ID of note to update
            updates (Dict): Fields to update
            
        Returns:
            bool: True if successful, False otherwise
        """
        try:
            notes_data = self._load_notes()
            
            for i, note_data in enumerate(notes_data):
                if note_data.get('id') == note_id:
                    # Load note, update it, and save back
                    note = Note.from_dict(note_data)
                    note.update(
                        title=updates.get('title'),
                        content=updates.get('content'),
                        tags=updates.get('tags')
                    )
                    notes_data[i] = note.to_dict()
                    return self._save_notes(notes_data)
            
            return False  # Note not found
        except Exception as e:
            print(f"Error updating note: {e}")
            return False
    
    def delete_note(self, note_id: str) -> bool:
        """
        Delete a note by ID
        
        Args:
            note_id (str): ID of note to delete
            
        Returns:
            bool: True if successful, False otherwise
        """
        try:
            notes_data = self._load_notes()
            original_length = len(notes_data)
            
            # Filter out the note to delete
            notes_data = [note for note in notes_data if note.get('id') != note_id]
            
            if len(notes_data) == original_length:
                return False  # Note not found
            
            return self._save_notes(notes_data)
        except Exception as e:
            print(f"Error deleting note: {e}")
            return False
    
    def search_notes(self, query: str) -> List[Note]:
        """
        Search notes by title and content
        
        Args:
            query (str): Search query
            
        Returns:
            List[Note]: List of matching notes
        """
        if not query or not query.strip():
            return []
        
        query = query.lower().strip()
        matching_notes = []
        
        for note in self.get_all_notes():
            # Search in title and content
            if (query in note.title.lower() or 
                query in note.content.lower() or
                any(query in tag.lower() for tag in note.tags)):
                matching_notes.append(note)
        
        return matching_notes
    
    def get_notes_by_tag(self, tag: str) -> List[Note]:
        """
        Get all notes with a specific tag
        
        Args:
            tag (str): Tag to search for
            
        Returns:
            List[Note]: List of notes with the tag
        """
        if not tag or not tag.strip():
            return []
        
        tag = tag.lower().strip()
        matching_notes = []
        
        for note in self.get_all_notes():
            if any(tag == note_tag.lower() for note_tag in note.tags):
                matching_notes.append(note)
        
        return matching_notes
    
    def get_all_tags(self) -> List[str]:
        """
        Get all unique tags from all notes
        
        Returns:
            List[str]: Sorted list of unique tags
        """
        all_tags = set()
        for note in self.get_all_notes():
            all_tags.update(tag.lower() for tag in note.tags)
        
        return sorted(list(all_tags))
    
    def get_notes_count(self) -> int:
        """
        Get total number of notes
        
        Returns:
            int: Number of notes in storage
        """
        return len(self._load_notes())
    
    def clear_all_notes(self) -> bool:
        """
        Delete all notes (use with caution!)
        
        Returns:
            bool: True if successful
        """
        return self._save_notes([])
    
    def export_notes(self, export_file: str) -> bool:
        """
        Export all notes to a different JSON file
        
        Args:
            export_file (str): Path to export file
            
        Returns:
            bool: True if successful
        """
        try:
            notes_data = self._load_notes()
            with open(export_file, 'w') as f:
                json.dump(notes_data, f, indent=2, ensure_ascii=False)
            return True
        except Exception as e:
            print(f"Error exporting notes: {e}")
            return False
    
    def import_notes(self, import_file: str, merge: bool = True) -> bool:
        """
        Import notes from a JSON file
        
        Args:
            import_file (str): Path to import file
            merge (bool): If True, merge with existing notes. If False, replace all.
            
        Returns:
            bool: True if successful
        """
        try:
            with open(import_file, 'r') as f:
                import_data = json.load(f)
            
            if not isinstance(import_data, list):
                return False
            
            if merge:
                existing_notes = self._load_notes()
                # Combine and remove duplicates by ID
                all_notes_dict = {note['id']: note for note in existing_notes}
                for note in import_data:
                    if 'id' in note:
                        all_notes_dict[note['id']] = note
                combined_notes = list(all_notes_dict.values())
            else:
                combined_notes = import_data
            
            return self._save_notes(combined_notes)
        except Exception as e:
            print(f"Error importing notes: {e}")
            return False
# END GENAI@CLINE
