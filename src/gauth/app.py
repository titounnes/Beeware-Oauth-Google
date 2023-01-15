"""
Google Oauth
"""
import toga
from toga.style import Pack
from toga.style.pack import COLUMN, ROW
from gauth.modules import OAuth, Menu, Form, Yaml

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
        
        self.menu = Menu(self)
        self.menu.generate(Yaml(__file__).load('modules/config/menu.yaml'))

        self.auth = OAuth('gauth')
        user_info = self.auth.is_login()
        if user_info:
            self.main_window.info_dialog('Info', 'Welcome %s'%(user_info['name']))
            self.menu.toggle(['Logout'])
        else:
            self.menu.toggle(['Login'])

    async def menu_click(self, widget):
        match widget.text:
            case 'Login':
                self.login(widget)
            case 'Logout':
                await self.logout(widget)

    def login(self, widget):
        user_info = self.auth.login()
        self.main_window.info_dialog('Info', 'Welcome %s'%(user_info['name']))
        self.menu.toggle(['Login', 'Logout','Data 1','Data 2'])
    
    async def logout(self, widget):
        if await self.main_window.confirm_dialog('Confirmation', 'Are you sure?'):
            self.auth.logout()
            self.menu.toggle(['Login', 'Logout','Data 1','Data 2'])
            self.main_window.info_dialog('Info', 'You are logout succesfully.')

    def data_1(self, widget):
        pass 

    def data_2(self, widget):
        pass 

def main():
    return GAuth()
