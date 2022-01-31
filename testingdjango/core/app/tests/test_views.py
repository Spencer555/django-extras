from django.test import TestCase, Client 
from django.urls import reverse 
from app.models import Book 
import json 



class TestViews(TestCase):
    
    #this runs b4 every test
    def setUp(self):
        self.client = Client()
        self.list_url = reverse('book_list')
        self.detail_url = reverse('book_detail', args=[1])

        #create a book for testing 
        self.book1 = Book.objects.create(title="mystorybook", cost= 90, price=100).save()
        self.book2 = Book.objects.create(title="book2", cost= 190, price=300).save()
    
    def test_project_list_GET(self):
        response = self.client.get(self.list_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'bookList.html')


    def test_project_detail_GET(self):
        response = self.client.get(self.detail_url)
        

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'bookDetail.html')

    def test_project_create_POST(self):
        url = reverse('book_create')
        response = self.client.post(url, self.book2)
     

        book2 = Book.objects.get(id=2)
        self.assertEquals(book2.title, "book2")

#  def test_project_detail_POST(self):

#      #does not exist but how u would handle if u had a subcategory in detatil view which create on post req

#        Category.objects.create(
#            project=self.project1,
#            name='development'
#        )
#         response = self.client.post(self.detail_url, {
#             'title':'red mouse',
#             'amount':1000,
#             'category':"development"
#         })
      

#         self.assertEquals(response.status_code, 302)
#         self.assertEquals(self.project1.expenses.first().title, 'expense1')
      

#also sub categ
    # def test_project_detail_DELETE(self):
        #  peform login
        # response = self.client.delete(self.detail_url, json.dumps({
        #     "id":1
        # }))
        # self.assertEquals(response.status_code, 204)
        # self.assertEquals(self.book.expenses.count(), 0)


           