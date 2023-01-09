"""
Google Oauth
"""
import toga
from toga.style import Pack
from toga.style.pack import COLUMN, ROW
from gauth.libs.OAuth import OAuth

import warnings
warnings.filterwarnings("ignore")

class GAuth(toga.App):

    def startup(self):
        """
        Construct and show the Toga application.

        Usually, you would add your application to a main content box.
        We then create a main window (with a name matching the app), and
        show the main window.
        """
        main_box = toga.Box()

        self.main_window = toga.MainWindow(title=self.formal_name)
        self.main_window.content = main_box
        self.main_window.show()

        auth = OAuth('gauth')
          
        user_info = auth.is_login() 
        if  user_info == False:
            user_info = auth.login()
            
        self.main_window.info_dialog('Info', 'Welcome %s'%(user_info['name']))
        
def main():
    return GAuth()
