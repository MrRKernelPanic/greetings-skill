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
        
        good_evening_intent = IntentBuilder("GoodEveningIntent").require("GoodEveningKeyword").build()
        self.register_intent(good_evening_intent, self.handle_good_evening_intent)
    
    
    
    #For each of the above intents there is a response, held in the .dialog files (can choose any of them!)
    def handle_hello_intent(self, message):
        self.speak_dialog("hello")
                                                                        
    def handle_good_evening(self, message):
        self.speak_dialog("goodevening")
        
    def stop(self):
        pass

def create_skill():
    return GreetingsSkill()
