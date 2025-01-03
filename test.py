import unittest
from Clem import PitchSensor, PostureSensor, ExpressionSensor, SemanticSearch, UserEmotion


class SemanticSearchTests(unittest.TestCase):

    def setUp(self):
        
        self.semantic_search = SemanticSearch()        


    def test_search_matches(self):

        input_list = ["snow", "fine", "exciting", "angry", "joy", "rubbish", "angered",
                       "potato"]
        
        output = ["fine", "excited", "angered", "joyful", "angered"]

        self.assertEqual(self.semantic_search.emotions_match(input_list), output)
    

class ExpressionSensorTests(unittest.TestCase):

    def setUp(self):
        self.expression_sensor = ExpressionSensor()


    def test_sense_facial_expression(self):

        test_method = self.expression_sensor.sense_facial_expression()

        
        self.assertIn(test_method, self.expression_sensor.emotions_to_match)


class PostureSensorTests(unittest.TestCase):

    def setUp(self):
        self.posture_sensor = PostureSensor()

    def test_match_posture_to_emotion(self):

        test_method = self.posture_sensor.match_posture_to_emotion()

        
        self.assertIn(test_method, self.posture_sensor.emotions_to_match)


class PitchSensorTests(unittest.TestCase):

    def setUp(self):
        self.pitch_sensor = PitchSensor()        


    def test_low_baseline_assessment_normal(self):

        method = self.pitch_sensor.baseline_assess_natural_pitch(10)

        self.assertEqual(method, "low")

    def test_low_baseline_assessment_extreme(self):

        method = self.pitch_sensor.baseline_assess_natural_pitch(-125)

        self.assertEqual(method, "low")

    
    def test_high_baseline_assessment_normal(self):

        method = self.pitch_sensor.baseline_assess_natural_pitch(200)

        self.assertEqual(method, "high")

    
    def test_high_baseline_assessment_extreme(self):

        method = self.pitch_sensor.baseline_assess_natural_pitch(165)

        self.assertEqual(method, "high")


class FirstUserEmotionTests(unittest.TestCase):

    def setUp(self):
         
        self.user_emotion = UserEmotion()

        self.user_emotion.current_pos_neg_emotions = ["positive_1", 
                                                    "positive_2", 
                                                    "neutal", "positive_3", 
                                                    "negative_2"]

        self.user_emotion.append_user_emotion_ratings_without_pitch()
        

    def test_user_emotion_ratings_without_pitch(self):

        emotion_scores = self.user_emotion.current_user_emotion_scores      

        self.assertEqual(emotion_scores, [1,2,0,3,-2])
        

    def test_calculate_median_user_emotion_rating(self):

        method = self.user_emotion.calculate_median_user_emotion_rating()

        self.assertEqual(method, 1)

    
    def test_append_user_emotion_rating_based_on_pitch(self):
        
        self.user_emotion.append_user_emotion_rating_based_on_pitch("high", 180)
        
        emotion_scores = self.user_emotion.current_user_emotion_scores      

        self.assertEqual(emotion_scores, [1,2,0,3,-2,2])    


class SecondUserEmotionTests(unittest.TestCase):

    def setUp(self):
        
        self.user_emotion = UserEmotion()

        self.user_emotion.current_pos_neg_emotions = ["positive_1", 
                                                    "positive_2", 
                                                    "neutal", "positive_3", 
                                                    "negative_2"]

        self.user_emotion.append_user_emotion_ratings_without_pitch()

        self.user_emotion.append_user_emotion_rating_based_on_pitch("high", 180)


    def test_calculate_mean_user_emotion_rating(self):

        method = self.user_emotion.calculate_mean_user_emotion_rating()        

        self.assertEqual(method, 1)

    
    def test_store_mean_user_emotion_rating(self):
        mean = self.user_emotion.calculate_mean_user_emotion_rating()
        
        self.user_emotion.store_mean_user_emotion_rating(mean)

        emotion_history = self.user_emotion.user_emotion_rating_history

        self.assertEqual(emotion_history, [1])

    def test_reset_current_pos_neg_emotions(self):

        self.user_emotion.reset_current_pos_neg_emotions()

        current_emotions = self.user_emotion.current_pos_neg_emotions

        self.assertEqual(current_emotions, [])


    def test_reset_current_user_emotion_scores(self):

        self.user_emotion.reset_current_user_emotion_scores()

        current_emotions_scores = self.user_emotion.current_user_emotion_scores

        self.assertEqual(current_emotions_scores, [])

    
class ThirdUserEmotionTests(unittest.TestCase):

    def setUp(self):
        
        self.user_emotion = UserEmotion()

        self.user_emotion.user_emotion_rating_history = [0,2,4,1,-1]

    
    def test_view_most_recent_user_emotion_rating(self):

        method = self.user_emotion.view_most_recent_user_emotion_rating()

        self.assertEqual(method, -1)

        

unittest.main()