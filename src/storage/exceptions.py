"""
Custom exceptions for storage operations
"""

class StorageError(Exception):
    """Base exception for storage operations"""
    pass

class FileAccessError(StorageError):
    """Raised when file operations fail"""
    pass

class ValidationError(StorageError):
    """Raised when data validation fails"""
    pass

class ImportError(StorageError):
    """Raised when task import fails"""
    pass