from mixer.backend.django import mixer

import pytest 

@pytest.fixture
def product(request, db):
    return mixer.blend('core.Products', quantity=request.param)

@pytest.mark.parametrize('product', [1], indirect=True)
def test_product_is_in_stock(product):
    #mixer helps add fake data and to test so u only list the field u need
    assert product.is_in_stock == True 
@pytest.mark.parametrize('product', [0], indirect=True)    
def test_product_is_not_in_stock(product):
    #mixer helps add fake data and to test so u only list the field u need
    assert product.is_in_stock == False 
    
        
        
#without fixtures
# @pytest.mark.django_db #allows to access dbase
# class TestModels:
    
#     def test_product_is_in_stock(self):
#         #mixer helps add fake data and to test so u only list the field u need
#         product = mixer.blend('core.Products', quantity=1)
        
#         assert product.is_in_stock == True 
        
#     def test_product_is_not_in_stock(self):
#         #mixer helps add fake data and to test so u only list the field u need
#         product = mixer.blend('core.Products', quantity=0)
        
#         assert product.is_in_stock == False 
        