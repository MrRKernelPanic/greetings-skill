import re
from adapt.intent import IntentBuilder
from mycroft.skills.core import (MycroftSkill,intent_handler,intent_file_handler)
from mycroft.audio import wait_while_speaking, is_speaking
#some of this lot required for messing with files and paths.
from os.path import join, isfile, abspath, dirname
from mycroft.util import play_wav

from pushover import Client

class GreetingsSkill(MycroftSkill):
    
    def __init__(self):
        super(GreetingsSkill, self).__init__("GreetingsSkill")
        #setup the sound file and the sound process.
        self.sound_file = join(abspath(dirname(__file__)), 'snd','bomb.wav')
        self.beep_process = None

 
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
        
        how_are_you_intent = IntentBuilder("HowAreYouIntent").require("HowAreYouKeyword").build()
        self.register_intent(how_are_you_intent, self.handle_how_are_you_intent)   
        
        da_bomb_intent = IntentBuilder("DaBombIntent").require("DaBombKeyword").build()
        self.register_intent(da_bomb_intent, self.handle_da_bomb_intent)   
   
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
        
    def handle_how_are_you_intent(self, message):
        self.speak_dialog("howareyou")  
    
    def handle_da_bomb_intent(self, message):
        #self.speak_dialog("howareyou")   Do stuff here!!!
        client = Client("uMC4uvNmeaZqb4amQ4PXXLd48LyFGu", api_token="ayr3k9882mg9p8apd87cwffmbd99iv")
        client.send_message("Dropped the Bomb", title="Mycroft Boom")
        #Play the WAV.
        self.beep_process = play_wav(self.sound_file)
    
    def _stop_beep(self):
        if self._is_playing_beep():
            self.beep_process.kill()
            self.beep_process = None
   
    def stop(self):
        pass

def create_skill():
    return GreetingsSkill()
