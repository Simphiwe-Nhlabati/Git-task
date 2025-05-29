from django.test import TestCase
from .models import Notes
from django.urls import reverse
# Create your tests here.


class TestModelNotes(TestCase):
  
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
        
        
class TestViewsNotes(TestCase):
    
    def setUp(self):
        Notes.objects.create(title='hello lil bro howzit',
                             body='This is my lil bro so bright')
        
    def test_read_sticky_notes(self):
        response = self.client.get(reverse('read_sticky_notes'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(self.note.title, 'hello lil bro howzit')
        self.assertEqual(self.note.body, 'This is my lil bro so bright')
        
    def test_create_sticky_notes(self):
        response = self.client.post(reverse('create_sticky_notes'), {
            'title': 'hello lil bro howzit',
            'body': 'This is my lil bro so bright.'
        })
        self.assertEqual(response.status_code, 302)
        self.assertTrue(Notes.objects.filter(title='hello lil bro howzit'))
        
    def test_update_sticky_notes(self):
        response = self.client.post(reverse('update_sticky_notes', args=[1]), {
            'title': 'Hello big bro howzit',
            'body': 'This is my big bro so shiny.'
        })
        self.assertEqual(response.status_code, 302)
        note = Notes.objects.get(id=1)
        self.assertEqual(note.title, 'Hello big bro howzit')
        self.assertEqual(note.body, 'This is my big bro so shiny')
        
    def test_delete_sticky_notes(self):
        response = self.client.post(reverse('delete_sticky_notes', args=[1]))
        self.assertEqual(response.status_code, 302)
        self.assertFalse(Notes.objects.filter(id=1))