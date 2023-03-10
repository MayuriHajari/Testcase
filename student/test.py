import json
import re
from rest_framework.test import APIClient
from django.test import TestCase,Client
from django.urls import reverse
from django.core.exceptions import ValidationError
from student.models.student_model import Student 
from django.test import TestCase, Client
from django.core.validators import validate_email

class Get_Url_test(TestCase):

    def test_valid_student_request(self):
        reponse=self.client.get('/student/')
        self.assertEqual(reponse.status_code,200)

    def test_invalid_get_request(self):
        response = self.client.get('/student/15')
        self.assertEqual(response.status_code, 404)   

class PostRequestTestCase(TestCase):
    def setUp(self):
        self.valid_payload = {'student_name': 'John Dew','mail_id':'Abc@gmail.com'}
        self.url = ('/student/')
       
    
    def test_valid_post_request(self):
        response = self.client.post(self.url, data=json.dumps(self.valid_payload), content_type='application/json')
       
        self.assertEqual(response.status_code, 200)
        
   
        
class StudentModelTestCase(TestCase):
    
    def test_valid_mail_id(self):
        self.valid_mail_id = Student.objects.create(student_name='John Doe',mail_id='john@example.com')
        match = re.match("^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$", self.valid_mail_id.mail_id)
        if match == None:
                self.fail(f"{self.valid_mail_id.mail_id} is not a valid email id")
        else:
            self.assertEqual(1,1)

        

    def test_valid_email_ids(self):
       
        self.valid_student = {'student_name': 'XYZ', 'mail_id': ['Johne@abc.com','xy@zbc.com']}
        self.url = ('/student/')
       
        for email in self.valid_student["mail_id"]:
            try:
                validate_email(email)
            except ValidationError:
                self.fail(f"{email} is not a valid email")
                
        response = self.client.post(self.url, data=json.dumps(self.valid_student), content_type='application/json')       
        self.assertEqual(response.status_code, 200)
       
    
class StudentTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.student1 = Student.objects.create(
            id='0ee814e2-5a93-43f8-965d-31b2a87a1d69', student_name='Akshay',mail_id='akshay@gmail.com')
        

    def test_get_all_students(self):
        # get API response
        response = self.client.get('/student/')
        self.assertEqual(response.status_code,200)
        #print(response.json())
        self.assertEqual(response.json(), [
            {'id':'0ee814e2-5a93-43f8-965d-31b2a87a1d69', 'student_name':'Akshay','mail_id':'akshay@gmail.com'}
           
        ])
        