from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI()

# Veri modeli tanımlama
class Reservation(BaseModel):
    reservation_id: int
    customer_id: str
    hotel_name: str
    check_in_date: str
    check_out_date: str
    total_price: int

# Örnek rezervasyon verisi
reservations = [
    Reservation(reservation_id=10001, customer_id="C001", hotel_name="Hilton Istanbul", check_in_date="2025-02-01", check_out_date="2025-02-05", total_price=12000),
    Reservation(reservation_id=10002, customer_id="C002", hotel_name="Radisson Blu", check_in_date="2025-02-03", check_out_date="2025-02-07", total_price=9500),
    Reservation(reservation_id=10003, customer_id="C003", hotel_name="Swissotel", check_in_date="2025-02-05", check_out_date="2025-02-10", total_price=18000)
]

@app.get("/reservations", response_model=List[Reservation])
def get_reservations():
    return reservations

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
