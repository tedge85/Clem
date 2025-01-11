import unittest
from Clem import PitchSensor, PostureSensor, ExpressionSensor, RobotEmotion, SemanticSearch, UserEmotion, Dialogue


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
        

    def test_calculate_median_user_emotion_rating_odd_num_entries(self):
        '''Tests method with odd number of entries in 
        self.current_user_emotion_scores'''
        
        method = self.user_emotion.calculate_median_user_emotion_rating()

        self.assertEqual(method, 1)


    def test_convert_emotion_string_to_grade(self):    
        
        method = self.user_emotion.convert_emotion_string_to_grade("excited")

        self.assertEqual(method, "positive_2")


    def test_convert_emotion_list_to_grade_list(self):    
        
        e_list = ["OK", "upset", "upbeat"]

        method = self.user_emotion.convert_emotion_list_to_grade_list(e_list)

        self.assertEqual(method, ["neutral", "negative_2", "positive_1"])
        

    def test_append_user_emotion_rating_based_on_pitch(self):
        
        self.user_emotion.append_user_emotion_rating_based_on_pitch("high", 180)
        
        emotion_scores = self.user_emotion.current_user_emotion_scores      

        self.assertEqual(emotion_scores, [1,2,0,3,-2,2])    


    def test_commit_to_current_pos_neg_emotions(self):

        em_list = ["fearful", "proud", "good spirits"]

        e = "grand"

        p = "OK"         

        self.user_emotion.commit_to_current_pos_neg_emotions(em_list, e, p)

        graded_em = ["positive_1", "positive_2", "neutal", "positive_3", 
                    "negative_2", "negative_3", "positive_3", "positive_1", 
                    "neutral", "neutral"] 
        
        self.assertEqual(self.user_emotion.current_pos_neg_emotions, graded_em)


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

        self.user_emotion.user_emotion_rating_history = [0,2,4,1,2,-1]
        
        self.user_emotion.current_user_emotion_scores = [3,2,3,2]
    

    def test_calculate_median_user_emotion_rating_even_num_entries(self):
        '''Tests method with even number of entries in 
        self.current_user_emotion_scores'''                

        method = self.user_emotion.calculate_median_user_emotion_rating()

        self.assertEqual(method, 2)


    def test_view_most_recent_user_emotion_rating(self):

        method = self.user_emotion.view_most_recent_user_emotion_rating()

        self.assertEqual(method, -1)


class RobotEmotionTest(unittest.TestCase):

    def setUp(self):
        
        self.r_emotion = RobotEmotion()


    def test_decide_robot_emotion(self):

        method = self.r_emotion.decide_robot_emotion(-5)

        self.assertEqual(method, "sympathetic_3")


    def test_suggest_physical_interaction_hug(self):

        method = self.r_emotion.suggest_physical_interaction(-2)

        self.assertEqual(method, "hug")


    def test_suggest_physical_interaction_squeeze_hand(self):

        method = self.r_emotion.suggest_physical_interaction(-1)

        self.assertEqual(method, "squeeze hand")


    def test_suggest_physical_interaction_shake_hand(self):

        method = self.r_emotion.suggest_physical_interaction(0)

        self.assertEqual(method, "shake hand")


    def test_suggest_physical_interaction_high_five(self):

        method = self.r_emotion.suggest_physical_interaction(2)

        self.assertEqual(method, "high five")


    def test_suggest_physical_interaction_bug_hug(self):

        method = self.r_emotion.suggest_physical_interaction(9)

        self.assertEqual(method, "big hug")


class DialogueTest(unittest.TestCase):

    def setUp(self):

        self.dialogue = Dialogue([{}],[])


    def test_say_goodbye_empty(self):

        method = self.dialogue.say_goodbye([],None,None)

        msg = "I'm sorry we didn't get to chat; maybe next time. Goodbye!"

        self.assertEqual(method, msg)


    def test_say_goodbye_pos(self):

        method = self.dialogue.say_goodbye([-1,0,3],-1,3)

        msg = '''POS I'm glad that you seem to be feeling more positive since 
                    the start of our chat. I hope that I can continue to have 
                    a positive impact on your mood!'''

        self.assertEqual(method, msg)

    
    def test_say_goodbye_neg(self):

        method = self.dialogue.say_goodbye([-1,3,-3],-1,-3)

        msg = '''NEG I'm sorry that you seem to be feeling less positive about 
                    things since the start of our conversation. I hope I can 
                    make you feel better the next time we chat.'''

        self.assertEqual(method, msg)


    def test_say_goodbye_no_change_pos(self):

        method = self.dialogue.say_goodbye([2,3,2],2,2)

        msg = '''NO_C_POS I'm glad that you seem to have maintained a positive
                        outlook during our chat. Please know that this is a 
                        safe space to talk about negative emotions, should you 
                        wish to  during our next chat.'''

        self.assertEqual(method, msg)

    
    def test_say_goodbye_no_change_neg(self):

        method = self.dialogue.say_goodbye([-2,3,-2],-2,-2)

        msg = '''NO_C_NEG I'm sorry that I don't appear to have improved your
                        mood. I hope I can have a more positive influence in our
                        next chat.'''

        self.assertEqual(method, msg)

    
    def test_user_choice_confirmed_general_conf_yes(self):
        
        choice = "Y"

        method = self.dialogue.user_choice_confirmed(choice, general_conf=True)

        self.assertEqual(method, True)

    
    def test_user_choice_confirmed_general_conf_no(self):
        
        choice = "N"

        method = self.dialogue.user_choice_confirmed(choice, general_conf=True)

        self.assertEqual(method, False)


    def test_user_choice_confirmed_quit_conf_yes(self):
        
        choice = "Q"

        method = self.dialogue.user_choice_confirmed(choice, quit_conf=True)

        self.assertEqual(method, True)

    
    def test_user_choice_confirmed_quit_conf_no(self):
        
        choice = "C"

        method = self.dialogue.user_choice_confirmed(choice, quit_conf=True)

        self.assertEqual(method, False)


unittest.main()