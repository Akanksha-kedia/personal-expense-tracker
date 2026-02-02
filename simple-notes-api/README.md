# 📝 Simple Notes Manager API

A beginner-friendly **Notes Management System** built with Python that demonstrates **REST API principles** and **clean architecture**. Perfect for learning Python, understanding API design, and extending with web frameworks like Flask or FastAPI.

## 🎯 Project Overview

This project is designed to be:
- ✅ **Easy to understand** - Clean, well-documented code
- ✅ **Beginner-friendly** - Uses only Python standard library
- ✅ **Extensible** - Ready for Flask/FastAPI integration  
- ✅ **Interview-ready** - Demonstrates key programming concepts
- ✅ **Open-source ready** - Professional structure and documentation

## 🚀 Quick Start

### Run the CLI Application
```bash
cd simple-notes-api
python3 cli.py
```

### Basic Usage
```bash
> create                    # Create a new note
> list                      # List all notes  
> search python             # Search for notes containing "python"
> stats                     # Show statistics
> help                      # Show all commands
> quit                      # Exit
```

## 📁 Project Structure

```
simple-notes-api/
├── models.py           # Data models (Note class, validation)
├── storage.py          # Storage layer (JSON file persistence)  
├── service.py          # Business logic (Service layer)
├── cli.py              # Command-line interface
├── requirements.txt    # Dependencies (optional packages)
├── README.md          # This documentation
├── web_flask.py       # Flask web API (extension)
├── web_fastapi.py     # FastAPI web API (extension)
└── notes.json         # Data storage file (auto-generated)
```

## 🏗️ Architecture Explained

### Clean Architecture Pattern
This project follows **clean architecture principles**:

```
┌─────────────────┐
│   CLI / Web     │  ← Interface Layer (cli.py, web_*.py)
├─────────────────┤
│   Service       │  ← Business Logic (service.py)
├─────────────────┤
│   Storage       │  ← Data Access (storage.py)  
├─────────────────┤
│   Models        │  ← Domain Models (models.py)
└─────────────────┘
```

### Layer Responsibilities

#### 🎯 **Models Layer** (`models.py`)
- **Purpose**: Define data structures and validation rules
- **Key Classes**: `Note`, validation functions
- **Why it's important**: Ensures data integrity and provides a clear contract

```python
class Note:
    def __init__(self, title: str, content: str, tags: list = None):
        # Data validation and initialization
        # Automatic ID generation and timestamps
```

#### 💾 **Storage Layer** (`storage.py`)  
- **Purpose**: Handle data persistence (currently JSON files)
- **Key Classes**: `NotesStorage`
- **Why it's important**: Separates data access from business logic
- **Easy to extend**: Could swap JSON for SQLite, PostgreSQL, etc.

```python
class NotesStorage:
    def create_note(self, note: Note) -> bool:
    def get_note_by_id(self, note_id: str) -> Optional[Note]:
    def update_note(self, note_id: str, updates: dict) -> bool:
    def delete_note(self, note_id: str) -> bool:
```

#### 🧠 **Service Layer** (`service.py`)
- **Purpose**: Contains business logic and orchestrates operations
- **Key Classes**: `NotesService` 
- **Why it's important**: Clean API for different interfaces (CLI, web)
- **Returns**: Structured responses with success/error information

```python
class NotesService:
    def create_note(self, title, content, tags) -> Tuple[bool, str, Optional[str]]:
        # Returns: (success, message, note_id)
```

#### 🖥️ **Interface Layer** (`cli.py`, web extensions)
- **Purpose**: Handle user interaction and input/output
- **Key Classes**: `NotesCliApp`
- **Why it's important**: Separates user interface from business logic

## 🔧 Core Features

### ✅ CRUD Operations
- **Create**: Add new notes with title, content, and tags
- **Read**: View individual notes or list all notes
- **Update**: Modify existing notes (title, content, tags)
- **Delete**: Remove notes with confirmation

### 🔍 Search & Filter
- **Full-text search**: Search in titles and content
- **Tag filtering**: Find notes by specific tags
- **Tag management**: List all unique tags

### 📊 Data Management  
- **Statistics**: Note count, tag statistics, averages
- **Export/Import**: Backup and restore notes as JSON
- **Data validation**: Ensure data integrity

### 🛡️ Error Handling
- Input validation with detailed error messages
- Graceful error handling at all layers
- Data backup before critical operations

## 💻 Detailed Usage Examples

### Creating Your First Note
```bash
> create
Title: My Learning Notes
Content: Today I learned about Python APIs and clean architecture
Tags (comma-separated, optional): python, learning, api
✅ Note 'My Learning Notes' created successfully
Note ID: 123e4567-e89b-12d3-a456-426614174000
```

### Viewing and Managing Notes
```bash
> list
Found 1 note(s):

1. 📄 My Learning Notes
   ID: 123e4567-e89b-12d3-a456-426614174000
   Tags: python, learning, api
   Created: 2026-01-31T21:43:00.123456

> show 123e4567-e89b-12d3-a456-426614174000
📄 NOTE DETAILS
------------------------------
📄 My Learning Notes
   ID: 123e4567-e89b-12d3-a456-426614174000
   Content: Today I learned about Python APIs and clean architecture
   Tags: python, learning, api
   Created: 2026-01-31T21:43:00.123456

Full Content:
Today I learned about Python APIs and clean architecture
```

### Searching and Filtering
```bash
> search python
🔍 SEARCH RESULTS for 'python'
----------------------------------------
Found 1 note matching 'python'

1. 📄 My Learning Notes
   ID: 123e4567-e89b-12d3-a456-426614174000
   Tags: python, learning, api
   Created: 2026-01-31T21:43:00.123456

> tag learning
🏷️ NOTES WITH TAG 'learning'
----------------------------------------
Found 1 note with tag 'learning'

> tags  
🏷️ ALL TAGS
--------------------
Found 3 unique tags

  • api
  • learning  
  • python
```

## 🌐 Web Framework Extensions

### Flask Web API (`web_flask.py`)
Extend the project with a REST API using Flask:

```python
from flask import Flask, request, jsonify
from service import NotesService

app = Flask(__name__)
notes_service = NotesService()

@app.route('/api/notes', methods=['POST'])
def create_note():
    # Implementation
    
@app.route('/api/notes', methods=['GET']) 
def get_notes():
    # Implementation
```

### FastAPI Web API (`web_fastapi.py`)
Modern async API with automatic documentation:

```python
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from service import NotesService

app = FastAPI(title="Simple Notes API")
notes_service = NotesService()

class NoteCreate(BaseModel):
    title: str
    content: str  
    tags: List[str] = []

@app.post("/api/notes")
async def create_note(note: NoteCreate):
    # Implementation
```

## 🧪 Testing Examples

### Manual Testing with CLI
```bash
# Test CRUD operations
> create
> list  
> update [note-id]
> delete [note-id]

# Test search functionality  
> search "important"
> tag "work"

# Test data management
> stats
> export backup.json
> import backup.json
```

### Unit Testing Structure (Future Enhancement)
```python
# test_notes.py
import unittest
from models import Note
from service import NotesService

class TestNotesService(unittest.TestCase):
    def setUp(self):
        self.service = NotesService("test_notes.json")
    
    def test_create_note(self):
        success, message, note_id = self.service.create_note(
            "Test Note", "Test Content", ["test"]
        )
        self.assertTrue(success)
        self.assertIsNotNone(note_id)
```

## 🎓 Learning Outcomes

By studying and extending this project, you'll learn:

### Python Concepts
- ✅ **Object-Oriented Programming**: Classes, inheritance, encapsulation
- ✅ **Type Hints**: Modern Python typing for better code clarity
- ✅ **Error Handling**: Try/catch, custom exceptions, graceful failures
- ✅ **File I/O**: Reading/writing JSON, file management
- ✅ **Data Structures**: Lists, dictionaries, sets for data manipulation

### Software Architecture
- ✅ **Clean Architecture**: Separation of concerns, dependency injection
- ✅ **Repository Pattern**: Data access abstraction
- ✅ **Service Pattern**: Business logic organization
- ✅ **MVC Pattern**: Model-View-Controller concepts

### API Design
- ✅ **REST Principles**: Resource-based URLs, HTTP methods
- ✅ **Data Validation**: Input sanitization and validation
- ✅ **Error Responses**: Consistent error handling and messaging
- ✅ **Documentation**: API documentation and examples

### Development Practices
- ✅ **Code Organization**: Modular design, clear file structure
- ✅ **Documentation**: Comprehensive README, code comments
- ✅ **Version Control**: Git-ready project structure
- ✅ **Testing**: Unit testing principles and structure

## 🚀 Extension Ideas

### Beginner Extensions
1. **Add note categories** (personal, work, ideas)
2. **Implement note priority levels** (high, medium, low)  
3. **Add creation/modification date filtering**
4. **Implement note archiving functionality**

### Intermediate Extensions
1. **Add user authentication and multiple user support**
2. **Implement note sharing between users**
3. **Add file attachments to notes**
4. **Create a web interface with HTML/CSS/JavaScript**

### Advanced Extensions  
1. **Add full-text search with ranking**
2. **Implement real-time collaboration**
3. **Add REST API with OpenAPI documentation**
4. **Deploy with Docker and cloud services**

## 🤝 Contributing

This project welcomes contributions! Areas where help is needed:

### For Beginners
- 📝 Improve documentation and examples
- 🐛 Report bugs and usability issues
- 💡 Suggest new features and improvements
- 🧪 Add test cases and examples

### For Experienced Developers  
- 🌐 Create web framework integrations
- 🔧 Performance optimizations
- 🛡️ Security enhancements
- 📊 Advanced features (search, analytics)

## 📚 Further Reading

### Python Resources
- [Python Official Documentation](https://docs.python.org/3/)
- [Clean Architecture in Python](https://realpython.com/python-application-layouts/)
- [Type Hints Documentation](https://docs.python.org/3/library/typing.html)

### API Design
- [REST API Best Practices](https://restfulapi.net/)
- [Flask Documentation](https://flask.palletsprojects.com/)
- [FastAPI Documentation](https://fastapi.tiangolo.com/)

### Software Architecture
- [Clean Architecture by Robert C. Martin](https://blog.cleancoder.com/uncle-bob/2012/08/13/the-clean-architecture.html)
- [Repository Pattern](https://martinfowler.com/eaaCatalog/repository.html)

## 📄 License

This project is open source and available under the MIT License.

## 🙏 Acknowledgments

Built as a learning project to demonstrate:
- Clean Python code organization
- REST API design principles  
- Beginner-friendly architecture
- Professional development practices

---

**Happy coding! 🐍** Start with the CLI, understand the architecture, then extend it to match your learning goals.
