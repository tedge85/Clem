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

        ems = ["positive_1","positive_2","neutal","positive_3","negative_2"]

        self.user_emotion.graded_emotions = ems

        self.user_emotion.convert_nonpitch_emotions_to_graded_emotion_scores()
        

    def test_user_emotion_scores_without_pitch(self):

        emotion_scores = self.user_emotion.emotions_scores      

        self.assertEqual(emotion_scores, [1,2,0,3,-2])
        

    def test_calculate_median_user_emotion_score_odd_num_entries(self):
        '''Tests method with odd number of entries in 
        self.current_user_emotion_scores'''
        
        method = self.user_emotion.calculate_median_user_emotion_score()

        self.assertEqual(method, 1)


    def test_convert_emotion_string_to_graded_emotion(self):    
        
        user_em = self.user_emotion

        method = user_em.convert_emotion_string_to_graded_emotion("excited")

        self.assertEqual(method, "positive_2")


    def test_convert_emotion_list_to_graded_emotion_list(self):    
        
        e_list = ["OK", "upset", "upbeat"]

        user_em = self.user_emotion

        method = user_em.convert_emotion_list_to_graded_emotion_list(e_list)

        self.assertEqual(method, ["neutral", "negative_2", "positive_1"])
        

    def test_convert_pitch_emotions_to_graded_emotion_scores(self):
        
        self.user_emotion.convert_pitch_emotions_to_graded_emotion_scores("high", 180)
        
        emotion_scores = self.user_emotion.emotions_scores      

        self.assertEqual(emotion_scores, [1,2,0,3,-2,2])    
    

class SecondUserEmotionTests(unittest.TestCase):

    def setUp(self):
        
        self.user_em = UserEmotion()
        
        ems = ["positive_1","positive_2","neutal","positive_3","negative_2"]

        self.user_em.graded_emotions = ems

        self.user_em.convert_nonpitch_emotions_to_graded_emotion_scores()

        self.user_em.convert_pitch_emotions_to_graded_emotion_scores("high", 180)


    def test_calculate_mean_user_emotions_score(self):

        method = self.user_em.calculate_mean_user_emotions_score()        

        self.assertEqual(method, 1)


    def test_append_user_emotion_ratings_without_pitch(self):

        user_em = self.user_em

        curr_emotion_ratings = user_em.emotions_scores

        expected_result = [1,2,0,3,-2,2]

        self.assertEqual(curr_emotion_ratings, expected_result)
    

    def test_record_final_user_emotion_score(self):

        mean = self.user_em.calculate_mean_user_emotions_score()
        
        self.user_em.record_final_user_emotion_score(mean)

        emotion_history = self.user_em.user_emotion_score_history

        self.assertEqual(emotion_history, [1])


    def test_save_graded_emotions(self):

        user_em = self.user_em

        em_list = ["joyful","happy","upbeat"]
        em1 = "annoyed"
        em2 = "grand"        

        user_em.save_graded_emotions(em_list,em1,em2)

        updates_to_list = ["positive_3","positive_2","positive_1","negative_2",
                         "neutral"]

        previous_list = ["positive_1","positive_2","neutal","positive_3", 
                        "negative_2"]

        expected_list = previous_list + updates_to_list
        
        stored_emotions = user_em.graded_emotions

        self.assertEqual(stored_emotions,expected_list)


    def test_reset_graded_emotions(self):

        self.user_em.reset_graded_emotions()

        current_emotions = self.user_em.graded_emotions

        self.assertEqual(current_emotions, [])


    def test_reset_emotions_scores(self):

        self.user_em.reset_emotions_scores()

        current_emotions_scores = self.user_em.emotions_scores

        self.assertEqual(current_emotions_scores, [])

    
class ThirdUserEmotionTests(unittest.TestCase):

    def setUp(self):
        
        self.user_emotion = UserEmotion()

        self.user_emotion.user_emotion_score_history = [0,2,4,1,2,-1]
        
        self.user_emotion.emotions_scores = [3,2,3,2]
    

    def test_calculate_median_user_emotion_score_even_num_entries(self):
        '''Tests method with even number of entries in 
        self.current_user_emotion_scores'''                

        method = self.user_emotion.calculate_median_user_emotion_score()

        self.assertEqual(method, 2)


    def test_return_most_recent_user_emotion_grade(self):

        method = self.user_emotion.return_most_recent_user_emotion_grade()

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