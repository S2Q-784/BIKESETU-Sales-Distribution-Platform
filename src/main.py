from models import Manufacturer, BikesetuYard, FranchiseeStore, Customer
from shipment import ShipmentTracker
from review import ReviewManager

def main():
    # Initialize actors
    manufacturer = Manufacturer("Bike Manufacturer Co.")
    yard = BikesetuYard("Bikesetu Yard A")
    store = FranchiseeStore("Store A")
    customer = Customer("John Doe", "123 Main St")

    # Initialize managers
    shipment_tracker = ShipmentTracker()
    review_manager = ReviewManager()

    # Create and track a shipment
    shipment = shipment_tracker.create_shipment(manufacturer, yard, store, customer)
    shipment_tracker.update_status(shipment, "Left Manufacturer", manufacturer.name)
    shipment_tracker.update_status(shipment, "Arrived at Yard", yard.location)
    shipment_tracker.update_status(shipment, "Left Yard", yard.location)
    shipment_tracker.update_status(shipment, "Arrived at Franchisee Store", store.location)
    shipment_tracker.update_status(shipment, "Delivered to Customer", customer.address)

    # Customer Review
    review_manager.add_review(customer, 5, "Bike delivered on time, great service!")

    # Display tracking info
    print("Tracking Information:")
    for event in shipment_tracker.get_tracking_info(shipment):
        print(event)

    # Display reviews
    print("Customer Reviews:")
    for review in review_manager.get_reviews():
        print(f"{review.customer.name}: {review.rating} stars - {review.comment}")

if __name__ == "__main__":
    main()
