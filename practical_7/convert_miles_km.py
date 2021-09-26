"""Covnert miles to kilometers.  Creator: Khan Thompson
Date: 20/09/2021
"""

from kivy.app import App
from kivy.lang import Builder

MILES_TO_KM = 1.60934

class MilesConverterApp(App):
    """ Convert miles to kilometers. """

    def build(self):
        """ build the Kivy app from the kv file """
        self.title = "Convert Miles To Kilometers"
        self.root = Builder.load_file('convert_miles_km.kv')
        return self.root  # build() should always return a widget object

    def handle_increment(self, value, increment):
        """increment the input(value) by increment."""
        try:
            result = int(value) + increment
            self.root.ids.input_number.text = str(result)
        except ValueError:
            self.root.ids.input_number.text = str(increment)
            pass


    def handle_calculate(self, value):
        """ Handle calculation (could be button press or other call),
        output result to label widget
        """
        try:
            result = float(value) * MILES_TO_KM
            self.root.ids.output_number.text = str(result)
        except ValueError:
            self.root.ids.output_number.text = str(0.0)
            pass

if __name__ in ('__main__', '__android__'):
MilesConverterApp().run()
