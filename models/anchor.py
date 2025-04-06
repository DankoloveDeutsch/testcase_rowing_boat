class Anchor:
    def __init__(self):
        """Инициализация якоря."""
        self.is_lowered = False
    
    def lower(self) -> bool:
        """Опускает якорь."""
        if not self.is_lowered:
            self.is_lowered = True
            return True
        return False
    
    def raise_anchor(self) -> bool:
        """Поднимает якорь."""
        if self.is_lowered:
            self.is_lowered = False
            return True
        return False
