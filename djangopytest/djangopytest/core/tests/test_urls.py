from django.urls import reverse, resolve 
#have one assert per function
class TestUrls:
    
    def test_detail_url(self):
        path = reverse('detail', kwargs={"pk":1})
        assert resolve(path).view_name == 'detail'
        