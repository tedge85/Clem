import unittest
from Clem import EyeLids, Head, Arms, Hands, PhysicalInteraction, PitchSensor, PostureSensor, ExpressionSensor, RobotEmotion, SemanticSearch, UserEmotion, Dialogue

class ListeningRobotEmotionTestsLayerOne(unittest.TestCase):
    """Test listening gestures where robot emotion informs listening
    gesture."""

    def setUp(self):

        self.head = Head()

        self.r_emotion = RobotEmotion()


    def test_head_listening_gesture_y_position(self):
        """Test nodding listening gesture works with 
        RobototEmotion.decide_robot_emotion() value as argument."""

        curr_r_emotion = self.r_emotion.decide_robot_emotion(5)

        self.head.listening_gesture(curr_r_emotion)

        y_pos = self.head.current_yposition

        self.assertEqual(y_pos, 20)


class ListeningRobotEmotionTestsLayerTwo(unittest.TestCase):
    """Test user emotions to robot emotions conversion."""

    def setUp(self):
        
        self.user_emotion = UserEmotion()

        self.r_emotion = RobotEmotion()        


    def test_most_recent_user_emotion_score(self):
        """Test eyelid listening gesture works with 
        RobototEmotion.decide_robot_emotion() value as argument
        after latest user emotion passed to 
        RobotEmotion.decide_robot_emotion."""
    
        em1 = "annoyed"
        em2 = "grand"
        em_list = ["joyful","happy","upbeat"]

        user_em = self.user_emotion              

        user_em.save_graded_emotions(em_list,em1,em2)

        # This should ensure user_em.emotions_scores 
        # = [-2,0,1,2,3] 
        user_em.convert_nonpitch_emotions_to_graded_emotion_scores()
        
        # user_em.current_user_emotion_scores should now be [-2,0,1,2,3,2]
        user_em.convert_pitch_emotions_to_graded_emotion_scores("low", 120)

        # mean_score should now calculate as 1.
        mean_score = user_em.calculate_mean_user_emotions_score()        
    
        user_em.record_final_user_emotion_score(mean_score)

        final_user_em = user_em.return_most_recent_user_emotion_grade()

        self.assertEqual(final_user_em, 1)


class ListeningRobotEmotionTestsLayerThree(unittest.TestCase):
    """Test listening gestures where user emotion informs robot 
    emotion before robot emotion informs listening gesture."""

    def setUp(self):
        
        self.user_emotion = UserEmotion()

        self.r_emotion = RobotEmotion()

        self.eyelids = EyeLids()

        em1 = "annoyed"
        em2 = "grand"
        em_list = ["joyful","happy","upbeat"]

        user_em = self.user_emotion              

        user_em.save_graded_emotions(em_list,em1,em2)

        # This should ensure user_em.emotions_scores 
        # = [-2,0,1,2,3] 
        user_em.convert_nonpitch_emotions_to_graded_emotion_scores()
        
        # user_em.current_user_emotion_scores should now be [-2,0,1,2,3,2]
        user_em.convert_pitch_emotions_to_graded_emotion_scores("low", 120)

        # mean_score should now calculate as 1.
        mean_score = user_em.calculate_mean_user_emotions_score()        
    
        user_em.record_final_user_emotion_score(mean_score)

        self.final_user_em = user_em.return_most_recent_user_emotion_grade()        


    def test_eyelids_listening_gesture_x_position(self):
        """Test eyelid listening gesture works with 
        RobototEmotion.decide_robot_emotion() value as argument
        after latest user emotion passed to 
        RobotEmotion.decide_robot_emotion."""
        
        # curr_r_emotion should now be 'pleased_1'.
        curr_r_emotion = self.r_emotion.decide_robot_emotion(self.final_user_em)          

        # This method should adjust eyelid x position to 15.
        self.eyelids.listening_gesture(curr_r_emotion)

        x_pos = self.eyelids.current_xposition

        self.assertEqual(x_pos, 15)


class PhysicalInteractionTests(unittest.TestCase):

    def setUp(self):
        
        self.arms = Arms()

        self.hands = Hands()

        self.phys_int = PhysicalInteraction()

        self.arms.hug(self.hands.hug, self.phys_int.apply_safe_robot_force, 70) 


    def test_hug_arms_xposition(self):
        
        x_pos = self.arms.current_xposition

        self.assertEqual(x_pos, 30)

    
    def test_hug_arms_yposition(self):
    
        y_pos = self.arms.current_yposition

        self.assertEqual(y_pos, 30)

    
    def test_hug_hands_yposition(self):
        
        y_pos = self.hands.current_yposition

        self.assertEqual(y_pos, -15)      
        

unittest.main()