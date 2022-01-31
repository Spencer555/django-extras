from django.test import SimpleTestCase
from app.forms import BookForm

class TestForms(SimpleTestCase):

    def test_book_form_with_valid_data(self):
        form = BookForm(data={
            'title':'book 1',
            'cost':  22,
            'price': 100
        })

        self.assetTrue(form.is_valid())

    def test_book_form_with_no_valid_data(self):
        form = BookForm(data={})

        self.assetFalse(form.is_valid())
        #asserting the length of errors is 3 one for every single field
        self.assetEquals(len(form.errors),3)

