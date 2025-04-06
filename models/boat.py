from typing import List, Tuple, Optional
from .section import Section
from .oar import Oar
from .anchor import Anchor
from .passenger import Passenger
import math

class Boat:
    def __init__(self, max_weight: float):
        """Инициализация вёсельной лодки с тремя секциями."""
        self.max_weight = max_weight
        self.current_weight = 0.0
        self.sections = [Section() for _ in range(3)]  # носовая, средняя, задняя
        self.oars = [Oar("left"), Oar("right")]
        self.anchor = Anchor()
        self.position = (0.0, 0.0)  # координаты (x, y)
        self.direction = 0.0  # градусы, 0 - север
        self.speed = 0.0
    
    def move(self) -> Tuple[float, float]:
        """Двигает лодку в текущем направлении."""
        if self.anchor.is_lowered:
            return self.position
        
        dx = self.speed * math.sin(math.radians(self.direction))
        dy = self.speed * math.cos(math.radians(self.direction))
        
        self.position = (self.position[0] + dx, self.position[1] + dy)
        return self.position
    
    def turn(self, angle: float) -> float:
        """Поворачивает лодку на указанный угол."""
        self.direction = (self.direction + angle) % 360
        return self.direction
    
    def get_max_capacity(self) -> int:
        """Возвращает максимальную вместимость лодки."""
        return sum(section.capacity for section in self.sections)
    
    def add_passenger(self, passenger: Passenger, section_index: int) -> bool:
        """Добавляет пассажира в указанную секцию."""
        if self.current_weight + passenger.weight > self.max_weight:
            return False
        if 0 <= section_index < len(self.sections):
            return self.sections[section_index].add_passenger(passenger)
        return False
    
    def remove_passenger(self, passenger_id: int) -> Optional[Passenger]:
        """Удаляет пассажира по ID."""
        for section in self.sections:
            passenger = section.remove_passenger(passenger_id)
            if passenger:
                return passenger
        return None
    
    def tilt_angle(self) -> float:
        """Расчет наклона лодки по разнице в весе в носовой и кормовой секциях""" 
        front_weight = self.sections[0].get_weight()
        rear_weight = self.sections[2].get_weight()
        return (front_weight - rear_weight) * 0.5

    def lower_anchor(self) -> bool:
        """Опускает якорь."""
        return self.anchor.lower()
    
    def raise_anchor(self) -> bool:
        """Поднимает якорь."""
        return self.anchor.raise_anchor()

    def attach_oar(self, side: str) -> bool:
        """Устанавливает весло в уключину."""
        oar = next((o for o in self.oars if o.side == side), None)
        if oar and not oar.is_attached:
            oar.attach()
            return True
        return False

    def detach_oar(self, side: str) -> bool:
        """Извлекает весло из уключины."""
        oar = next((o for o in self.oars if o.side == side), None)
        if oar and oar.is_attached:
            oar.detach()
            return True
        return False

    def row(self, oar_side: str, strength: float = 1.0) -> Tuple[float, float]:
        """Гребет указанным веслом."""
        if self.anchor.is_lowered:
            return self.position
        
        oar = next((o for o in self.oars if o.side == oar_side), None)

        if not oar or not oar.is_attached:
            raise Exception("Весло не установлено в уключину")
        
        if oar.row(strength):
            # Поворот лодки зависит от того, каким веслом гребем
            if oar.side == "left":
                self.turn(-5 * strength)
            else:
                self.turn(5 * strength)
            
            self.speed = min(self.speed + 0.5 * strength, 5.0)
            return self.move()
        
        return self.position
    
    def row_both(self, strength: float = 1.0) -> Tuple[float, float]:
        """Гребет обоими веслами одновременно."""
        if self.anchor.is_lowered:
            return self.position
        
        left_success = next((o for o in self.oars if o.side == "left"), None).row(strength)
        right_success = next((o for o in self.oars if o.side == "right"), None).row(strength)
        
        if left_success and right_success:
            self.speed = min(self.speed + 1.0 * strength, 10.0)
            return self.move()
        
        return self.position
