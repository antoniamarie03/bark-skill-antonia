from mycroft 
import MycroftSkill
import intent_file_handler

class Bark(MycroftSkill):
	def __init__(self):
		MycdoftSkill.__init__(self)
		
	@intent_file_handler('bark.intent')
	def handle_bark(self, massage):
		self.speak_dialoog('bark')
	

def create_skill():
	return Bark()
