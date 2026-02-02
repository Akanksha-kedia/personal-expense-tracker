# START GENAI@CLINE
"""
Simple Notes Manager API - Service Layer
Business logic and API operations
"""

from typing import List, Optional, Dict, Any, Tuple
from models import Note, validate_note_data
from storage import NotesStorage


class NotesService:
    """
    Service class that provides business logic for notes management
    
    This class implements the Service pattern, providing:
    - High-level API for notes operations
    - Input validation and error handling
    - Business logic and rules
    - Clean interface for CLI and web frameworks
    """
    
    def __init__(self, storage_file: str = "notes.json"):
        """
        Initialize the notes service
        
        Args:
            storage_file (str): Path to storage file
        """
        self.storage = NotesStorage(storage_file)
    
    def create_note(self, title: str, content: str, tags: Optional[List[str]] = None) -> Tuple[bool, str, Optional[str]]:
        """
        Create a new note with validation
        
        Args:
            title (str): Note title
            content (str): Note content
            tags (List[str], optional): List of tags
            
        Returns:
            Tuple[bool, str, Optional[str]]: (success, message, note_id)
        """
        try:
            # Validate input data
            note_data = {
                'title': title,
                'content': content,
                'tags': tags or []
            }
            
            validation_errors = validate_note_data(note_data)
            if validation_errors:
                error_messages = [f"{field}: {error}" for field, error in validation_errors.items()]
                return False, f"Validation errors: {'; '.join(error_messages)}", None
            
            # Create note
            note = Note(title, content, tags)
            
            # Save to storage
            if self.storage.create_note(note):
                return True, f"Note '{note.title}' created successfully", note.id
            else:
                return False, "Failed to save note to storage", None
                
        except ValueError as e:
            return False, f"Invalid input: {str(e)}", None
        except Exception as e:
            return False, f"Unexpected error: {str(e)}", None
    
    def get_note(self, note_id: str) -> Tuple[bool, str, Optional[Note]]:
        """
        Retrieve a note by ID
        
        Args:
            note_id (str): Note ID
            
        Returns:
            Tuple[bool, str, Optional[Note]]: (success, message, note)
        """
        try:
            if not note_id or not isinstance(note_id, str):
                return False, "Invalid note ID", None
            
            note = self.storage.get_note_by_id(note_id.strip())
            if note:
                return True, "Note retrieved successfully", note
            else:
                return False, f"Note with ID '{note_id}' not found", None
                
        except Exception as e:
            return False, f"Error retrieving note: {str(e)}", None
    
    def get_all_notes(self) -> Tuple[bool, str, List[Note]]:
        """
        Retrieve all notes
        
        Returns:
            Tuple[bool, str, List[Note]]: (success, message, notes_list)
        """
        try:
            notes = self.storage.get_all_notes()
            count = len(notes)
            
            if count == 0:
                return True, "No notes found", []
            else:
                message = f"Retrieved {count} note{'s' if count != 1 else ''}"
                return True, message, notes
                
        except Exception as e:
            return False, f"Error retrieving notes: {str(e)}", []
    
    def update_note(self, note_id: str, title: Optional[str] = None, 
                   content: Optional[str] = None, tags: Optional[List[str]] = None) -> Tuple[bool, str]:
        """
        Update an existing note
        
        Args:
            note_id (str): Note ID
            title (str, optional): New title
            content (str, optional): New content
            tags (List[str], optional): New tags
            
        Returns:
            Tuple[bool, str]: (success, message)
        """
        try:
            if not note_id or not isinstance(note_id, str):
                return False, "Invalid note ID"
            
            # Check if note exists
            existing_note = self.storage.get_note_by_id(note_id.strip())
            if not existing_note:
                return False, f"Note with ID '{note_id}' not found"
            
            # Prepare update data (only include fields that are being updated)
            update_data = {}
            if title is not None:
                update_data['title'] = title
            if content is not None:
                update_data['content'] = content
            if tags is not None:
                update_data['tags'] = tags
            
            if not update_data:
                return False, "No fields provided for update"
            
            # Validate update data
            validation_errors = validate_note_data(update_data)
            if validation_errors:
                error_messages = [f"{field}: {error}" for field, error in validation_errors.items()]
                return False, f"Validation errors: {'; '.join(error_messages)}"
            
            # Perform update
            if self.storage.update_note(note_id.strip(), update_data):
                return True, f"Note '{existing_note.title}' updated successfully"
            else:
                return False, "Failed to update note"
                
        except Exception as e:
            return False, f"Error updating note: {str(e)}"
    
    def delete_note(self, note_id: str) -> Tuple[bool, str]:
        """
        Delete a note by ID
        
        Args:
            note_id (str): Note ID
            
        Returns:
            Tuple[bool, str]: (success, message)
        """
        try:
            if not note_id or not isinstance(note_id, str):
                return False, "Invalid note ID"
            
            # Get note title for confirmation message
            existing_note = self.storage.get_note_by_id(note_id.strip())
            if not existing_note:
                return False, f"Note with ID '{note_id}' not found"
            
            # Delete note
            if self.storage.delete_note(note_id.strip()):
                return True, f"Note '{existing_note.title}' deleted successfully"
            else:
                return False, "Failed to delete note"
                
        except Exception as e:
            return False, f"Error deleting note: {str(e)}"
    
    def search_notes(self, query: str) -> Tuple[bool, str, List[Note]]:
        """
        Search notes by query
        
        Args:
            query (str): Search query
            
        Returns:
            Tuple[bool, str, List[Note]]: (success, message, matching_notes)
        """
        try:
            if not query or not isinstance(query, str):
                return False, "Invalid search query", []
            
            query = query.strip()
            if not query:
                return False, "Empty search query", []
            
            matching_notes = self.storage.search_notes(query)
            count = len(matching_notes)
            
            if count == 0:
                return True, f"No notes found matching '{query}'", []
            else:
                message = f"Found {count} note{'s' if count != 1 else ''} matching '{query}'"
                return True, message, matching_notes
                
        except Exception as e:
            return False, f"Error searching notes: {str(e)}", []
    
    def get_notes_by_tag(self, tag: str) -> Tuple[bool, str, List[Note]]:
        """
        Get notes by tag
        
        Args:
            tag (str): Tag to search for
            
        Returns:
            Tuple[bool, str, List[Note]]: (success, message, matching_notes)
        """
        try:
            if not tag or not isinstance(tag, str):
                return False, "Invalid tag", []
            
            tag = tag.strip()
            if not tag:
                return False, "Empty tag", []
            
            matching_notes = self.storage.get_notes_by_tag(tag)
            count = len(matching_notes)
            
            if count == 0:
                return True, f"No notes found with tag '{tag}'", []
            else:
                message = f"Found {count} note{'s' if count != 1 else ''} with tag '{tag}'"
                return True, message, matching_notes
                
        except Exception as e:
            return False, f"Error retrieving notes by tag: {str(e)}", []
    
    def get_all_tags(self) -> Tuple[bool, str, List[str]]:
        """
        Get all unique tags
        
        Returns:
            Tuple[bool, str, List[str]]: (success, message, tags_list)
        """
        try:
            tags = self.storage.get_all_tags()
            count = len(tags)
            
            if count == 0:
                return True, "No tags found", []
            else:
                message = f"Found {count} unique tag{'s' if count != 1 else ''}"
                return True, message, tags
                
        except Exception as e:
            return False, f"Error retrieving tags: {str(e)}", []
    
    def get_statistics(self) -> Tuple[bool, str, Dict[str, Any]]:
        """
        Get notes statistics
        
        Returns:
            Tuple[bool, str, Dict]: (success, message, stats)
        """
        try:
            notes_count = self.storage.get_notes_count()
            all_tags = self.storage.get_all_tags()
            tags_count = len(all_tags)
            
            # Calculate average tags per note
            if notes_count > 0:
                all_notes = self.storage.get_all_notes()
                total_tags = sum(len(note.tags) for note in all_notes)
                avg_tags_per_note = total_tags / notes_count
            else:
                avg_tags_per_note = 0
            
            stats = {
                'total_notes': notes_count,
                'total_unique_tags': tags_count,
                'average_tags_per_note': round(avg_tags_per_note, 2),
                'all_tags': all_tags
            }
            
            return True, "Statistics retrieved successfully", stats
            
        except Exception as e:
            return False, f"Error retrieving statistics: {str(e)}", {}
    
    def export_notes(self, export_file: str) -> Tuple[bool, str]:
        """
        Export all notes to file
        
        Args:
            export_file (str): Export file path
            
        Returns:
            Tuple[bool, str]: (success, message)
        """
        try:
            if not export_file or not isinstance(export_file, str):
                return False, "Invalid export file path"
            
            if self.storage.export_notes(export_file.strip()):
                notes_count = self.storage.get_notes_count()
                return True, f"Exported {notes_count} notes to '{export_file}'"
            else:
                return False, "Failed to export notes"
                
        except Exception as e:
            return False, f"Error exporting notes: {str(e)}"
    
    def import_notes(self, import_file: str, merge: bool = True) -> Tuple[bool, str]:
        """
        Import notes from file
        
        Args:
            import_file (str): Import file path
            merge (bool): Whether to merge with existing notes
            
        Returns:
            Tuple[bool, str]: (success, message)
        """
        try:
            if not import_file or not isinstance(import_file, str):
                return False, "Invalid import file path"
            
            original_count = self.storage.get_notes_count()
            
            if self.storage.import_notes(import_file.strip(), merge):
                new_count = self.storage.get_notes_count()
                
                if merge:
                    imported_count = new_count - original_count
                    message = f"Imported {imported_count} notes from '{import_file}' (merged with existing)"
                else:
                    message = f"Imported {new_count} notes from '{import_file}' (replaced all existing)"
                
                return True, message
            else:
                return False, "Failed to import notes"
                
        except Exception as e:
            return False, f"Error importing notes: {str(e)}"
    
    def clear_all_notes(self) -> Tuple[bool, str]:
        """
        Delete all notes (use with caution!)
        
        Returns:
            Tuple[bool, str]: (success, message)
        """
        try:
            notes_count = self.storage.get_notes_count()
            
            if notes_count == 0:
                return True, "No notes to delete"
            
            if self.storage.clear_all_notes():
                return True, f"Successfully deleted all {notes_count} notes"
            else:
                return False, "Failed to delete notes"
                
        except Exception as e:
            return False, f"Error clearing notes: {str(e)}"
# END GENAI@CLINE
