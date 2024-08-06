import unittest
from EmotionDetection.emotion_detection import emotion_detector

class TestEmotionDetection(unittest.TestCase):
    def test_joy(self):
        sparks_joy = 'I am glad this happened'
        result_joy = emotion_detector(sparks_joy)
        self.assertEqual(result_joy['dominant_emotion'], 'joy')

    def test_anger(self):
        sparks_anger = 'I am really mad about this'
        result_anger = emotion_detector(sparks_anger)
        self.assertEqual(result_anger['dominant_emotion'], 'anger')

    def test_disgust(self):
        sparks_disgust = 'I feel disgusted just hearing about this'
        result_disgust = emotion_detector(sparks_disgust)
        self.assertEqual(result_disgust['dominant_emotion'], 'disgust')

    def test_sadness(self):
        sparks_sadness = 'I am so sad about this'
        result_sadness = emotion_detector(sparks_sadness)
        self.assertEqual(result_sadness['dominant_emotion'], 'sadness')

    def test_fear(self):
        sparks_fear = 'I am really afraid that this will happen'
        result_fear = emotion_detector(sparks_fear)
        self.assertEqual(result_fear['dominant_emotion'], 'fear')

if __name__ == '__main__':
    unittest.main()