# START GENAI@CLINE
"""
Simple Notes Manager API - Flask Web Extension
REST API using Flask web framework
"""

from flask import Flask, request, jsonify
from flask_cors import CORS
from typing import Dict, Any
import sys
import os

# Add current directory to path to import our modules
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from service import NotesService
from models import validate_note_data


def create_app(storage_file: str = "notes_web.json") -> Flask:
    """
    Create and configure Flask application
    
    Args:
        storage_file (str): Storage file for web API
        
    Returns:
        Flask: Configured Flask application
    """
    app = Flask(__name__)
    app.config['JSON_SORT_KEYS'] = False
    
    # Enable CORS for frontend integration
    CORS(app)
    
    # Initialize service
    notes_service = NotesService(storage_file)
    
    def format_response(success: bool, message: str, data: Any = None) -> Dict[str, Any]:
        """Format consistent API response"""
        response = {
            "success": success,
            "message": message
        }
        if data is not None:
            response["data"] = data
        return response
    
    def format_note(note) -> Dict[str, Any]:
        """Format note for API response"""
        return {
            "id": note.id,
            "title": note.title,
            "content": note.content,
            "tags": note.tags,
            "created_at": note.created_at,
            "updated_at": note.updated_at
        }
    
    # Error handlers
    @app.errorhandler(400)
    def bad_request(error):
        return jsonify(format_response(False, "Bad request")), 400
    
    @app.errorhandler(404)
    def not_found(error):
        return jsonify(format_response(False, "Resource not found")), 404
    
    @app.errorhandler(500)
    def internal_error(error):
        return jsonify(format_response(False, "Internal server error")), 500
    
    # API Routes
    
    @app.route('/', methods=['GET'])
    def home():
        """API documentation endpoint"""
        return jsonify({
            "name": "Simple Notes Manager API",
            "version": "1.0.0",
            "description": "REST API for managing notes",
            "endpoints": {
                "GET /": "API documentation",
                "GET /api/notes": "List all notes",
                "POST /api/notes": "Create a new note",
                "GET /api/notes/<id>": "Get specific note",
                "PUT /api/notes/<id>": "Update note",
                "DELETE /api/notes/<id>": "Delete note",
                "GET /api/notes/search?q=<query>": "Search notes",
                "GET /api/notes/tags/<tag>": "Get notes by tag",
                "GET /api/tags": "List all tags",
                "GET /api/stats": "Get statistics"
            }
        })
    
    @app.route('/api/notes', methods=['GET'])
    def get_notes():
        """Get all notes"""
        try:
            success, message, notes = notes_service.get_all_notes()
            
            if success:
                notes_data = [format_note(note) for note in notes]
                return jsonify(format_response(True, message, notes_data))
            else:
                return jsonify(format_response(False, message)), 400
                
        except Exception as e:
            return jsonify(format_response(False, f"Server error: {str(e)}")), 500
    
    @app.route('/api/notes', methods=['POST'])
    def create_note():
        """Create a new note"""
        try:
            data = request.get_json()
            
            if not data:
                return jsonify(format_response(False, "No data provided")), 400
            
            title = data.get('title', '').strip()
            content = data.get('content', '').strip()
            tags = data.get('tags', [])
            
            # Validate input
            validation_errors = validate_note_data({
                'title': title,
                'content': content,
                'tags': tags
            })
            
            if validation_errors:
                error_msg = '; '.join([f"{field}: {error}" for field, error in validation_errors.items()])
                return jsonify(format_response(False, f"Validation errors: {error_msg}")), 400
            
            success, message, note_id = notes_service.create_note(title, content, tags)
            
            if success:
                # Return the created note
                _, _, note = notes_service.get_note(note_id)
                return jsonify(format_response(True, message, format_note(note))), 201
            else:
                return jsonify(format_response(False, message)), 400
                
        except Exception as e:
            return jsonify(format_response(False, f"Server error: {str(e)}")), 500
    
    @app.route('/api/notes/<note_id>', methods=['GET'])
    def get_note(note_id):
        """Get specific note by ID"""
        try:
            success, message, note = notes_service.get_note(note_id)
            
            if success and note:
                return jsonify(format_response(True, message, format_note(note)))
            else:
                return jsonify(format_response(False, message)), 404
                
        except Exception as e:
            return jsonify(format_response(False, f"Server error: {str(e)}")), 500
    
    @app.route('/api/notes/<note_id>', methods=['PUT'])
    def update_note(note_id):
        """Update existing note"""
        try:
            data = request.get_json()
            
            if not data:
                return jsonify(format_response(False, "No data provided")), 400
            
            title = data.get('title')
            content = data.get('content')
            tags = data.get('tags')
            
            # Only validate fields that are being updated
            update_data = {}
            if title is not None:
                update_data['title'] = title.strip() if isinstance(title, str) else title
            if content is not None:
                update_data['content'] = content.strip() if isinstance(content, str) else content
            if tags is not None:
                update_data['tags'] = tags
            
            if update_data:
                validation_errors = validate_note_data(update_data)
                if validation_errors:
                    error_msg = '; '.join([f"{field}: {error}" for field, error in validation_errors.items()])
                    return jsonify(format_response(False, f"Validation errors: {error_msg}")), 400
            
            success, message = notes_service.update_note(note_id, title, content, tags)
            
            if success:
                # Return updated note
                _, _, note = notes_service.get_note(note_id)
                return jsonify(format_response(True, message, format_note(note)))
            else:
                return jsonify(format_response(False, message)), 404
                
        except Exception as e:
            return jsonify(format_response(False, f"Server error: {str(e)}")), 500
    
    @app.route('/api/notes/<note_id>', methods=['DELETE'])
    def delete_note(note_id):
        """Delete note by ID"""
        try:
            success, message = notes_service.delete_note(note_id)
            
            if success:
                return jsonify(format_response(True, message))
            else:
                return jsonify(format_response(False, message)), 404
                
        except Exception as e:
            return jsonify(format_response(False, f"Server error: {str(e)}")), 500
    
    @app.route('/api/notes/search', methods=['GET'])
    def search_notes():
        """Search notes by query parameter"""
        try:
            query = request.args.get('q', '').strip()
            
            if not query:
                return jsonify(format_response(False, "Search query parameter 'q' is required")), 400
            
            success, message, notes = notes_service.search_notes(query)
            
            if success:
                notes_data = [format_note(note) for note in notes]
                return jsonify(format_response(True, message, notes_data))
            else:
                return jsonify(format_response(False, message)), 400
                
        except Exception as e:
            return jsonify(format_response(False, f"Server error: {str(e)}")), 500
    
    @app.route('/api/notes/tags/<tag>', methods=['GET'])
    def get_notes_by_tag(tag):
        """Get notes by tag"""
        try:
            success, message, notes = notes_service.get_notes_by_tag(tag)
            
            if success:
                notes_data = [format_note(note) for note in notes]
                return jsonify(format_response(True, message, notes_data))
            else:
                return jsonify(format_response(False, message)), 400
                
        except Exception as e:
            return jsonify(format_response(False, f"Server error: {str(e)}")), 500
    
    @app.route('/api/tags', methods=['GET'])
    def get_tags():
        """Get all unique tags"""
        try:
            success, message, tags = notes_service.get_all_tags()
            
            if success:
                return jsonify(format_response(True, message, tags))
            else:
                return jsonify(format_response(False, message)), 400
                
        except Exception as e:
            return jsonify(format_response(False, f"Server error: {str(e)}")), 500
    
    @app.route('/api/stats', methods=['GET'])
    def get_stats():
        """Get notes statistics"""
        try:
            success, message, stats = notes_service.get_statistics()
            
            if success:
                return jsonify(format_response(True, message, stats))
            else:
                return jsonify(format_response(False, message)), 400
                
        except Exception as e:
            return jsonify(format_response(False, f"Server error: {str(e)}")), 500
    
    return app


def main():
    """Main entry point for Flask application"""
    import argparse
    
    parser = argparse.ArgumentParser(description='Simple Notes Manager - Flask Web API')
    parser.add_argument('--port', type=int, default=5000, help='Port to run the server on')
    parser.add_argument('--host', default='127.0.0.1', help='Host to bind the server to')
    parser.add_argument('--storage', default='notes_web.json', help='Storage file path')
    parser.add_argument('--debug', action='store_true', help='Run in debug mode')
    
    args = parser.parse_args()
    
    print("=" * 60)
    print("🌐 SIMPLE NOTES MANAGER - FLASK WEB API")
    print("=" * 60)
    print(f"Storage file: {args.storage}")
    print(f"Server: http://{args.host}:{args.port}")
    print(f"API Documentation: http://{args.host}:{args.port}/")
    print("=" * 60)
    
    app = create_app(args.storage)
    
    try:
        app.run(
            host=args.host,
            port=args.port,
            debug=args.debug
        )
    except KeyboardInterrupt:
        print("\n👋 Server stopped!")


if __name__ == "__main__":
    main()
# END GENAI@CLINE
