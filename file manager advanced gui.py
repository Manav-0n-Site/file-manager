import os
import shutil
import tkinter as tk
from tkinter import filedialog, messagebox, ttk
from pathlib import Path
from datetime import datetime

class AdvancedFileOrganizer:
    def __init__(self):
        self.file_types = {
            'Documents': ['.pdf', '.doc', '.docx', '.txt', '.rtf', '.odt', '.xls', '.xlsx', '.ppt', '.pptx'],
            'Images': ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff', '.svg', '.webp', '.ico'],
            'Audio': ['.mp3', '.wav', '.aac', '.flac', '.ogg', '.m4a', '.wma'],
            'Video': ['.mp4', '.avi', '.mov', '.wmv', '.flv', '.mkv', '.webm', '.mpeg'],
            'Archives': ['.zip', '.rar', '.7z', '.tar', '.gz', '.bz2'],
            'Code': ['.py', '.js', '.html', '.css', '.java', '.cpp', '.c', '.php', '.rb', '.json', '.xml'],
            'Executables': ['.exe', '.msi', '.dmg', '.app', '.deb', '.rpm', '.bat', '.sh'],
            'Design': ['.psd', '.ai', '.eps', '.sketch', '.fig'],
            'Database': ['.sql', '.db', '.sqlite', '.mdb']
        }
    
    def organize_directory(self, source_dir, progress_callback=None):
        """Organize files with progress callback for GUI"""
        source_path = Path(source_dir)
        if not source_path.exists():
            return False, "Directory does not exist!"
        
        # Create category folders
        for category in self.file_types.keys():
            folder_path = source_path / category
            folder_path.mkdir(exist_ok=True)
        
        # Get all files
        files = [f for f in source_path.iterdir() if f.is_file()]
        total_files = len(files)
        
        moved_files = 0
        errors = []
        
        for i, file_path in enumerate(files):
            if progress_callback:
                progress_callback(i, total_files, f"Processing {file_path.name}")
            
            file_extension = file_path.suffix.lower()
            category = self.get_file_category(file_extension)
            
            destination_folder = source_path / category
            destination_path = destination_folder / file_path.name
            
            try:
                if destination_path.exists():
                    # Create unique filename with timestamp
                    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
                    new_name = f"{file_path.stem}_{timestamp}{file_path.suffix}"
                    destination_path = destination_folder / new_name
                
                shutil.move(str(file_path), str(destination_path))
                moved_files += 1
                
            except Exception as e:
                errors.append(f"{file_path.name}: {str(e)}")
        
        return True, f"Moved {moved_files} files. Errors: {len(errors)}"
    
    def get_file_category(self, file_extension):
        """Get category for file extension"""
        for category, extensions in self.file_types.items():
            if file_extension in extensions:
                return category
        return 'Other'
    
    def add_custom_category(self, category_name, extensions):
        """Add custom file category"""
        self.file_types[category_name] = extensions
    
    def get_file_stats(self, directory):
        """Get statistics about files in directory"""
        path = Path(directory)
        stats = {'total': 0, 'by_category': {}, 'by_extension': {}}
        
        for file_path in path.iterdir():
            if file_path.is_file():
                stats['total'] += 1
                ext = file_path.suffix.lower()
                
                # Count by extension
                stats['by_extension'][ext] = stats['by_extension'].get(ext, 0) + 1
                
                # Count by category
                category = self.get_file_category(ext)
                stats['by_category'][category] = stats['by_category'].get(category, 0) + 1
        
        return stats

class FileOrganizerGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Advanced File Organizer")
        self.root.geometry("600x500")
        
        self.organizer = AdvancedFileOrganizer()
        self.setup_ui()
    
    def setup_ui(self):
        # Main frame
        main_frame = ttk.Frame(self.root, padding="20")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Directory selection
        ttk.Label(main_frame, text="Select Directory:").grid(row=0, column=0, sticky=tk.W, pady=5)
        
        self.dir_var = tk.StringVar()
        ttk.Entry(main_frame, textvariable=self.dir_var, width=50).grid(row=1, column=0, sticky=(tk.W, tk.E), pady=5)
        ttk.Button(main_frame, text="Browse", command=self.browse_directory).grid(row=1, column=1, padx=5)
        
        # Progress bar
        self.progress = ttk.Progressbar(main_frame, mode='determinate')
        self.progress.grid(row=2, column=0, columnspan=2, sticky=(tk.W, tk.E), pady=10)
        
        # Status label
        self.status_var = tk.StringVar(value="Ready")
        ttk.Label(main_frame, textvariable=self.status_var).grid(row=3, column=0, columnspan=2, pady=5)
        
        # Organize button
        ttk.Button(main_frame, text="Organize Files", command=self.organize_files).grid(row=4, column=0, columnspan=2, pady=10)
        
        # Stats text area
        ttk.Label(main_frame, text="File Statistics:").grid(row=5, column=0, sticky=tk.W, pady=5)
        
        self.stats_text = tk.Text(main_frame, height=15, width=70)
        self.stats_text.grid(row=6, column=0, columnspan=2, pady=5)
        
        # Configure grid weights
        main_frame.columnconfigure(0, weight=1)
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)
    
    def browse_directory(self):
        directory = filedialog.askdirectory()
        if directory:
            self.dir_var.set(directory)
            self.show_stats(directory)
    
    def show_stats(self, directory):
        try:
            stats = self.organizer.get_file_stats(directory)
            self.stats_text.delete(1.0, tk.END)
            
            self.stats_text.insert(tk.END, f"Total files: {stats['total']}\n\n")
            self.stats_text.insert(tk.END, "Files by category:\n")
            for category, count in stats['by_category'].items():
                self.stats_text.insert(tk.END, f"  {category}: {count}\n")
            
            self.stats_text.insert(tk.END, "\nFiles by extension:\n")
            for ext, count in stats['by_extension'].items():
                if ext:  # Skip empty extensions
                    self.stats_text.insert(tk.END, f"  {ext}: {count}\n")
                    
        except Exception as e:
            self.stats_text.delete(1.0, tk.END)
            self.stats_text.insert(tk.END, f"Error reading directory: {e}")
    
    def organize_files(self):
        directory = self.dir_var.get()
        if not directory:
            messagebox.showerror("Error", "Please select a directory first!")
            return
        
        def update_progress(current, total, message):
            self.progress['value'] = (current / total) * 100
            self.status_var.set(message)
            self.root.update_idletasks()
        
        try:
            success, message = self.organizer.organize_directory(directory, update_progress)
            if success:
                messagebox.showinfo("Success", message)
                self.show_stats(directory)
            else:
                messagebox.showerror("Error", message)
        
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")
        
        finally:
            self.progress['value'] = 0
            self.status_var.set("Ready")

if __name__ == "__main__":
    root = tk.Tk()
    app = FileOrganizerGUI(root)
    root.mainloop()