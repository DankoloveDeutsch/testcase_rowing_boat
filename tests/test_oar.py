import pytest
from testcase_rowing_boat.models.oar import Oar
from testcase_rowing_boat.models.boat import Boat

class TestOar:
    def test_oar_initialization(self):
        """Тест создания весла."""
        oar = Oar("left")
        assert oar.side == "left"
        assert not oar.is_in_water
    
    def test_put_in_water(self):
        """Тест опускания весла в воду."""
        oar = Oar("right")
        assert oar.put_in_water()
        assert oar.is_in_water
    
    def test_take_out_of_water(self):
        """Тест поднятия весла из воды."""
        oar = Oar("left")
        oar.put_in_water()
        assert oar.take_out_of_water()
        assert not oar.is_in_water
    def test_oar_attachment(self):
        """Тест работы с веслами."""
        boat = Boat(max_weight=225)
        
        for oar in boat.oars:
            assert not oar.is_attached

        assert boat.attach_oar("left")
        assert boat.attach_oar("right")
        
        for oar in boat.oars:
            assert oar.is_attached

        initial_position = boat.position
        boat.row("left")
        assert boat.position != initial_position

        assert boat.detach_oar("right")
        assert not next(o for o in boat.oars if o.side == "right").is_attached

        with pytest.raises(Exception, match="Весло не установлено"):
            boat.row("right")