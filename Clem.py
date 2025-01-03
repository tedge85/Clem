import openai
import random
import difflib
from abc import abstractmethod
from collections import deque

API_KEY = open("API_KEY.txt", "r").read()

openai.api_key = API_KEY


class BodyParts:

    def __init__(self, current_xposition=0, current_yposition=0):
        self.current_xposition = current_xposition
        self.current_yposition = current_yposition


    @abstractmethod
    def listening_gesture(self, current_robot_emotion):
        pass

    @abstractmethod
    def return_to_neutral_positon(self):
        '''Returns all body part coordinates to 0.'''
        self.current_xposition = 0
        self.current_xposition = 0
    
class Head(BodyParts):
    
    def listening_gesture(self, current_robot_emotion):
        '''Moves body part to signify listening, expressing 
        current_robot_emotion'''
                
        if current_robot_emotion == "sympathetic_1":
            
            for i in range(6):
                self.current_yposition += 10                
                self.current_yposition -= 20
                
            print("*Clem nods delicately*") 
        
        elif current_robot_emotion == "sympathetic_2":
            for i in range(8):
                self.current_yposition += 10                
                self.current_yposition -= 20
                
            print("*Clem nods delicately*")

        elif current_robot_emotion == "sympathetic_3":
            for i in range(6):
                self.current_yposition += 20                
                self.current_yposition -= 40
            print("*Clem nods sympathetically*")

        elif current_robot_emotion == "pleased_2":
            for i in range(6):
                self.current_yposition += 20                
                self.current_yposition -= 40
                
            print("*Clem nods slowly*")

        elif current_robot_emotion == "pleased_3":
            for i in range(6):
                self.current_yposition += 30                
                self.current_yposition -= 60
                
            print("*Clem nods encouragingly*")

        else:
            pass # No head movement for other emotions.


    def return_to_neutral_positon(self):
        '''Returns body part x and y coordinates to 0.'''
        super().return_to_natural_position()


class EyeLids(BodyParts):
    
    def listening_gesture(self, current_robot_emotion):
        '''Moves body part to signify listening, expressing 
        current_robot_emotion'''                        
        
        # Condition for all pleased emotions.
        if current_robot_emotion[1] == "p": 
            
            self.current_xposition += 15                
            self.current_yposition -= 10            
                
            print("*Clem squints*")
                         
        else:
            self.current_xposition += 10                
            self.current_yposition -= 5            
                
            print("*Clem squints slightly*")


    def return_to_neutral_positon(self):
        '''Returns body part x and y coordinates to 0.'''
        super().return_to_natural_position()


class Eyebrows(BodyParts):
    
    def listening_gesture(self, current_robot_emotion):
        '''Moves body part to signify listening, expressing 
        current_robot_emotion'''                        
        
        c_r_e = current_robot_emotion 
        
        # Condition for all sympathetic emotions.
        if c_r_e[1] == "s" or c_r_e == "pleased_3": 
            
            self.current_xposition += 15                                        
                
            print("*Clem raises her eyebrows*")
                         
        else:
            pass # No eyebrow movement for other emotions.

    def return_to_neutral_positon(self):
        '''Returns body part x and y coordinates to 0.'''
        super().return_to_natural_position()


class Mouth(BodyParts): ######################################## check UML for R and L
    
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
        

class InteractingBodyParts(BodyParts): 

    @abstractmethod
    def __init__(self, current_xposition=0, current_yposition=0, 
                 current_zposition=0):
        super().__init__(current_xposition, current_yposition)
        self.current_zposition = current_zposition


    @abstractmethod
    def move(self, physical_interaction, safe_robot_force_method, user_force):
        '''Moves the x, y or z coordinate position depending on 
        interaction argument.'''
        pass


    @abstractmethod
    def return_to_neutral_positon(self):
        '''Returns body part coordinates x, y & z to 0.'''
        super().return_to_natural_position() # Reset x and y positions.
        self.current_zposition = 0
        

class Arms(InteractingBodyParts):    

    def move(self, physical_interaction, hands_move_method, 
            safe_robot_force_method, user_force):
        '''Moves the x, y or z coordinate position depending on 
        interaction argument.'''
        
        if physical_interaction == "big hug":
            self.current_xposition += 50
            self.current_yposition += 30
            hands_move_method() # Call method to move hands once arms in 
                                # position.
            safe_robot_force_method("big hug") # Call method to safely apply 
                                      # robot force in interaction.
            print("*Clem gives you a big hug*")

        elif physical_interaction == "hug":
            
            self.current_xposition += 30
            self.current_yposition += 30
            
            hands_move_method("hug") 
            
            safe_robot_force_method(user_force)
            
            print("*Clem gives you a hug*")

        elif physical_interaction == "squeeze hand":
            
            self.current_xposition += 15
            
            hands_move_method("squeeze hand") 
            
            safe_robot_force_method(user_force)
            
            print("*Clem squeezes your hand*")

        elif physical_interaction == "hand shake":

            for i in range(4): # Shake hands with 4 shakes.
                self.current_xposition += 15
                safe_robot_force_method(user_force)
                hands_move_method("hand shake") 
                safe_robot_force_method(user_force)
                self.current_xposition -= 15
                i += 1
                        
            print("*Clem shakes your hand*")

        elif physical_interaction == "high five":
            
            self.current_xposition += 80
            self.current_yposition += 30
            
            hands_move_method("high five") 
            
            safe_robot_force_method(user_force)
            
            print("*Clem gives you a high five*")


    def return_to_neutral_positon(self):
        '''Returns body part coordinates x, y & z to 0.'''
        super().return_to_natural_position()


    def listening_gesture(self, current_robot_emotion):
        return super().listening_gesture(current_robot_emotion)                


class Hands(InteractingBodyParts):
    
    def move(self, physical_interaction, hands_move_method, 
            safe_robot_force_method, user_force):
        '''Moves the x, y or z coordinate position depending on 
        interaction argument.'''
        
        if physical_interaction == "big hug" or "hug":

            self.current_yposition -= 15
            safe_robot_force_method(user_force)

        elif physical_interaction == "hand squeeze":

            self.current_yposition -= 20
            safe_robot_force_method(user_force)

        elif physical_interaction == "hand shake":

            self.current_yposition -= 25
            safe_robot_force_method(user_force)

        elif physical_interaction == "high five":

            self.current_xposition += 10
            safe_robot_force_method(user_force)


    def return_to_neutral_positon(self):
        '''Returns body part coordinates x, y & z to 0.'''
        super().return_to_natural_position()


    def listening_gesture(self, current_robot_emotion):
        return super().listening_gesture(current_robot_emotion)


class Torso(InteractingBodyParts):
    
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
                            
    
    def move(self, physical_interaction, hands_move_method, 
            safe_robot_force_method, user_force):
        '''Moves the x, y or z coordinate position depending on 
        interaction argument.'''
        
        if physical_interaction == "big hug":

            self.current_zposition += 20
            safe_robot_force_method(user_force)

        elif physical_interaction == "hug":

            self.current_zposition += 15
            safe_robot_force_method(user_force)

        else:
            pass


    def return_to_neutral_positon(self):
        '''Returns body part coordinates x, y & z to 0.'''
        super().return_to_natural_position()


class PhysicalInteraction:

    def __init__(self):
        
        self.robot_force = 0         


    def apply_safe_robot_force(self, user_force):
        '''Calculates how much force to apply from hands, arms and torso when 
        physically interacting with user, depending on how much force applied 
        by user to Clem.'''        

        force_total = user_force + self.robot_force

        while force_total < 100:
            self.robot_force += 1

        return self.robot_force

    
    def reset_robot_force(self):
        '''Resets robot_force attribute to zero immediately following a 
        physical intearaction.'''

        self.robot_force = 0


    def suggest_physical_interaction(self, current_robot_emotion):
        
        if current_robot_emotion == "negative_2" or "positive_1":
            
            return "hug"

        elif current_robot_emotion == "negative_1":
            
            return "squeeze hand"

        elif current_robot_emotion == "neutral":
            
            return "shake hand"

        elif current_robot_emotion == "positive_2":
            
            return "high five"

        # Return "big hug" if current_robot_emotion is sympathetic_3 
        # or positive_3. 
        else:

            return "big hug"         


class RobotEmotion:


    def __init__(self):
        self.current_robot_emotion = ""


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


class UserEmotion:


    def __init__(self):        
        self.user_emotion_rating_history = [] # A stack used to access most recent emotion.
        
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
        self.current_pos_neg_emotions = []
        self.current_user_emotion_scores = []


    def view_most_recent_user_emotion_rating(self):
        '''Treats self.user_emotion_rating_history like a stack and 
        returns the top of the stack (last appended rating).'''

        index_of_last_item = len(self.user_emotion_rating_history)-1
        return self.user_emotion_rating_history[index_of_last_item] 


    def commit_to_current_pos_neg_emotions(self, semantic_emotion_matches, 
                                        user_facial_expression, 
                                        user_posture_sensor):
        '''Adds record of graded positive or negative emotion sensed to 
        current_pos_neg_emotions list.'''
        

        for emotion in semantic_emotion_matches:
            for key, value in self.user_emotion_choices.items():
                if emotion == value:
                    self.current_pos_neg_emotions.append(key)

        for emotion in user_facial_expression:
            for key, value in self.user_emotion_choices.items():
                if emotion == value:
                    self.current_pos_neg_emotions.append(key)

        for emotion in user_posture_sensor:
            for key, value in self.user_emotion_choices.items():
                if emotion == value:
                    self.current_pos_neg_emotions.append(key)


    def append_user_emotion_ratings_without_pitch(self):
        '''Gives a numerical emotion rating depending on graded
        'negative'or 'positive' emotion recorded in 
        current_pos_neg_emotions, multiplied by pitch reading. 
        Negative emotions are given negative score, and positive 
        emotions are given positive score depending on grade recorded.
        Total is multiplied by score based on pitch sensor reading 
        (higher pitches suggest more intense emotion).'''
                

        for pos_or_neg_word in self.current_pos_neg_emotions:
            if pos_or_neg_word == "positive_1":
                self.current_user_emotion_scores.append(1)
            elif pos_or_neg_word == "positive_2":
                self.current_user_emotion_scores.append(2)
            elif pos_or_neg_word == "positive_3":
                self.current_user_emotion_scores.append(3)
            elif pos_or_neg_word == "negative_1":
                self.current_user_emotion_scores.append(-1)
            elif pos_or_neg_word == "negative_2":
                self.current_user_emotion_scores.append(-2)
            elif pos_or_neg_word == "negative_3":
                self.current_user_emotion_scores.append(-3)
            else:
                self.current_user_emotion_scores.append(0) # Condition if neutral emotion.


    def calculate_median_user_emotion_rating(self):
        '''Calculates median user emotion rating held in user_emotion_score list.'''
        
        index_of_last_item = len(self.current_user_emotion_scores)-1
        sorted_score = sorted(self.current_user_emotion_scores)
        
        if len(sorted_score)%2 != 0:
            # Calculation if odd number of records.
            halfway_index = index_of_last_item // 2 
            median = sorted_score[halfway_index] 
        else:
            # Calculation if even number of records.
            index_1 = index_of_last_item / 2
            index_2 = index_1 + 1
            num_to_divide = sorted_score[index_1] + sorted_score[index_2]
            median = num_to_divide // 2 

        return median


    def append_user_emotion_rating_based_on_pitch(self, baseline_pitch, user_voice_pitch):
        '''Multiply median emotion score according to pitch reading 
        (depending on base assessment): higher pitch readings 
        inferred as more intense emotion.'''
        
        median_rating = self.calculate_median_user_emotion_rating()
                
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
                            
        self.current_user_emotion_scores.append(pitch_emotion_rating)


    def calculate_mean_user_emotion_rating(self):
        '''Takes the mean score of all recorded emotion ratings.'''

        num_of_ratings = len(self.current_user_emotion_scores)
        
        total_emotion_rating = 0

        for rating in self.current_user_emotion_scores:
            
            total_emotion_rating += rating

        mean_emotion_rating = total_emotion_rating // num_of_ratings

        return mean_emotion_rating


    def store_mean_user_emotion_rating(self, mean_emotion_rating):
        '''Appends final_user_emotion to user_emotion_rating_history list.'''

        self.user_emotion_rating_history.append(mean_emotion_rating)


    def reset_current_pos_neg_emotions(self):
        '''Resets self.current_pos_neg_emotions, ready for next emotion 
        analysis.'''
        
        self.current_pos_neg_emotions = []

    def reset_current_user_emotion_scores(self):
        '''Resets self.current_user_emotion_scores, ready for next emotion 
        analysis and subsequent calculation.'''
        
        self.current_user_emotion_scores = []


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

    def clem_message(self, new_chat_log):
        '''Makes calls to Chat GPT API and prompts user for input before saving
        said input, responding and saving response.'''                
        
        # Update chat_log history.
        self.chat_log_history.append(new_chat_log)

        response = openai.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a caring social assistant who listens to elderly people and responds so that they feel heard and understood. You may give advice occasionally."},
                *self.chat_log_history, # Unpack chat_log_history.
                {"role": "user", "content": new_chat_log["content"]}
            ]
        )        

        clem_response = response.choices[0].message.content
        
        formatted_clem_response = clem_response.strip("\n").strip()

        self.chat_log_history.append({"role": "assistant", "content": formatted_clem_response})
        
        return formatted_clem_response



    def robot_verbal_response(self, user_input):
        pass

    
    

    def end_of_speech_check(self):
        '''Prompts user to check if they have finished their speech input or
        if they would like to add more.'''

        prompts = ["Anything else on your mind?","Would you like to"
            " add anything else?", "Do you want to tell me more about that?"]
        random_reply_index = random.randint(0, len(prompts) - 1)
        print(prompts[random_reply_index])
        user_choice = input("Type 'y' or 'n': ")
        while True:
            try:
                if user_choice.lower() == "y":
                    self.end_of_speech = False
                    return
                elif user_choice.lower() == "n":
                    self.end_of_speech = True
                    return
            except TypeError:
                print("/n!!Please choose 'y' or 'n'!!/n")            


dialogue = Dialogue(chat_log_history = [{"role": "system",
                                                      "content": "You are a" 
                                                      " caring social"
                                                      " assistant who listens"
                                                      " to elderly people and"
                                                      " responds so that they"
                                                      " feel heard and"
                                                      " understood. You may"
                                                      " give advice"
                                                      " occasionally."}])            
                            
# CLI logic.
if __name__ == "__main__":

    messages_to_reply_to = deque([])
    
        
    user_message_string = ""
    
    user_name = input("Please enter your first name or the name you would like me"
                    " to call you: ") 

    print("Hi, " + user_name + ". What would you like to chat about" 
                    " today?")
    while True:        
                        
        first_user_input = input()

        # Catch error if no speech inputted #################################################################### test
        try:
            
            messages_to_reply_to.append(first_user_input)
            print("first input: ",messages_to_reply_to)
            ######################################################## add listening gestures
            dialogue.end_of_speech_check()                
            if dialogue.end_of_speech:
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
