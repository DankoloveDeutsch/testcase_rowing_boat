import pytest
from testcase_rowing_boat.models.boat import Boat
from testcase_rowing_boat.models.passenger import Passenger

class TestBoat:
    def test_boat_initialization(self):
        """Тест создания лодки."""
        boat = Boat(max_weight=225)
        assert len(boat.sections) == 3
        assert len(boat.oars) == 2
        assert boat.position == (0.0, 0.0)
        assert boat.direction == 0.0
        assert boat.speed == 0.0
        assert not boat.anchor.is_lowered
    
    def test_boat_movement(self):
        """Тест движения лодки."""
        boat = Boat(max_weight=225)
        boat.speed = 1.0
        initial_position = boat.position
        boat.move()
        assert boat.position != initial_position
    
    def test_boat_turn(self):
        """Тест поворота лодки."""
        boat = Boat(max_weight=225)
        initial_direction = boat.direction
        boat.turn(90)
        assert boat.direction == (initial_direction + 90) % 360
    
    def test_add_passenger(self):
        """Тест добавления пассажира."""
        boat = Boat(max_weight=225)
        passenger = Passenger(70.0)
        assert boat.add_passenger(passenger, 0)
        assert len(boat.sections[0].passengers) == 1
    
    def test_anchor_operations(self):
        """Тест операций с якорем."""
        boat = Boat(max_weight=225)
        assert boat.lower_anchor()
        assert boat.anchor.is_lowered
        
        # С опущенным якорем лодка не должна двигаться
        boat.speed = 1.0
        initial_position = boat.position
        boat.move()
        assert boat.position == initial_position
        
        assert boat.raise_anchor()
        assert not boat.anchor.is_lowered
        
        # После поднятия якоря лодка может двигаться
        boat.move()
        assert boat.position != initial_position
    
    def test_rowing(self):
        """Тест гребли."""
        boat = Boat(max_weight=225)

        initial_position = boat.position
        initial_direction = boat.direction
        
        boat.attach_oar("right")
        boat.row("right")
        assert boat.direction != initial_direction
        assert boat.position != initial_position
        
        # Сброс
        boat.position = (0.0, 0.0)
        boat.direction = 0.0
        boat.speed = 0.0
        
        initial_direction = boat.direction
        initial_position = boat.position
        boat.attach_oar("left")
        boat.row_both()
        assert boat.direction == initial_direction
        assert boat.position != initial_position
    def test_max_capacity(self):
        """Тест максимальной грузоподъемности"""
        boat = Boat(max_weight=225)
        p1 = Passenger(70)
        p2 = Passenger(90)
        p3 = Passenger(75)
        
        assert boat.add_passenger(p1, 0)
        assert boat.add_passenger(p2, 1)
        assert boat.add_passenger(p3, 2)
        assert not boat.add_passenger(Passenger(1), 0)
    def test_tilt_calculation(self):
        """Тест расчета угла наклона"""
        boat = Boat(max_weight=225)
        passenger = Passenger(90)
        boat.add_passenger(passenger, 0)
        assert boat.tilt_angle() > 0, "Нос должен быть опущен"

    def test_invalid_passenger(self):
        """Тест добавления пассажира с отрицательным весом"""
        with pytest.raises(ValueError):
            Passenger(-10)