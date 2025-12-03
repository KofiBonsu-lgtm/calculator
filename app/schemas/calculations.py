from pydantic import BaseModel, Field, field_validator, model_validator, validator
from typing import Optional
from app.models.calculations import CalculationType

class CalculationCreate(BaseModel):
    a: float
    b: float
    type: CalculationType

    @model_validator(mode="after")
    def check_division(self):
        if self.type == CalculationType.divide and self.b == 0:
            raise ValueError("Cannot divide by zero")
        return self
    
class CalculationRead(BaseModel):
    id: int
    a: float
    b: float
    type: CalculationType
    result: Optional[float] = None
    created_at: Optional[str]

    class Config:
        orm_mode = True