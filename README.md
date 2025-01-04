# TaskMaster CLI

A powerful and flexible command-line task manager written in Python.

## 🌟 Features

- ✅ Complete task management (create, modify, delete)
- 📋 Subtasks with progress tracking
- 🏷️ Tags with automatic suggestion
- 📊 Customizable categories with color coding
- 📝 Task-attached notes system
- 📅 Due dates and priorities
- 📈 Detailed statistics
- 📜 Complete modification history
- 🔍 Advanced search and filtering
- 📤 Data import/export

## 🚀 Installation

```bash
# Clone the repository
git clone https://github.com/your-username/taskmaster-cli.git
cd taskmaster-cli

# Create a virtual environment (recommended)
python -m venv venv
source venv/bin/activate  # Linux/Mac
# or
venv\Scripts\activate  # Windows

# Install dependencies
pip install -r requirements.txt
```

## 💻 Usage

To launch the application:

```bash
python main.py
```

### Main Menu

1. Add task
2. Show all tasks
3. Mark task as complete
4. Delete task
5. Add subtask
6. Search tasks
7. Filter tasks
8. Export tasks
9. Import tasks
10. Show overdue tasks
11. Statistics
12. Sort tasks
13. Mark subtask as complete
14. View task history
15. Manage categories
16. Manage notes
17. Quit

## 📁 Project Structure

```
taskmaster-cli/
├── data/                 # Data storage
├── todo_app/            
│   ├── core/            # Models and business logic
│   │   └── auto_tagging/# Automatic tagging system
│   ├── managers/        # Operation managers
│   ├── storage/         # Storage management
│   └── ui/              # User interface
└── main.py              # Entry point
```

## 🎯 Detailed Features

### Automatic Tagging System

The system analyzes task titles and descriptions to automatically suggest relevant tags based on predefined keywords.

### Categories

- Create categories with color codes
- Hierarchical organization (categories and subcategories)
- Filter and sort by category

### Notes

- Add detailed notes to tasks
- Modification history
- Quick view in task list

### Statistics

- Completion rate
- Priority distribution
- Most used tags
- Overdue task analysis

## 📊 Data Storage

Data is stored in JSON files in the `data/` folder:

- `tasks.json`: Tasks and subtasks
- `categories.json`: Categories
- `notes.json`: Notes
- `history.json`: Modification history

## 🤝 Contributing

Contributions are welcome! Feel free to:

1. Fork the project
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License. See the `LICENSE` file for details.

## 🙏 Acknowledgments

- Inspired by task management best practices
- Uses SOLID principles and MVC design pattern
- Colorful interface using ANSI colors
