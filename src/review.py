from models import Review

class ReviewManager:
    def __init__(self):
        self.reviews = []

    def add_review(self, customer, rating, comment):
        review = Review(customer, rating, comment)
        self.reviews.append(review)
        print(f"Review added: {customer.name} rated {rating} stars")

    def get_reviews(self):
        return self.reviews
