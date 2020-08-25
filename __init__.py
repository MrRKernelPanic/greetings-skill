from mycroft import MycroftSkill, intent_file_handler


class Greetings(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('greetings.intent')
    def handle_greetings(self, message):
        self.speak_dialog('greetings')


def create_skill():
    return Greetings()

