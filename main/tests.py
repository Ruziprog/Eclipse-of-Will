from django.test import TestCase
from .models import Character, Empire

class CharacterModelTest(TestCase):
    def setUp(self):
        Character.objects.create(
            name="Test Character",
            age=30,
            gender="Male",
            ability="Test Ability",
            description="Test Description",
            image_url="http://example.com/image.jpg",
            quote="Test Quote",
            weight=65,
            height=165,
            order=1
            )
        
    def test_character_creation(self):
        character = Character.objects.get(name="Test Character")
        self.assertEqual(character.age, 30)
        self.assertEqual(character.gender, "Male")
        self.assertEqual(character.ability, "Test Ability")
        self.assertEqual(character.description, "Test Description")
        self.assertEqual(character.image_url, "http://example.com/image.jpg")
        self.assertEqual(character.quote, "Test Quote")
        self.assertEqual(character.weight, 65)
        self.assertEqual(character.height, 165)
        self.assertEqual(character.order, 1)

    def test_character_str(self):
        character = Character.objects.get(name="Test Character")
        self.assertEqual(str(character), "Test Character")

    def test_character_image_url_can_be_blank(self):
        char = Character.objects.create(
            name="No image",
            age=24,
            gender="Female",
            ability="Test",
            description="Test",
            weight=56,
            height=178,
            order=2
        )
        self.assertIsNone(char.image_url)

class EmpireModelTest(TestCase):
    def setUp(self):
        Empire.objects.create(
            name="Test Empire",
            credo="Strength is Right",
            anthem="Test Anthem",
            description="Test Description",
            image_url="http://example.com/empire.jpg",
            order=2,
            ruler="Test Ruler",
            Heir="Test Heir"
        )

def test_empire_creation(self):
    empire = Empire.objects.get(name="Test Empire")
    self.assertEqual(empire.credo, "Strength is Right")
    self.assertEqual(str(empire), "Test Empire")
    self.assertEqual(empire.order, 1)