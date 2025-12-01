import yaml
from pathlib import Path
from typing import Dict, Any


class DataLoader:
    """Singleton class for loading test data from YAML files."""
    
    _instance = None
    _data: Dict[str, Any] = {}
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance
    
    def __init__(self):
        if not self._data:
            self._load_data()
    
    def _load_data(self) -> None:
        """Load YAML data once (singleton pattern)."""
        project_root = Path(__file__).parent.parent
        yaml_path = project_root / "data" / "user_data.yml"
        
        with open(yaml_path, 'r', encoding='utf-8') as file:
            self._data = yaml.safe_load(file)
    
    def get_user(self, user_type: str) -> Dict[str, Any]:
        """
        Get user data by type.
        
        Args:
            user_type: Type of user ('existing_user', 'registration_user', 'wrong_credentials')
        
        Returns:
            Dictionary with user data (name, email, password)
        """
        return self._data['users'].get(user_type, {})
    
    def get_user_field(self, user_type: str, field: str) -> str:
        """
        Get specific field from user data.
        
        Args:
            user_type: Type of user
            field: Field name ('name', 'email', 'password')
        
        Returns:
            Field value as string
        """
        return self._data['users'].get(user_type, {}).get(field, '')


# Singleton instance for import
data_loader = DataLoader()
