## 📜 License

This project is licensed under the [MIT License](LICENSE).



# 📂 Advanced File Organizer (GUI + CLI)

> **Made with ❤️ by Manav** – a 17-year-old passionate 12th-grade developer who loves solving everyday problems for developers.  
> This project helps you **organize messy folders automatically** into neat, categorized folders — saving time and effort.

---

## 🚀 Features

### 🖥️ **Advanced File Organizer (GUI)**
- ✅ **Beautiful GUI (Tkinter)** – User-friendly interface  
- ✅ **Automatic Folder Categorization** – Documents, Images, Videos, Audio, Code, etc.  
- ✅ **Real-Time Progress Bar** – Shows organization progress  
- ✅ **Live File Statistics** – Displays files by type and extension  
- ✅ **Collision Handling** – Adds timestamp if a file with the same name exists  
- ✅ **Custom Categories** – Easily extendable to support more file types  

---

### 💻 **Simple File Organizer (CLI)**
- ⚡ **Quick to Run:** Just open terminal and run  
- 📂 **Automatic Folder Creation:** No manual setup needed  
- 🔄 **Duplicate File Handling:** Renames duplicates automatically  
- 🖊️ **Terminal Logs:** Shows exactly which files were moved  
- 🔧 **Beginner-Friendly:** Perfect for those who want a lightweight solution  

---

## 🛠️ Tech Stack

- **Python 3.x**
- **Tkinter** – for GUI version
- **Shutil + Pathlib** – for file operations
- **Datetime** – for unique file renaming
- **OS module** – for directory management

---

## 📸 Preview

### GUI Version  
![GUI Preview](https://via.placeholder.com/900x500?text=GUI+File+Organizer+Preview)  

*(Replace with an actual screenshot of your GUI window)*  

---

## 📂 Project Structure

```bash
.
├── gui_file_organizer.py    # GUI version (Tkinter)
├── cli_file_organizer.py    # Command-line version
├── README.md                # Documentation
└── requirements.txt         # (Optional) Python dependencies
```

---

## ⚡ Installation & Usage

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/your-username/file-organizer.git
cd file-organizer
```

### 2️⃣ Run GUI Version
```bash
python gui_file_organizer.py
```
- Select the folder to organize  
- Click **Organize Files**  
- Watch as your files get sorted neatly!  

---

### 3️⃣ Run CLI Version
```bash
python cli_file_organizer.py
```
- Enter a directory path or press Enter for current folder  
- Files will be organized into category folders automatically  

---

## 📊 Example

Before:
```
Downloads/
├── notes.pdf
├── image1.png
├── music.mp3
├── code.py
└── movie.mp4
```

After:
```
Downloads/
├── Documents/
│   └── notes.pdf
├── Images/
│   └── image1.png
├── Audio/
│   └── music.mp3
├── Code/
│   └── code.py
└── Video/
    └── movie.mp4
```

---

## 💡 Future Improvements

- [ ] Dark Mode GUI  
- [ ] Option to undo file organization  
- [ ] Support for cloud storage (Google Drive / Dropbox)  
- [ ] Drag & drop folder selection  

---

## 🧑‍💻 About the Creator

Hi! I'm **Manav**, a **12th-grade student (17 y/o)** who loves developing projects that solve real-world problems.  
I made this project to help developers, students, and office users quickly declutter their folders and stay organized.  

---

## ⭐ Contribute

- Found a bug? Open an issue.  
- Want to add a feature? Feel free to fork and submit a PR.  

If you liked this project, don’t forget to **star ⭐ the repository**.  

---

**"Made with ❤️, Python, and a love for clean folders – by Manav."**

