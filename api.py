from flask import Flask, jsonify

app = Flask(__name__)

# Örnek otel rezervasyon verisi
reservations = [
    {"reservation_id": 10001, "customer_id": "C001", "hotel_name": "Hilton Istanbul", "check_in_date": "2025-02-01", "check_out_date": "2025-02-05", "total_price": 12000},
    {"reservation_id": 10002, "customer_id": "C002", "hotel_name": "Radisson Blu", "check_in_date": "2025-02-03", "check_out_date": "2025-02-07", "total_price": 9500},
    {"reservation_id": 10003, "customer_id": "C003", "hotel_name": "Swissotel", "check_in_date": "2025-02-05", "check_out_date": "2025-02-10", "total_price": 18000}
]

@app.route("/reservations", methods=["GET"])
def get_reservations():
    return jsonify(reservations)

if __name__ == "__main__":
    app.run(debug=True)
