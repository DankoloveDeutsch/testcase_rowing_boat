import pytest
from testcase_rowing_boat.models.anchor import Anchor

class TestAnchor:
    def test_anchor_initialization(self):
        """Тест создания якоря."""
        anchor = Anchor()
        assert not anchor.is_lowered
    
    def test_lower_anchor(self):
        """Тест опускания якоря."""
        anchor = Anchor()
        assert anchor.lower()
        assert anchor.is_lowered
    
    def test_raise_anchor(self):
        """Тест поднятия якоря."""
        anchor = Anchor()
        anchor.lower()
        assert anchor.raise_anchor()
        assert not anchor.is_lowered