from django.test import SimpleTestCase
from django.urls import reverse, resolve
from app.views import book_list, book_detail, BookCreateView
#simple test case used when u dont need to interact with dbase

#class name functions etc should start with test

class TestUrls(SimpleTestCase):
    
    def test_list_url_resolves(self):
        url = reverse('book_list')
        self.assertEquals(resolve(url).func, book_list)

    #testing class based views
    def test_create_resolves(self):
        url = reverse('book_create')
        self.assertEquals(resolve(url).func.view_class, BookCreateView)


    def test_detail_url_resolves(self):
        # url = reverse('book_detail', args=[1]) for ids
        #for slugs
        url = reverse('book_detail', args=['some-slug'])
        self.assertEquals(resolve(url).func, book_detail)