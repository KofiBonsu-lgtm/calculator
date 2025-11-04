from Calculator.Addition import addition
from Calculator.Subtraction import subtraction
from Calculator.Division import division
from httpx import AsyncClient, ASGITransport
from main import app
import pytest

def test_add():
    assert addition(2, 3) == 5
def test_subtract():
    assert subtraction(3, 5) == 2
def test_divide():
    assert division(2, 6) == 3    

@pytest.mark.asyncio
async def test_add_endpoint():
 transport = ASGITransport(app=app)
 async with AsyncClient(transport=transport, base_url="http://test") as ac:
        response = await ac.get("/add?a=5&b=3")
 assert response.status_code == 200
 assert response.json() == {"result": 8}
