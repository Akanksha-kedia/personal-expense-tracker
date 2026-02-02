# START GENAI@CLINE
"""
Simple Notes Manager API - Command Line Interface
Interactive CLI for testing and using the Notes API
"""

import sys
from typing import List
from service import NotesService
from models import Note


class NotesCliApp:
    """
    Command-line interface for the Simple Notes Manager API
    
    Provides an interactive menu system to:
    - Create, read, update, delete notes
    - Search notes and filter by tags
    - View statistics and manage data
    - Import/export functionality
    """
    
    def __init__(self, storage_file: str = "notes.json"):
        """
        Initialize CLI application
        
        Args:
            storage_file (str): Storage file path
        """
        self.service = NotesService(storage_file)
        self.storage_file = storage_file
    
    def display_header(self):
        """Display application header"""
        print("\n" + "=" * 60)
        print("📝 SIMPLE NOTES MANAGER API - COMMAND LINE INTERFACE")
        print("=" * 60)
        print(f"Storage file: {self.storage_file}")
        print("Type 'help' for available commands or 'quit' to exit")
        print("=" * 60)
    
    def display_menu(self):
        """Display main menu options"""
        print("\n📋 AVAILABLE COMMANDS:")
        print("=" * 40)
        
        # CRUD Operations
        print("\n🔧 CRUD OPERATIONS:")
        print("  create      - Create a new note")
        print("  list        - List all notes")
        print("  show <id>   - Show specific note by ID")
        print("  update <id> - Update an existing note")
        print("  delete <id> - Delete a note by ID")
        
        # Search and Filter
        print("\n🔍 SEARCH & FILTER:")
        print("  search <query>  - Search notes by content")
        print("  tag <tagname>   - Find notes by tag")
        print("  tags            - List all tags")
        
        # Data Management
        print("\n📊 DATA MANAGEMENT:")
        print("  stats     - Show statistics")
        print("  export    - Export notes to file")
        print("  import    - Import notes from file")
        print("  clear     - Delete all notes (use with caution!)")
        
        # System
        print("\n⚙️  SYSTEM:")
        print("  help      - Show this help message")
        print("  quit      - Exit the application")
        print()
    
    def format_note(self, note: Note, show_content: bool = True) -> str:
        """
        Format a note for display
        
        Args:
            note (Note): Note to format
            show_content (bool): Whether to show full content
            
        Returns:
            str: Formatted note string
        """
        lines = []
        lines.append(f"📄 {note.title}")
        lines.append(f"   ID: {note.id}")
        
        if show_content:
            # Truncate content if too long
            content = note.content
            if len(content) > 100:
                content = content[:100] + "..."
            lines.append(f"   Content: {content}")
        
        if note.tags:
            tags_str = ", ".join(note.tags)
            lines.append(f"   Tags: {tags_str}")
        
        lines.append(f"   Created: {note.created_at}")
        if note.updated_at != note.created_at:
            lines.append(f"   Updated: {note.updated_at}")
        
        return "\n".join(lines)
    
    def get_user_input(self, prompt: str, required: bool = True) -> str:
        """
        Get user input with validation
        
        Args:
            prompt (str): Input prompt
            required (bool): Whether input is required
            
        Returns:
            str: User input
        """
        while True:
            try:
                value = input(f"{prompt}: ").strip()
                if required and not value:
                    print("❌ This field is required. Please try again.")
                    continue
                return value
            except KeyboardInterrupt:
                print("\n\n👋 Goodbye!")
                sys.exit(0)
            except EOFError:
                print("\n\n👋 Goodbye!")
                sys.exit(0)
    
    def get_tags_input(self) -> List[str]:
        """Get tags input from user"""
        tags_input = input("Tags (comma-separated, optional): ").strip()
        if not tags_input:
            return []
        
        # Split by comma and clean up
        tags = [tag.strip() for tag in tags_input.split(",") if tag.strip()]
        return tags
    
    def confirm_action(self, message: str) -> bool:
        """Get confirmation for destructive actions"""
        while True:
            response = input(f"{message} (yes/no): ").lower().strip()
            if response in ['yes', 'y']:
                return True
            elif response in ['no', 'n']:
                return False
            else:
                print("Please enter 'yes' or 'no'")
    
    def cmd_create(self):
        """Create a new note"""
        print("\n📝 CREATE NEW NOTE")
        print("-" * 30)
        
        title = self.get_user_input("Title")
        content = self.get_user_input("Content")
        tags = self.get_tags_input()
        
        success, message, note_id = self.service.create_note(title, content, tags)
        
        if success:
            print(f"✅ {message}")
            print(f"Note ID: {note_id}")
        else:
            print(f"❌ {message}")
    
    def cmd_list(self):
        """List all notes"""
        print("\n📋 ALL NOTES")
        print("-" * 30)
        
        success, message, notes = self.service.get_all_notes()
        
        if not success:
            print(f"❌ {message}")
            return
        
        if not notes:
            print("📭 No notes found. Create your first note with 'create'!")
            return
        
        print(f"Found {len(notes)} note(s):\n")
        
        for i, note in enumerate(notes, 1):
            print(f"{i}. {self.format_note(note, show_content=False)}")
            print()
    
    def cmd_show(self, note_id: str = None):
        """Show a specific note"""
        if not note_id:
            note_id = self.get_user_input("Note ID")
        
        print(f"\n📄 NOTE DETAILS")
        print("-" * 30)
        
        success, message, note = self.service.get_note(note_id)
        
        if success and note:
            print(self.format_note(note, show_content=True))
            print(f"\nFull Content:\n{note.content}")
        else:
            print(f"❌ {message}")
    
    def cmd_update(self, note_id: str = None):
        """Update an existing note"""
        if not note_id:
            note_id = self.get_user_input("Note ID")
        
        # First, show current note
        success, message, note = self.service.get_note(note_id)
        if not success:
            print(f"❌ {message}")
            return
        
        print(f"\n✏️  UPDATE NOTE")
        print("-" * 30)
        print("Current note:")
        print(self.format_note(note))
        print("\nEnter new values (press Enter to keep current value):")
        
        # Get updates
        new_title = input(f"Title [{note.title}]: ").strip()
        new_content = input(f"Content [{note.content[:50]}...]: ").strip()
        
        print(f"Current tags: {', '.join(note.tags) if note.tags else 'None'}")
        tags_input = input("Tags (comma-separated): ").strip()
        
        # Prepare update data
        updates = {}
        if new_title:
            updates['title'] = new_title
        if new_content:
            updates['content'] = new_content
        if tags_input:
            updates['tags'] = [tag.strip() for tag in tags_input.split(",") if tag.strip()]
        
        if not updates:
            print("❌ No updates provided.")
            return
        
        # Perform update
        success, message = self.service.update_note(
            note_id,
            title=updates.get('title'),
            content=updates.get('content'),
            tags=updates.get('tags')
        )
        
        if success:
            print(f"✅ {message}")
        else:
            print(f"❌ {message}")
    
    def cmd_delete(self, note_id: str = None):
        """Delete a note"""
        if not note_id:
            note_id = self.get_user_input("Note ID")
        
        # Show note before deletion
        success, message, note = self.service.get_note(note_id)
        if not success:
            print(f"❌ {message}")
            return
        
        print(f"\n🗑️  DELETE NOTE")
        print("-" * 30)
        print("Note to delete:")
        print(self.format_note(note, show_content=False))
        
        if not self.confirm_action("Are you sure you want to delete this note?"):
            print("❌ Delete cancelled.")
            return
        
        success, message = self.service.delete_note(note_id)
        
        if success:
            print(f"✅ {message}")
        else:
            print(f"❌ {message}")
    
    def cmd_search(self, query: str = None):
        """Search notes"""
        if not query:
            query = self.get_user_input("Search query")
        
        print(f"\n🔍 SEARCH RESULTS for '{query}'")
        print("-" * 40)
        
        success, message, notes = self.service.search_notes(query)
        
        if not success:
            print(f"❌ {message}")
            return
        
        print(message)
        
        if notes:
            print()
            for i, note in enumerate(notes, 1):
                print(f"{i}. {self.format_note(note, show_content=False)}")
                print()
    
    def cmd_tag(self, tag: str = None):
        """Find notes by tag"""
        if not tag:
            tag = self.get_user_input("Tag name")
        
        print(f"\n🏷️  NOTES WITH TAG '{tag}'")
        print("-" * 40)
        
        success, message, notes = self.service.get_notes_by_tag(tag)
        
        if not success:
            print(f"❌ {message}")
            return
        
        print(message)
        
        if notes:
            print()
            for i, note in enumerate(notes, 1):
                print(f"{i}. {self.format_note(note, show_content=False)}")
                print()
    
    def cmd_tags(self):
        """List all tags"""
        print(f"\n🏷️  ALL TAGS")
        print("-" * 20)
        
        success, message, tags = self.service.get_all_tags()
        
        if not success:
            print(f"❌ {message}")
            return
        
        print(message)
        
        if tags:
            print()
            for tag in tags:
                print(f"  • {tag}")
        else:
            print("No tags found.")
    
    def cmd_stats(self):
        """Show statistics"""
        print(f"\n📊 NOTES STATISTICS")
        print("-" * 30)
        
        success, message, stats = self.service.get_statistics()
        
        if not success:
            print(f"❌ {message}")
            return
        
        print(f"Total notes: {stats['total_notes']}")
        print(f"Unique tags: {stats['total_unique_tags']}")
        print(f"Average tags per note: {stats['average_tags_per_note']}")
        
        if stats['all_tags']:
            print(f"\nAll tags: {', '.join(stats['all_tags'])}")
    
    def cmd_export(self):
        """Export notes"""
        filename = self.get_user_input("Export filename", required=True)
        if not filename.endswith('.json'):
            filename += '.json'
        
        success, message = self.service.export_notes(filename)
        
        if success:
            print(f"✅ {message}")
        else:
            print(f"❌ {message}")
    
    def cmd_import(self):
        """Import notes"""
        filename = self.get_user_input("Import filename", required=True)
        
        merge = self.confirm_action("Merge with existing notes? (no = replace all)")
        
        success, message = self.service.import_notes(filename, merge)
        
        if success:
            print(f"✅ {message}")
        else:
            print(f"❌ {message}")
    
    def cmd_clear(self):
        """Clear all notes"""
        print(f"\n⚠️  CLEAR ALL NOTES")
        print("-" * 30)
        
        success, message, stats = self.service.get_statistics()
        if success and stats['total_notes'] > 0:
            print(f"This will permanently delete {stats['total_notes']} notes!")
            
            if not self.confirm_action("Are you absolutely sure?"):
                print("❌ Clear operation cancelled.")
                return
        
        success, message = self.service.clear_all_notes()
        
        if success:
            print(f"✅ {message}")
        else:
            print(f"❌ {message}")
    
    def parse_command(self, command_line: str):
        """Parse and execute command"""
        parts = command_line.strip().split()
        if not parts:
            return
        
        cmd = parts[0].lower()
        args = parts[1:] if len(parts) > 1 else []
        
        # Command routing
        if cmd in ['help', 'h', '?']:
            self.display_menu()
        elif cmd in ['quit', 'exit', 'q']:
            print("👋 Goodbye!")
            sys.exit(0)
        elif cmd == 'create':
            self.cmd_create()
        elif cmd == 'list':
            self.cmd_list()
        elif cmd == 'show':
            note_id = args[0] if args else None
            self.cmd_show(note_id)
        elif cmd == 'update':
            note_id = args[0] if args else None
            self.cmd_update(note_id)
        elif cmd == 'delete':
            note_id = args[0] if args else None
            self.cmd_delete(note_id)
        elif cmd == 'search':
            query = ' '.join(args) if args else None
            self.cmd_search(query)
        elif cmd == 'tag':
            tag = args[0] if args else None
            self.cmd_tag(tag)
        elif cmd == 'tags':
            self.cmd_tags()
        elif cmd == 'stats':
            self.cmd_stats()
        elif cmd == 'export':
            self.cmd_export()
        elif cmd == 'import':
            self.cmd_import()
        elif cmd == 'clear':
            self.cmd_clear()
        else:
            print(f"❌ Unknown command: {cmd}")
            print("Type 'help' for available commands.")
    
    def run(self):
        """Main application loop"""
        self.display_header()
        
        # Show initial stats
        success, _, stats = self.service.get_statistics()
        if success:
            print(f"📊 Current stats: {stats['total_notes']} notes, {stats['total_unique_tags']} unique tags")
        
        self.display_menu()
        
        while True:
            try:
                command = input("\n> ").strip()
                if command:
                    self.parse_command(command)
            except KeyboardInterrupt:
                print("\n\n👋 Goodbye!")
                break
            except EOFError:
                print("\n\n👋 Goodbye!")
                break


def main():
    """Main entry point"""
    storage_file = "notes.json"
    
    # Handle command line argument for custom storage file
    if len(sys.argv) > 1:
        storage_file = sys.argv[1]
    
    app = NotesCliApp(storage_file)
    app.run()


if __name__ == "__main__":
    main()
# END GENAI@CLINE
