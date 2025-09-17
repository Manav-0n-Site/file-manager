import os
import shutil
from pathlib import Path

class FileOrganizer:
    def __init__(self, source_directory):
        self.source_dir = Path(source_directory)
        self.file_types = {
            'Documents': ['.pdf', '.doc', '.docx', '.txt', '.rtf', '.odt', '.xls', '.xlsx', '.ppt', '.pptx'],
            'Images': ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff', '.svg', '.webp'],
            'Audio': ['.mp3', '.wav', '.aac', '.flac', '.ogg', '.m4a'],
            'Video': ['.mp4', '.avi', '.mov', '.wmv', '.flv', '.mkv', '.webm'],
            'Archives': ['.zip', '.rar', '.7z', '.tar', '.gz'],
            'Code': ['.py', '.js', '.html', '.css', '.java', '.cpp', '.c', '.php', '.rb'],
            'Executables': ['.exe', '.msi', '.dmg', '.app', '.deb', '.rpm']
        }
    
    def create_folders(self):
        """Create category folders if they don't exist"""
        for category in self.file_types.keys():
            folder_path = self.source_dir / category
            folder_path.mkdir(exist_ok=True)
    
    def get_file_category(self, file_extension):
        """Determine which category a file belongs to based on its extension"""
        for category, extensions in self.file_types.items():
            if file_extension.lower() in extensions:
                return category
        return 'Other'
    
    def organize_files(self):
        """Organize files into their respective category folders"""
        if not self.source_dir.exists():
            print(f"Error: Directory '{self.source_dir}' does not exist!")
            return
        
        print(f"Organizing files in: {self.source_dir}")
        self.create_folders()
        
        moved_files = 0
        skipped_files = 0
        
        for item in self.source_dir.iterdir():
            if item.is_file():
                file_extension = item.suffix
                category = self.get_file_category(file_extension)
                
                # Create destination path
                destination_folder = self.source_dir / category
                destination_path = destination_folder / item.name
                
                try:
                    # Check if file already exists in destination
                    if destination_path.exists():
                        # Add counter to filename to avoid overwriting
                        counter = 1
                        while destination_path.exists():
                            new_name = f"{item.stem}_{counter}{item.suffix}"
                            destination_path = destination_folder / new_name
                            counter += 1
                    
                    shutil.move(str(item), str(destination_path))
                    print(f"Moved: {item.name} → {category}/")
                    moved_files += 1
                    
                except Exception as e:
                    print(f"Error moving {item.name}: {e}")
                    skipped_files += 1
        
        print(f"\nOrganization complete!")
        print(f"Files moved: {moved_files}")
        print(f"Files skipped: {skipped_files}")

def main():
    # Get the directory to organize (current directory by default)
    directory = input("Enter the directory path to organize (press Enter for current directory): ").strip()
    
    if not directory:
        directory = os.getcwd()
    
    # Create organizer instance and organize files
    organizer = FileOrganizer(directory)
    organizer.organize_files()

if __name__ == "__main__":
    main()