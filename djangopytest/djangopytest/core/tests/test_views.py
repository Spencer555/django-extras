from django.test import RequestFactory 
from django.urls import reverse
from django.contrib.auth.models import User, AnonymousUser
from core.views import product_detail
from mixer.backend.django import mixer 
import pytest
from django.test import TestCase

@pytest.fixture(scope="module")
#the scope makes it instantiate only once    
def factory():
    return RequestFactory()

@pytest.fixture
#if it would access dbase pass it db
def product(db):
    return mixer.blend('core.Products')

def test_product_detail_authenticated(factory, product):
    # def test_product_detail_authenticated(factory, Products, db): db is passed in produ so we dont need it here
    path = reverse('detail', kwargs={'pk': 1})
    request = factory.get(path)
    #creates a new user instance
    request.user = mixer.blend('user')
    
    response = product_detail(request, pk=1)
    
    assert response.status_code == 200
    
def test_product_detail_unauthenticated(factory, product):
        path = reverse('detail', kwargs={'pk': 1})
        request = factory.get(path)
        #creates a new user instance
        request.user = AnonymousUser()
        
        response = product_detail(request, pk=1)
        
        assert response.status_code == 302
        
            
            
            
            
            
#with setup class       
            
            
            
            
# @pytest.mark.django_db
# class TestViews(TestCase):
    
#     @classmethod
#     def setUpClass(cls):
#         #runs b4 everything else
#         super(TestViews, cls).setUpClass()
#         mixer.blend('core.Products')
#         cls.factory = RequestFactory()
#         cls.path = reverse('detail', kwargs={'pk': 1})
       
        
    
#     def test_product_detail_authenticated(self):
#         mixer.blend('core.Products')
#         request = self.factory.get(self.path)
#         #creates a new user instance
#         request.user = mixer.blend('user')
#         response = product_detail(request, pk=1)
        
#         assert response.status_code == 200
       
       
        
#     def test_product_detail_unauthenticated(self):
#             mixer.blend('core.Products')
#             request = self.factory.get(self.path)
#             #creates a new user instance
#             request.user = AnonymousUser()
            
#             response = product_detail(request, pk=1)
            
#             assert response.status_code == 302
            