from selenium import webdriver
from app.models import Book 
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from django.urls import reverse
import time 


class TestProjectListPage(StaticLiveServerTestCase):


   #b4 every test func
    def setUp(self):
        self.browser = webdriver.Chrome()
    
    
    #after every test func
    def teadown(self):
        self.browser.close()


    def test_no_project_alerts_is_displayed(self):
        self.browser.get(self.live_server_url)
        time.sleep(20)
        
        # the user request the page for the first time 
        alert = self.browser.find_element_by_class_name('classname in ui')
        
        self.assertEquals(
            alert.find_element_by_tag_name('h3').text, 'Sorry you dont\'t have any projects, yet, '
        )
        
    def test_no_projects_alert_button_redirects_to_add_page(self):
        self.browser.get(self.live_server_url)
        
        #the user requests the page for the first time
        add_url = self.live_server_url #gets the main url
        self.browser.find_element_by_tag_name('a').click()
        self.assertEquals(
            self.browser.current_url,
        )
        
        
    def test_user_sees_project_list(self):
        book1 = Book.objects.get.create(
            title="book 1",
            cost = 33,
            price = 50
        )
        self.browser.get(self.live_server_url)
        
        #the user sees the proj on their screen
        self.assertEquals(
            self.browser.find_element_by_tag_name('h5').text,
            'project1'
        )

    
    def test_user_is_redirected_to_project_detail(self):
        book1 = Book.objects.get.create(
                    title="book 1",
                    cost = 33,
                    price = 50
                )
        self.browser.get(self.live_server_url)
        
        #the user sees the project when he clicks the visit and is being redirected to the detail page 
        detail_url = self.live_server_url + reverse('detail', args=[book1.id])
        self.browser.find_element_by_link_text('VISIT').click()
        self.assertEquals(
            self.browser.current_url,
            detail_url
        )