# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/


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
