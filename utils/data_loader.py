import yaml
from pathlib import Path
from typing import Dict, Any, List, Union


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
        """Load all YAML files from data directory."""
        project_root = Path(__file__).parent.parent
        data_dir = project_root / "data"
        
        # Загружаем все YAML файлы
        for yaml_file in data_dir.glob("*.yml"):
            file_data = self._load_yaml_file(yaml_file)
            # Сохраняем данные по имени файла (без расширения)
            self._data[yaml_file.stem] = file_data
    
    def _load_yaml_file(self, file_path: Path) -> Union[Dict, List]:
        """Load single YAML file."""
        with open(file_path, 'r', encoding='utf-8') as file:
            return yaml.safe_load(file)
    
    # ===== User methods =====
    def get_user(self, user_type: str) -> Dict[str, Any]:
        """
        Get user data by type.
        
        Args:
            user_type: Type of user ('existing_user', 'registration_user', 'wrong_credentials')
        
        Returns:
            Dictionary with user data (name, email, password)
        """
        user_data = self._data.get('user_data', {})
        # user_data.yml содержит словарь с ключом 'users'
        return user_data.get('users', {}).get(user_type, {})
    
    def get_user_field(self, user_type: str, field: str) -> str:
        """
        Get specific field from user data.
        
        Args:
            user_type: Type of user
            field: Field name ('name', 'email', 'password')
        
        Returns:
            Field value as string
        """
        return self.get_user(user_type).get(field, '')
    
    # ===== Product methods =====
    def get_products(self) -> List[Dict[str, Any]]:
        """
        Get all products.
        
        Returns:
            List of product dictionaries
        """
        return self._data.get('products', [])
    
    def get_product(self, product_id: int) -> Dict[str, Any]:
        """
        Get product by ID.
        
        Args:
            product_id: Product ID
        
        Returns:
            Dictionary with product data
        """
        products = self.get_products()
        for product in products:
            if product.get('id') == product_id:
                return product
        return {}
    
    def get_product_by_name(self, name: str) -> Dict[str, Any]:
        """
        Get product by name.
        
        Args:
            name: Product name
        
        Returns:
            Dictionary with product data
        """
        products = self.get_products()
        for product in products:
            if product.get('name') == name:
                return product
        return {}
    
    def get_product_field(self, product_id: int, field: str) -> Any:
        """
        Get specific field from product data.
        
        Args:
            product_id: Product ID
            field: Field name ('name', 'category', 'price', etc.)
        
        Returns:
            Field value
        """
        return self.get_product(product_id).get(field, '')


# Singleton instance for import
data_loader = DataLoader()