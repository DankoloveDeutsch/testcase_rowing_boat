class Oar:
    def __init__(self, side: str):
        """Инициализация весла."""
        self.side = side
        self.is_in_water = False
        self.is_attached = False

    def attach(self) -> bool:
        """Устанавливает весло в уключину."""
        if not self.is_attached:
            self.is_attached = True
            return True
        return False

    def detach(self) -> bool:
        """Извлекает весло из уключины."""
        if self.is_attached:
            self.is_attached = False
            self.take_out_of_water()
            return True
        return False
    def row(self, strength: float = 1.0) -> bool:
        """Гребет веслом."""
        if not self.is_attached:
            return False
            
        if not self.is_in_water:
            self.put_in_water()
        
        return True
    def put_in_water(self) -> bool:
        """Опускает весло в воду."""
        if not self.is_in_water:
            self.is_in_water = True
            return True
        return False
    
    def take_out_of_water(self) -> bool:
        """Поднимает весло из воды."""
        if self.is_in_water:
            self.is_in_water = False
            return True
        return False
