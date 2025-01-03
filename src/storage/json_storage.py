"""
JSON-based storage implementation
"""
from typing import List
from ..core.task import Task
from .serializers import task_to_dict, dict_to_task
from .file_handler import read_json_file, write_json_file
from .id_generator import adjust_imported_ids
from .validators import validate_task_data
from .exceptions import StorageError, ImportError

class JsonTaskStorage:
    def __init__(self, filename: str = "data/tasks.json"):
        self.filename = filename
        self.tasks: List[Task] = []
        self.load_tasks()

    def load_tasks(self) -> None:
        """Load tasks from the JSON file"""
        try:
            data = read_json_file(self.filename)
            for task_data in data:
                validate_task_data(task_data)
            self.tasks = [dict_to_task(task_data) for task_data in data]
        except FileNotFoundError:
            self.tasks = []
        except StorageError as e:
            self.tasks = []
            raise StorageError(f"Failed to load tasks: {e}")

    def save_tasks(self) -> None:
        """Save tasks to the JSON file"""
        try:
            data = [task_to_dict(task) for task in self.tasks]
            for task_data in data:
                validate_task_data(task_data)
            write_json_file(self.filename, data)
        except StorageError as e:
            raise StorageError(f"Failed to save tasks: {e}")

    def export_tasks(self, filename: str) -> None:
        """Export tasks to a specified file"""
        try:
            data = [task_to_dict(task) for task in self.tasks]
            write_json_file(filename, data)
        except StorageError as e:
            raise StorageError(f"Failed to export tasks: {e}")

    def import_tasks(self, filename: str) -> None:
        """Import tasks from a specified file"""
        try:
            data = read_json_file(filename)
            for task_data in data:
                validate_task_data(task_data)
            imported_tasks = [dict_to_task(task_data) for task_data in data]
            imported_tasks = adjust_imported_ids(self.tasks, imported_tasks)
            self.tasks.extend(imported_tasks)
            self.save_tasks()
        except StorageError as e:
            raise ImportError(f"Failed to import tasks: {e}")