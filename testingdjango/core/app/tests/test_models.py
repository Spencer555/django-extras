from django.test import TestCase
from app.models import Book 


class TestModels(TestCase):

    def setUp(self):
        self.book1 = Book.objects.create(
            title="Book 1",
            cost = 222,
            price = 333
        )

    #testing for a model property
    def test_book_slug_is_assigned_on_creation(self):
        self.assertEquals(self.book1.slug, "book-1")


    def test_profit_margin(self):
        profit = self.book1.price - self.book1.cost
        self.assertEquals(profit, 111)

    def test_loss(self):
            loss = self.book1.cost - self.book1.price 
        
            self.assertEquals(loss, -111)



