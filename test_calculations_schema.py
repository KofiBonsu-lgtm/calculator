from app.schemas.calculations import CalculationCreate
from app.models.calculations import CalculationType
import pytest

def test_divide_validator_rejects_zero():
    with pytest.raises(ValueError):
        CalculationCreate(a=1.0, b=0.0, type=CalculationType.divide)

def test_good_create():
    obj = CalculationCreate(a=3.0, b=2.0, type=CalculationType.multiply)
    assert obj.a == 3.0
