from datetime import datetime

class Manufacturer:
    def __init__(self, name):
        self.name = name

class BikesetuYard:
    def __init__(self, location):
        self.location = location

class FranchiseeStore:
    def __init__(self, location):
        self.location = location

class Customer:
    def __init__(self, name, address):
        self.name = name
        self.address = address

class Shipment:
    def __init__(self, manufacturer, bikesetu_yard, franchisee_store, customer):
        self.manufacturer = manufacturer
        self.bikesetu_yard = bikesetu_yard
        self.franchisee_store = franchisee_store
        self.customer = customer
        self.status = "Pending"
        self.tracking_history = []

class Review:
    def __init__(self, customer, rating, comment):
        self.customer = customer
        self.rating = rating
        self.comment = comment
        self.date = datetime.now()
