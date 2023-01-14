import toga
    
class Menu(object):
    def __init__(self, app):
        self.app = app
        
    
    def generate(self, data):
        groups = {}
        cmd = {}
        group_order = 1
        for item in data:
            i = 0
            for key in data[item]: 
                cmd[item+'_cmd'] = toga.Command(
                    key['callback'],
                    text = key['text'],
                    shortcut = key.get('shortcut'),
                    enabled = key['enabled'],
                    section = i
                )
                i += 1
                if item == 'App':
                    cmd[item+'_cmd'].group = toga.Group.APP
                else:
                    if groups.get(item) is None:
                        groups[item] = toga.Group(item, order=group_order)
                        group_order += 1

                    cmd[item+'_cmd'].group = groups[item]
            
                self.app.commands.add(cmd[item+'_cmd'])

    def toggle(self, data):
        for item in self.app.commands:
            if type(item) == toga.command.Command:
                if item.text in data:
                    item.enabled = not item.enabled 
