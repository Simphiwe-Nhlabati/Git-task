from django.test import TestCase
from .models import Notes
# Create your tests here.


class TestNotes(TestCase):
  
    """
    Create title and 
    body test 
    """
        
    def setUp(self):
        Notes.objects.create(title='hello lil bro howzit',
                             body='This is my lil bro so bright')
        
    def test_title(self):
        note = Notes.objects.get(id=1)
        self.assertEqual(note.title, 'hello lil bro howzit')
        
    def test_body(self):
        note = Notes.objects.get(id=1)
        self.assertEqual(note.body, 'This is my lil bro so bright')
        
        
        