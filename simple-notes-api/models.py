# START GENAI@CLINE
"""
Simple Notes Manager API - Data Models
Contains the Note class and validation logic
"""

import json
import uuid
from datetime import datetime
from typing import Optional, Dict, Any


class Note:
    """
    Note model representing a single note with CRUD operations
    
    A Note has:
    - id: unique identifier
    - title: note title (required)
    - content: note content (required) 
    - tags: list of tags for categorization
    - created_at: timestamp when note was created
    - updated_at: timestamp when note was last modified
    """
    
    def __init__(self, title: str, content: str, tags: Optional[list] = None):
        """
        Initialize a new Note
        
        Args:
            title (str): Title of the note (required)
            content (str): Content/body of the note (required)
            tags (list, optional): List of tags. Defaults to empty list.
        """
        # Validation
        if not title or not isinstance(title, str):
            raise ValueError("Title is required and must be a non-empty string")
        
        if not content or not isinstance(content, str):
            raise ValueError("Content is required and must be a non-empty string")
        
        if tags is not None and not isinstance(tags, list):
            raise ValueError("Tags must be a list")
        
        # Initialize properties
        self.id = str(uuid.uuid4())  # Generate unique ID
        self.title = title.strip()
        self.content = content.strip()
        self.tags = tags or []
        self.created_at = datetime.now().isoformat()
        self.updated_at = self.created_at
    
    def update(self, title: Optional[str] = None, content: Optional[str] = None, 
               tags: Optional[list] = None) -> None:
        """
        Update note fields
        
        Args:
            title (str, optional): New title
            content (str, optional): New content
            tags (list, optional): New tags
        """
        if title is not None:
            if not isinstance(title, str) or not title.strip():
                raise ValueError("Title must be a non-empty string")
            self.title = title.strip()
        
        if content is not None:
            if not isinstance(content, str) or not content.strip():
                raise ValueError("Content must be a non-empty string")
            self.content = content.strip()
        
        if tags is not None:
            if not isinstance(tags, list):
                raise ValueError("Tags must be a list")
            self.tags = tags
        
        self.updated_at = datetime.now().isoformat()
    
    def to_dict(self) -> Dict[str, Any]:
        """
        Convert note to dictionary for JSON serialization
        
        Returns:
            Dict: Note data as dictionary
        """
        return {
            'id': self.id,
            'title': self.title,
            'content': self.content,
            'tags': self.tags,
            'created_at': self.created_at,
            'updated_at': self.updated_at
        }
    
    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'Note':
        """
        Create Note instance from dictionary
        
        Args:
            data (Dict): Note data as dictionary
            
        Returns:
            Note: Note instance
        """
        # Create note without triggering __init__ validation
        note = cls.__new__(cls)
        note.id = data['id']
        note.title = data['title']
        note.content = data['content']
        note.tags = data.get('tags', [])
        note.created_at = data['created_at']
        note.updated_at = data['updated_at']
        return note
    
    def __str__(self) -> str:
        """String representation of the note"""
        tags_str = f" [Tags: {', '.join(self.tags)}]" if self.tags else ""
        return f"Note: {self.title}{tags_str}"
    
    def __repr__(self) -> str:
        """Developer representation of the note"""
        return f"Note(id='{self.id}', title='{self.title}', tags={self.tags})"


def validate_note_data(data: Dict[str, Any]) -> Dict[str, str]:
    """
    Validate note data and return validation errors
    
    Args:
        data (Dict): Note data to validate
        
    Returns:
        Dict: Dictionary of field errors (empty if valid)
    """
    errors = {}
    
    # Validate title
    title = data.get('title')
    if not title:
        errors['title'] = 'Title is required'
    elif not isinstance(title, str):
        errors['title'] = 'Title must be a string'
    elif not title.strip():
        errors['title'] = 'Title cannot be empty or whitespace only'
    elif len(title.strip()) > 200:
        errors['title'] = 'Title cannot exceed 200 characters'
    
    # Validate content
    content = data.get('content')
    if not content:
        errors['content'] = 'Content is required'
    elif not isinstance(content, str):
        errors['content'] = 'Content must be a string'
    elif not content.strip():
        errors['content'] = 'Content cannot be empty or whitespace only'
    elif len(content) > 10000:
        errors['content'] = 'Content cannot exceed 10,000 characters'
    
    # Validate tags
    tags = data.get('tags')
    if tags is not None:
        if not isinstance(tags, list):
            errors['tags'] = 'Tags must be a list'
        else:
            for i, tag in enumerate(tags):
                if not isinstance(tag, str):
                    errors['tags'] = f'Tag at index {i} must be a string'
                    break
                elif not tag.strip():
                    errors['tags'] = f'Tag at index {i} cannot be empty'
                    break
            
            # Check for duplicates
            if len(tags) != len(set(tag.strip().lower() for tag in tags)):
                errors['tags'] = 'Tags cannot contain duplicates'
            
            if len(tags) > 20:
                errors['tags'] = 'Cannot have more than 20 tags'
    
    return errors
# END GENAI@CLINE
