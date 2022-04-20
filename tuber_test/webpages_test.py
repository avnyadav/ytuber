from django.test import TestCase
from webpages.models import Slider,Team

#  subtitle = models.CharField(max_length=255, )
#     button_text = models.CharField(max_length=200, )
#     photo = models.ImageField(upload_to="media/slider/%Y/", )
#     created_date = models.DateTimeField(auto_now_add=True, )
#     url = models.CharField(max_length=1000)
    
class SliderTestCase(TestCase):
    def setUp(self) -> None:
        self.headline = "Test Headline"
        Slider.objects.create(headline=self.headline,
        subtitle="Test Subtitle",
        button_text="Test Button Text",
        photo="Test Photo",
        url="Test URL")
        
    def testSlider(self):
        slider = Slider.objects.get(headline=self.headline)
        self.assertEqual(slider.headline, "Test Headline")
        self.assertEqual(slider.subtitle, "Test Subtitle")
        self.assertEqual(slider.button_text, "Test Button Text")
        self.assertEqual(slider.photo, "Test Photo")
        self.assertEqual(slider.url, "Test URL")

    def tearDown(self) -> None:
        Slider.objects.get(headline=self.headline).delete()
        return super().tearDown()
