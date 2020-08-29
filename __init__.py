from adapt.intent import IntentBuilder
from mycroft.skills.core import MycroftSkill

class GreetingsSkill(MycroftSkill):
    
    def __init__(self):
        super(GreetingsSkill, self).__init__("GreetingsSkill")
    
    def initialize(self):
        #For each command you need an intent and register, these 2 lines are for hello.
        #This then call the 'def handler' that gives the response.  For each intent there should be a generated .VOC file that has the keyword.
        #The .voc file should have the same name as the required "", e.g. "HelloKeyword" below
        
        hello_intent = IntentBuilder("HelloIntent").require("HelloKeyword").build()
        self.register_intent(hello_intent, self.handle_hello_intent)
        
        goodbye_intent = IntentBuilder("GoodbyeIntent").require("GoodbyeKeyword").build()
        self.register_intent(goodbye_intent, self.handle_goodbye_intent)
        
        good_evening_intent = IntentBuilder("GoodEveningIntent").require("GoodEveningKeyword").build()
        self.register_intent(good_evening_intent, self.handle_good_evening_intent)
    
        good_morning_intent = IntentBuilder("GoodMorningIntent").require("GoodMorningKeyword").build()
        self.register_intent(good_morning_intent, self.handle_good_morning_intent)
        
        good_afternoon_intent = IntentBuilder("GoodAfternoonIntent").require("GoodAfternoonKeyword").build()
        self.register_intent(good_afternoon_intent, self.handle_good_afternoon_intent)        
        
    
    #For each of the above intents there is a response, held in the .dialog files (can choose any of them!)
    def handle_hello_intent(self, message):
        self.speak_dialog("hello")
        
    def handle_goodbye_intent(self, message):
        self.speak_dialog("goodbye")
                                                                        
    def handle_good_evening_intent(self, message):
        self.speak_dialog("goodevening")
    
    def handle_good_morning_intent(self, message):
        self.speak_dialog("goodmorning")
    
    def handle_good_afternoon_intent(self, message):
        self.speak_dialog("goodafternoon")        
    
    def stop(self):
        pass

def create_skill():
    return GreetingsSkill()
