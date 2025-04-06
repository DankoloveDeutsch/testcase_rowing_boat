import pytest
from testcase_rowing_boat.models.section import Section
from testcase_rowing_boat.models.passenger import Passenger

class TestSection:
    def test_section_initialization(self):
        """Тест создания секции."""
        section = Section()
        assert section.capacity == 1
        assert len(section.passengers) == 0
    
    def test_add_passenger(self):
        """Тест добавления пассажира в секцию."""
        section = Section()
        passenger = Passenger(70.0)
        assert section.add_passenger(passenger)
        assert len(section.passengers) == 1
    
    def test_add_passenger_over_capacity(self):
        """Тест добавления пассажира сверх вместимости."""
        section = Section(capacity=1)
        passenger1 = Passenger(70.0)
        passenger2 = Passenger(80.0)
        assert section.add_passenger(passenger1)
        assert not section.add_passenger(passenger2)
        assert len(section.passengers) == 1
    
    def test_remove_passenger(self):
        """Тест удаления пассажира из секции."""
        section = Section()
        passenger = Passenger(70.0)
        section.add_passenger(passenger)
        removed_passenger = section.remove_passenger(passenger.id)
        assert removed_passenger is passenger
        assert len(section.passengers) == 0
    
    def test_get_weight(self):
        """Тест расчета общего веса пассажиров в секции."""
        section = Section(capacity=2)
        passenger1 = Passenger(70.0)
        passenger2 = Passenger(80.0)
        section.add_passenger(passenger1)
        section.add_passenger(passenger2)
        assert section.get_weight() == 150.0
