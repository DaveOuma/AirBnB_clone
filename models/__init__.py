#!/usr/bin/python3
"""
Initialization module for the models directory.

This module initializes the FileStorage instance and reloads data from the storage.

"""

from models.engine.file_storage import FileStorage

# Create a FileStorage instance
storage = FileStorage()

# Reload data from storage
storage.reload()

