from models import Shipment
from datetime import datetime

class ShipmentTracker:
    def __init__(self):
        self.shipments = []

    def create_shipment(self, manufacturer, bikesetu_yard, franchisee_store, customer):
        shipment = Shipment(manufacturer, bikesetu_yard, franchisee_store, customer)
        self.shipments.append(shipment)
        return shipment

    def update_status(self, shipment, status, location):
        shipment.status = status
        shipment.tracking_history.append({
            'status': status,
            'location': location,
            'timestamp': datetime.now()
        })
        print(f"Shipment updated: {status} at {location}")

    def get_tracking_info(self, shipment):
        return shipment.tracking_history
