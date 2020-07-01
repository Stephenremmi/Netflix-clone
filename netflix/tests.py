from django.test import TestCase
from .models import Director,Film,characters
import datetime as dt
# Create your tests here.
class DirectorTestClass(TestCase):

    # Set up method
    def setUp(self):
        self.tracy= Director(first_name = 'Tracy', last_name ='Wairimu', email ='tracy@citam.com')

        # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.tracy,Director))

         # Testing Save Method
    def test_save_method(self):
        self.tracy.save_director()
        editors = Director.objects.all()
        self.assertTrue(len(editors) > 0)

class FilmTestClass(TestCase):

    def setUp(self):
        # Creating a new director and saving it
        self.tracy= Director(first_name = 'Tracy', last_name ='Wairimu', email ='tracy@citam.com')
        self.tracy.save_direcor()

        # Creating a new character and saving it
        self.new_character = characters(name = 'testing')
        self.new_character.save()

        self.new_film= Film(title = 'Test Film',post = 'This is a random test Post',director = self.tracy)
        self.new_film.save()

        self.new_film.character.add(self.new_characters)
# Create your tests here.
    def tearDown(self):
        Director.objects.all().delete()
        Characters.objects.all().delete()
        Film.objects.all().delete()

