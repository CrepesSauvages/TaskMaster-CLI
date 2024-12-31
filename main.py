"""
Main entry point for the Todo List application
"""
from src.ui.cli import TodoCLI

def main():
    app = TodoCLI()
    app.run()

if __name__ == "__main__":
    main()