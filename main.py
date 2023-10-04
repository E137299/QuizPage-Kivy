
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder


Builder.load_file("QuizPage.kv")

class QuizPageApp(App):
    def build(self):
        return QuizManager()

class QuizManager(ScreenManager):
    pass

class Question1Screen(Screen):
    def answer_question(self, bool):
        if bool:
            self.manager.current = "correct"
        else:
            self.manager.current = "incorrect"


class Question2Screen(Screen):
    def answer_question(self, text):
        if text.lower() == "deep in the heart of texas.":
            # self.manager.current = "correct"
            self.ids.test.text = "CORRECT"
            self.ids.test.font_size = 50
        else:
            # self.manager.current = "incorrect"
            self.ids.test.text = "WRONG"
            self.ids.test.font_size = 75
            self.ids.test.color = "red"

class CorrectScreen(Screen):
    def advance(self):
        self.manager.current = "question two"

class IncorrectScreen(Screen):
    def advance(self):
        self.manager.current = "question2"

QuizPageApp().run()
