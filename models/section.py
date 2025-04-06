from typing import List, Optional
from .passenger import Passenger

class Section:
    def __init__(self, capacity: int = 1):
        """Инициализация секции лодки."""
        self.capacity = capacity
        self.passengers: List[Passenger] = []
    
    def add_passenger(self, passenger: Passenger) -> bool:
        """Добавляет пассажира в секцию."""
        if len(self.passengers) < self.capacity:
            self.passengers.append(passenger)
            return True
        return False
    
    def remove_passenger(self, passenger_id: int) -> Optional[Passenger]:
        """Удаляет пассажира из секции по ID."""
        for i, passenger in enumerate(self.passengers):
            if passenger.id == passenger_id:
                return self.passengers.pop(i)
        return None
    
    def is_full(self) -> bool:
        """Проверяет, заполнена ли секция."""
        return len(self.passengers) >= self.capacity
    
    def get_weight(self) -> float:
        """Возвращает общий вес пассажиров в секции."""
        return sum(passenger.weight for passenger in self.passengers)
