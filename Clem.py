import openai
import random
import difflib
from abc import abstractmethod
from collections import deque

API_KEY = open("API_KEY.txt", "r").read()

openai.api_key = API_KEY


class BodyParts:

    def __init__(self):
        self.current_xposition = 0 
        self.current_yposition = 0
        self.current_zposition = 0


    @abstractmethod
    def listening_gesture(self, current_robot_emotion):
        pass

    @abstractmethod
    def return_to_neutral_positon(self):
        '''Returns all body part coordinates to 0.'''
        self.current_xposition = 0
        self.current_xposition = 0
        self.current_zposition = 0


class Head(BodyParts):
    
    def __init__(self):
        super().__init__()


    def listening_gesture(self, current_robot_emotion):
        '''Moves body part to signify listening, expressing 
        current_robot_emotion'''
                
        if current_robot_emotion == "sympathetic_1":
            
            self.current_yposition += 20

            for i in range(6):
                self.current_zposition += 10
                self.current_zposition -= 10                
                
                
            print("*Clem nods delicately*") 
        
        elif current_robot_emotion == "sympathetic_2":

            self.current_yposition += 10

            for i in range(8):
                self.current_zposition += 5
                self.current_zposition -= 5                                
                
            print("*Clem nods delicately*")

        elif current_robot_emotion == "sympathetic_3":
            
            self.current_yposition += 30
            
            for i in range(6):
                self.current_zposition += 10
                self.current_zposition -= 10                
                
            print("*Clem nods sympathetically*")

        elif current_robot_emotion == "pleased_2":
            
            self.current_yposition += 40

            for i in range(6):
                self.current_zposition += 30
                self.current_zposition -= 30                                
                
            print("*Clem nods slowly*")

        elif current_robot_emotion == "pleased_3":
            
            self.current_yposition += 20

            for i in range(6):
                self.current_zposition += 5                
                self.current_zposition -= 5
                
            print("*Clem nods encouragingly*")

        else:
            pass # No head movement for other emotions.


    def return_to_neutral_positon(self):
        '''Returns body part x and y coordinates to 0.'''
        super().return_to_natural_position()


class EyeLids(BodyParts):

    def __init__(self):
        super().__init__()
    

    def listening_gesture(self, current_robot_emotion):
        '''Moves body part to signify listening, expressing 
        current_robot_emotion'''                        
        
        # Condition for all pleased emotions.
        if current_robot_emotion[0] == "p": 
            
            self.current_xposition += 15                
            self.current_yposition -= 10            
                
            print("*Clem squints*")
        # Condition for all other emorions.                         
        else:
            self.current_xposition += 10                
            self.current_yposition -= 5            
                
            print("*Clem squints slightly*")


    def return_to_neutral_positon(self):
        '''Returns body part x and y coordinates to 0.'''
        super().return_to_natural_position()


class Eyebrows(BodyParts):

    def __init__(self):
        super().__init__()


    def listening_gesture(self, current_robot_emotion):
        '''Moves body part to signify listening, expressing 
        current_robot_emotion'''                        
        
        c_r_e = current_robot_emotion 
        
        # Condition for all sympathetic emotions.
        if c_r_e[0] == "s" or c_r_e == "pleased_3": 
            
            self.current_xposition += 15                                        
                
            print("*Clem raises her eyebrows*")
                         
        else:
            pass # No eyebrow movement for other emotions.

    def return_to_neutral_positon(self):
        '''Returns body part x and y coordinates to 0.'''
        super().return_to_natural_position()


class Mouth(BodyParts): ######################################## check UML for R and L
    
    def __init__(self):
        super().__init__()

    
    def listening_gesture(self, current_robot_emotion):
        '''Moves body part to signify listening, expressing 
        current_robot_emotion'''                        
                
        if current_robot_emotion == "neutral": 
            
            self.current_xposition += 5                                        
                
            print("*Clem smiles delicately*")

        elif current_robot_emotion == "pleased_1": 
            
            self.current_xposition += 10                                        
                
            print("*Clem smiles*")

        elif current_robot_emotion == "pleased_2" or "pleased_3": 
            
            self.current_xposition += 15
            self.current_yposition += 5                                        
                
            print("*Clem smiles broadly*")

        # Condition for all sympathetic cases.
        else:
            self.current_xposition += 7                                        
                
            print("*Clem smiles sympathetically*")


    def return_to_neutral_positon(self):
        '''Returns body part x and y coordinates to 0.'''
        super().return_to_natural_position()
        

class Arms(BodyParts):

    def __init__(self):
        super().__init__()


    def hug(self, hands_hug_method, 
            safe_robot_force_method, user_force):
        '''Moves the x and y coordinate position and coordinates 
        with the hands to give the user a hug.'''

        self.current_xposition += 30
        self.current_yposition += 30

        # Call method to move hands once arms in # position.    
        hands_hug_method(safe_robot_force_method, user_force) 

        # Call method to safely apply robot force in interaction.    
        safe_robot_force_method(user_force)
            
        print("*Clem gives you a hug*")

    
    def big_hug(self, hands_hug_method, 
            safe_robot_force_method, user_force):
        '''Moves the x and y coordinate position and coordinates 
        with the hands to give the user a big hug.'''
        
        self.current_xposition += 50
        self.current_yposition += 30
        
        # Call method to move hands once arms in # position.
        hands_hug_method(safe_robot_force_method, user_force)  
        
        # Call method to safely apply robot force in interaction.                                         
        safe_robot_force_method("big hug") 
        
        print("*Clem gives you a big hug*")


    def squeeze_hand(self, hands_squeeze_method, 
            safe_robot_force_method, user_force):
        '''Moves the x and y coordinate position and coordinates 
        with the hands to squeeze the user's hand.'''
        
        self.current_xposition += 15
            
        hands_squeeze_method(safe_robot_force_method, user_force) 
            
        safe_robot_force_method(user_force)
            
        print("*Clem squeezes your hand*")
    

    def shake_hand(self, hands_shake_method, 
            safe_robot_force_method, user_force):
        '''Moves the x and y coordinate position and coordinates 
        with the hands to shake the user's hand.'''

        for i in range(4): # Shake hands with 4 shakes.
                self.current_xposition += 15
                safe_robot_force_method(user_force)
                hands_shake_method(safe_robot_force_method, user_force) 
                safe_robot_force_method(user_force)
                self.current_xposition -= 15
                i += 1
                        
        print("*Clem shakes your hand*")

    
    def give_high_five(self, hands_hfive_method, 
            safe_robot_force_method, user_force):
        '''Moves the x and y coordinate position and coordinates 
        with the hands to give the user a high-five.'''

        self.current_xposition += 80
        self.current_yposition += 30
            
        hands_hfive_method(safe_robot_force_method, user_force) 
            
        safe_robot_force_method(user_force)
            
        print("*Clem gives you a high five*")
                                                    

    def return_to_neutral_positon(self):
        '''Returns body part x and y coordinates to 0.'''
        super().return_to_natural_position()


    def listening_gesture(self, current_robot_emotion):
        return super().listening_gesture(current_robot_emotion)                
        '''Unused inherited abstract method'''


class Hands(BodyParts):

    def __init__(self):
        super().__init__()
    

    def hug(self, safe_robot_force_method, user_force):
        '''Moves the x and y coordinate position and coordinates 
        with the arms to give the user a hug.'''
        
        self.current_yposition -= 15
        safe_robot_force_method(user_force)


    def squeeze_hand(self, safe_robot_force_method, user_force):
        '''Moves the x and y coordinate position and coordinates 
        with the arms to squeeze the user's hand.'''

        self.current_yposition -= 20
        safe_robot_force_method(user_force)


    def shake_hand(self, safe_robot_force_method, user_force):
        '''Moves the x and y coordinate position and coordinates 
        with the arms to shake the user's hand.'''

        self.current_yposition -= 25
        safe_robot_force_method(user_force)


    def give_high_five(self, safe_robot_force_method, user_force):
        '''Moves the x and y coordinate position and coordinates 
        with the arms to give the user a high-five.'''

        self.current_xposition += 10
        safe_robot_force_method(user_force)


    def return_to_neutral_positon(self):
        '''Returns body part x and y coordinates to 0.'''
        super().return_to_natural_position()


    def listening_gesture(self, current_robot_emotion):
        return super().listening_gesture(current_robot_emotion)


class Torso(BodyParts):

    def __init__(self):
        super().__init__()
    

    def listening_gesture(self, current_robot_emotion):
        '''Moves body part to signify listening, expressing 
        current_robot_emotion'''                        
                
        if current_robot_emotion == "pleased_1": 
            
            self.current_zposition -= 5                                         
                
            print("*Clem leans backwards slightly*")

        elif current_robot_emotion == "pleased_2" or "pleased_3": 
            
            self.current_zposition -= 10                                                   
                
            print("*Clem leans backwards*")
        
        elif current_robot_emotion == "sympathetic_1":

            self.current_zposition += 5                                                   
                
            print("*Clem leans in slightly*")

        elif current_robot_emotion == "sympathetic_1" or "sympathetic":

            self.current_zposition += 10                                                   
                
            print("*Clem leans in*")

        else: 
            pass # Do nothing if neutral emotion displayed.         
                            
    
    def big_hug(self, physical_interaction, safe_robot_force_method, 
                user_force):
        '''Moves the x, y or z coordinate position depending on 
        interaction argument.'''
                
        self.current_zposition += 20
        safe_robot_force_method(user_force)


    def hug(self, physical_interaction, safe_robot_force_method, 
                user_force):
        '''Moves the x, y or z coordinate position depending on 
        interaction argument.'''        

        self.current_zposition += 15
        safe_robot_force_method(user_force)
        

    def return_to_neutral_positon(self):
        '''Returns body part x, y & z coordinates to 0.'''
        super().return_to_natural_position()


class PhysicalInteraction:     

    def apply_safe_robot_force(self, user_force):
        '''Calculates how much force to apply from hands, arms or 
        torso should be applied when physically interacting with 
        user, depending on how much force applied by user to Clem.'''        
        
        robot_force = 100 - user_force                

        return robot_force         


class RobotEmotion:

    def decide_robot_emotion(self, current_user_emotion_rating):
        '''Robot counter emotion decided based on user emotion rating.'''

        if current_user_emotion_rating <= -3: 
            return "sympathetic_3"
        elif current_user_emotion_rating == -2: 
            return "sympathetic_2"
        elif current_user_emotion_rating == -1: 
            return "sympathetic_1"
        elif current_user_emotion_rating == 0: 
            return "neutral"
        elif current_user_emotion_rating == 1: 
            return "pleased_1"
        elif current_user_emotion_rating == 2: 
            return "pleased_2"
        else:
            return "pleased_3"


    def suggest_physical_interaction(self, current_user_emotion_rating):
        """Suggests an appropriate physical interaction upon sayiing 
        goodbye, based on decided robot emotion

        Args:
            current_user_emotion_rating (integer): score relating to
            positive or negative emotion grade, to act as argument
            when calling self.decide_robot_emotion() method.

        Returns:
            string: a suggested physical interaction.
        """


        robot_emotion = self.decide_robot_emotion(current_user_emotion_rating)

        if robot_emotion == "sympathetic_2" or robot_emotion == "pleased_1":
            
            return "hug"

        elif robot_emotion == "sympathetic_1":
            
            return "squeeze hand"

        elif robot_emotion == "neutral":
            
            return "shake hand"

        elif robot_emotion == "pleased_2":
            
            return "high five"

        # Return "big hug" if current_robot_emotion is sympathetic_3 
        # or pleased_3. 
        else:

            return "big hug"   


class UserEmotion:

    def __init__(self):        
        self.user_emotion_score_history = [] # A stack used to access most recent emotion.
        
        ########################################################################################################## ref https://www.researchgate.net/publication/329290966_Emotion_Recognition_via_Facial_Expression_Utilization_of_Numerous_Feature_Descriptors_in_Different_Machine_Learning_Algorithms/citation/download
        self.user_emotion_choices = {
                                "neutral": ["fine", "OK", "grand"],
                                "negative_1": ["melancholy", "standoffish", "put off", "perturbed"],
                                "negative_2": ["upset", "anxious", "annoyed", "frustrated"], 
                                "negative_3": ["fearful", "saddened", "disgusted", "angered"],                                 
                                "positive_1": ["upbeat", "good spirits", "positive"], 
                                "positive_2": ["excited", "happy", "pleased"],
                                "positive_3": ["joyful", "surprised", "proud"]   
                                }
        self.graded_emotions = []
        self.emotions_scores = []


    def return_most_recent_user_emotion_grade(self):
        '''Treats self.user_emotion_score_history like a stack and 
        returns the top of the stack (last appended rating).'''

        index_of_last_item = len(self.user_emotion_score_history)-1

        return self.user_emotion_score_history[index_of_last_item] 
    

    def convert_emotion_string_to_graded_emotion(self, emotion):
        """Converts raw emotion string to a graded emotion of either
        negative_3, negative_2, negative_1, neutral, positive_1,
        positive_2, or positive_3.

        Args:
            emotion_or_emotions (string): single emotion string e.g.
            'angered', 'frustrated'.

            Return negative_3, negative_2, negative_1, neuutral, 
            positive_1, positive_2, positive_3 (string)
        """
        for key, value in self.user_emotion_choices.items():
            if emotion in value:
                return str(key)


    def convert_emotion_list_to_graded_emotion_list(self, emotion_list):
        """Converts raw emotion list to a graded emotion of 
        either negative_3, negative_2, negative_1, neutral, 
        positive_1, positive_2, or positive_3.

        Args:
            emotion_or_emotions (list): list of emotion strings e.g.
            ['angered', 'frustrated'].
        """

        graded_emotions = []

        for emotion in emotion_list:
            for key, value in self.user_emotion_choices.items():
                if emotion in value:
                    graded_emotions.append(str(key))

        return graded_emotions

                                                
    def save_graded_emotions(self, semantic_emotion_matches, 
                                        user_facial_expression, 
                                        user_posture_sensor):
        '''Adds record of graded positive or negative emotion sensed 
        by semantic emotion match, facial expression sensor, and
        posture sensor to current_pos_neg_emotions list.'''
        
        em_list = semantic_emotion_matches
        graded_emotions = self.convert_emotion_list_to_graded_emotion_list(em_list)
        
        for emotion in graded_emotions:
            self.graded_emotions.append(emotion)

        u_f_e = user_facial_expression
        u_f_e_graded_emotion = self.convert_emotion_string_to_graded_emotion(u_f_e)
        self.graded_emotions.append(u_f_e_graded_emotion)

        u_p_s = user_posture_sensor
        u_p_s_graded_emotion = self.convert_emotion_string_to_graded_emotion(u_p_s)
        self.graded_emotions.append(u_p_s_graded_emotion)
           

    def convert_nonpitch_emotions_to_graded_emotion_scores(self):
        '''Gives a numerical emotion rating depending on graded
        'negative'or 'positive' emotion recorded in 
        current_graded_emotions. 
        Negative emotions are given negative score, and positive 
        emotions are given positive score depending on grade recorded.
        '''
                
        for pos_or_neg_word in self.graded_emotions:
            if pos_or_neg_word == "positive_1":
                self.emotions_scores.append(1)
            elif pos_or_neg_word == "positive_2":
                self.emotions_scores.append(2)
            elif pos_or_neg_word == "positive_3":
                self.emotions_scores.append(3)
            elif pos_or_neg_word == "negative_1":
                self.emotions_scores.append(-1)
            elif pos_or_neg_word == "negative_2":
                self.emotions_scores.append(-2)
            elif pos_or_neg_word == "negative_3":
                self.emotions_scores.append(-3)
            else:
                self.emotions_scores.append(0) # Condition if neutral emotion.


    def calculate_median_user_emotion_score(self):
        '''Calculates median user emotion rating held in user_emotion_score list.'''
        
        index_of_last_item = len(self.emotions_scores)-1
        sorted_score = sorted(self.emotions_scores)
        
        # Calculation if odd number of records.
        if len(sorted_score) % 2 != 0:            
            halfway_index = index_of_last_item // 2 
            median = sorted_score[halfway_index] 
        else:
            # Calculation if even number of records.
            over_hway = index_of_last_item // 2
            under_hway = over_hway - 1
            num_to_divide = sorted_score[over_hway] + sorted_score[under_hway]
            median = num_to_divide // 2 

        return median


    def convert_pitch_emotions_to_graded_emotion_scores(self, baseline_pitch, user_voice_pitch):
        '''Multiply median emotion score according to pitch reading 
        (depending on base assessment): higher pitch readings 
        inferred as more intense emotion so multiplied by greater 
        value.'''
        
        median_rating = self.calculate_median_user_emotion_score()
                
        if baseline_pitch == "low":
            if user_voice_pitch <= 85 and user_voice_pitch < 110:
               pitch_emotion_rating = median_rating * 1

            elif user_voice_pitch <= 110 and user_voice_pitch < 135:
                pitch_emotion_rating = median_rating * 2
            
            elif user_voice_pitch <= 135 and user_voice_pitch < 160:
                pitch_emotion_rating = median_rating * 3

            else: 
                pitch_emotion_rating = median_rating * 4

        # Calculation if baseline assessment showed user as having naturally
        # high-pitched voice.
        else:
            if user_voice_pitch <= 155 and user_voice_pitch < 180:
                pitch_emotion_rating = median_rating * 1

            elif user_voice_pitch <= 180 and user_voice_pitch < 205:
                pitch_emotion_rating = median_rating * 2
            
            elif user_voice_pitch <= 205 and user_voice_pitch < 230:
                pitch_emotion_rating = median_rating * 3

            else: 
                pitch_emotion_rating = median_rating * 4
                            
        self.emotions_scores.append(pitch_emotion_rating)


    def calculate_mean_user_emotions_score(self):
        '''Takes the mean score of all recorded emotion ratings.'''

        num_of_ratings = len(self.emotions_scores)
        
        total_emotion_rating = 0

        for rating in self.emotions_scores:
            
            total_emotion_rating += rating

        mean_emotion_rating = total_emotion_rating // num_of_ratings

        return mean_emotion_rating


    def record_final_user_emotion_score(self, mean_emotion_rating):
        '''Appends final_user_emotion to user_emotion_score_history list.'''

        self.user_emotion_score_history.append(mean_emotion_rating)


    def reset_graded_emotions(self):
        '''Resets self.current_pos_neg_emotions, ready for next emotion 
        analysis.'''
        
        self.graded_emotions = []

    def reset_emotions_scores(self):
        '''Resets self.current_user_emotion_scores, ready for next emotion 
        analysis and subsequent calculation.'''
        
        self.emotions_scores = []
    

class SemanticSearch:
    
    def __init__(self):
        self.emotions_to_match = ["neutral", "fine", "grand", "melancholy", 
                                "standoffish", "put off", "perturbed",
                                "upset", "anxious", "annoyed", "frustrated", 
                                "fearful", "saddened", "disgusted", "angered",                                 
                                "upbeat", "good spirits", "positive", 
                                "excited", "happy", "pleased","joyful", 
                                "surprised", "proud"]  
        

    def emotions_match(self, user_message_list):
        '''Uses a difflib search method of user message to find a close emotions match.'''
        
        matches = []

        for word in user_message_list:            
            
            closest_match = difflib.get_close_matches(word, self.emotions_to_match, n=1)
            if closest_match:
                matches.append(closest_match)

        # Ensure list of elements returned rather than list of single element 
        # lists.
        return [item for match in matches for item in match] 
        
       
class ExpressionSensor:

    def __init__(self):
        self.emotions_to_match = ["neutral", "fine", "grand", "melancholy", 
                                "standoffish", "put off", "perturbed",
                                "upset", "anxious", "annoyed", "frustrated", 
                                "fearful", "saddened", "disgusted", "angered",                                 
                                "upbeat", "good spirits", "positive", 
                                "excited", "happy", "pleased","joyful", 
                                "surprised", "proud"]

        self.emotions_final_index = len(self.emotions_to_match) -1
        self.random_index = random.randint(0, self.emotions_final_index)


    def sense_facial_expression(self):
        '''Simulates facial expression recognition sensor by returning random 
        emotion.'''

        return self.emotions_to_match[self.random_index]


class PostureSensor(ExpressionSensor):

    def __init__(self):
        super().__init__()


    def match_posture_to_emotion(self):
        '''Simulates posture recognition sensor by returning random emotion.'''

        return self.emotions_to_match[self.random_index]


class PitchSensor:

    def __init__(self):        
        self.baseline_pitch = self.assess_pitch()        
        self.user_pitch = 0
        

    def baseline_assess_natural_pitch(self, natural_pitch):
        '''Simulates baseline assessment of natural pitch of normal speaking 
        voice (without emotion) and decides whether user's voice is naturally
        low or high-pitched.'''

        if natural_pitch < 165:
            return "low"

        else:
            return "high"  


    def assess_pitch(self):
        '''Simulated reading of pitch in user's voice, based on baseline 
        assessment.'''

        if self.baseline_assess_natural_pitch == "low":
            self.user_pitch = random.randint(85, 185)

        else:
            self.user_pitch = random.randint(155, 255)


class Dialogue:

    def __init__(self, chat_log_history, messages_to_reply_to=[]):
        
        self.chat_log_history = chat_log_history
        self.messages_to_reply_to = messages_to_reply_to        

    def respond(self, new_chat_log):
        '''Makes calls to Chat GPT API and prompts user for input before saving
        said input, responding and saving response.'''                
        
        # Update chat_log history.
        self.chat_log_history.append(new_chat_log)

        # system_content gives brief of Clem's role. ################################################ WILL THIS CAUSE AN ERROR?  
        system_content = '''You are a caring social assistant who listens to 
                        elderly people and responds so that they feel heard and
                        understood. You may give advice occasionally.'''

        response = openai.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": system_content},
                *self.chat_log_history, # Unpack chat_log_history.
                {"role": "user", "content": new_chat_log["content"]}
            ]
        )        

        clem_response = response.choices[0].message.content
        
        formatted_clem_response = clem_response.strip("\n").strip()

        self.chat_log_history.append({"role": "assistant", "content": formatted_clem_response})
        
        return formatted_clem_response



    def say_goodbye(self, user_emotion_score_history, first_user_emotion_score, final_user_emotion_score):
        """Returns a goodbye message that comments on the user's 
        emotional journey from the start of conversation to the end. 

        Args:
            first_user_emotion_score (integer): first emotion score 
            reading.

            final_user_emotion_score (integer): final emotion score 
            reading.
        
        """

        pos_msg = '''POS I'm glad that you seem to be feeling more positive since 
                    the start of our chat. I hope that I can continue to have 
                    a positive impact on your mood!'''
        
        no_change_pos = '''NO_C_POS I'm glad that you seem to have maintained a positive
                        outlook during our chat. Please know that this is a 
                        safe space to talk about negative emotions, should you 
                        wish to  during our next chat.'''

        no_change_neg = '''NO_C_NEG I'm sorry that I don't appear to have improved your
                        mood. I hope I can have a more positive influence in our
                        next chat.'''
        
        neg_msg = '''NEG I'm sorry that you seem to be feeling less positive about 
                    things since the start of our conversation. I hope I can 
                    make you feel better the next time we chat.'''
        
        if len(user_emotion_score_history) == 0:
            return "I'm sorry we didn't get to chat; maybe next time. Goodbye!"
        # Reflect on user's emotional score readings, comparing first and last.
        elif first_user_emotion_score < final_user_emotion_score:
            return pos_msg

        elif first_user_emotion_score > final_user_emotion_score:
            return neg_msg

        # Condition if no change but final score is positive.
        elif final_user_emotion_score > 0:
            return no_change_pos

        # Condition if no change but final score is netural or negative.
        else:
            return no_change_neg


    def user_choice_confirmed(self, user_choice, general_conf=False, 
                            quit_conf=False):
        """Returns True if user enters 'y' or 'q', False if 'n' or 
        'c' (depending on state). Prompts to try again if none of 
        these choices entered.

        Args:
            user_choice (string): 'y' or 'n' if general confirmation,
            'q' or 'c' if confirming goodbye message.
            general_conf (Boolean): True if used as general confirmation.
            quit_conf (Boolean): True if used as confirmation of user
            wanting to quit.
        
        """

        while True:
            if general_conf:
                try:
                    if user_choice.lower() == "y":                    
                        return True

                    elif user_choice.lower() == "n":
                        return False
                        
                except AttributeError:
                    
                    raise AttributeError("/n!! Please choose 'y' or 'n' !!/n")

            elif quit_conf:

                try:                

                    if user_choice.lower() == "q":
                        return True

                    elif user_choice.lower() == "c":
                        return False            

                except AttributeError:
                    
                    raise AttributeError(("/n!! Please choose 'q' or 'c' !!/n"))
    

    def print_end_of_speech_prompt(self): 
        '''Prompts user to check if they have finished their speech input or
        if they would like to add more. Returns Boolean'''

        prompts = ["Anything else on your mind?","Would you like to"
            " add anything else?", "Do you want to tell me more about that?"]
        
        random_reply_index = random.randint(0, len(prompts) - 1)
                
        print(prompts[random_reply_index])
                            

description_of_carer_role = '''You are a caring social assistant who listens to
                            elderly people and responds so that they feel heard
                            and understood. You may give advice occasionally.
                            '''
dialogue = Dialogue(chat_log_history = [{"role": "system",
                                        "content": description_of_carer_role}])            
                            
# CLI logic.
if __name__ == "__main__":

    messages_to_reply_to = deque([])
        
    user_message_string = ""
    
    user_name = input("Please enter your first name or the name you would like me"
                    " to call you: ") 

    print("Hi, " + user_name + ". What would you like to chat about" 
                    " today?")
    while True:

        if dialogue.user_wants_to_quit():
            # Call goodbye message.
            dialogue.say_goodbye()

        else:

            first_user_input = input()

        # Catch error if no speech inputted #################################################################### test
        try:
            
            messages_to_reply_to.append(first_user_input)
            print("first input: ",messages_to_reply_to)
            ######################################################## add listening gestures
            dialogue.end_of_speech_check()                
            if dialogue.user_is_at_end_of_speech():
                second_user_input = "."    
            else:
                second_user_input = input() 
            
            messages_to_reply_to.append(" " + second_user_input)
            
            
            user_message_string += messages_to_reply_to.popleft() + messages_to_reply_to.pop() #####################################
            print("string: ", user_message_string)
            updated_chat_log = {"role": "user", 
                        "content": user_message_string
                        }
                
            print(dialogue.clem_message(updated_chat_log))

        except AttributeError: 
            print("I'll give you a bit longer to think...")
            continue
