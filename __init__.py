from adapt.intent import IntentBuilder
from mycroft.skills.core import MycroftSkill

class GreetingsSkill(MycroftSkill):
    
    def __init__(self):
        super(GreetingsSkill, self).__init__("GreetingsSkill")
    
    def initialize(self):
        greetings_intent= IntentBuilder("GreetingsIntent"). \
            require("GreetingsKeyword").build()
        self.register_intent(greetings_intent, self.handle_greetings_intent)
        
    def handle_greetings_intent(self, message):
        self.speak_dialog("greetings")

    def stop(self):
        pass

def create_skill():
    return Greetings()

