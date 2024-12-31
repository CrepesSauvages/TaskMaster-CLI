"""
Validation utilities for task data
"""
from typing import Dict, Any
from .exceptions import ValidationError

def validate_task_data(data: Dict[str, Any]) -> None:
    """Validate task dictionary data"""
    required_fields = ['id', 'title', 'description', 'created_at']
    
    for field in required_fields:
        if field not in data:
            raise ValidationError(f"Missing required field: {field}")
        
    if not isinstance(data['id'], int):
        raise ValidationError("Task ID must be an integer")
        
    if not isinstance(data['title'], str) or not data['title'].strip():
        raise ValidationError("Title must be a non-empty string")
        
    if not isinstance(data['description'], str):
        raise ValidationError("Description must be a string")