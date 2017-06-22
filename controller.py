from model import Model
from view import View
from configurations.configurations import Config


class Controller:
    """
    Controller part of MVC
    """
    def __init__(self):
        """
        Constructor for Controller class
        """
        config = Config()
        self.model = Model(config.get_setting("Serialize", "serialize"))
        self.view = View()
        self.filename = None

    def start(self, filename):
        """
        This method starts the controller
        """
        self.filename = filename
        self.view.show_menu()
        self.read_commands(filename)

    def read_commands(self, filename):
        """
        Reads command from input, and processing them
        """
        arg0 = 'name'
        arg1 = 'val'
        command = self.view.get_command()
        while command != 4:
            if command == 0:
                self.view.show_db(self.model.return_db(self.filename))
            elif command == 1:
                s = self.view.input().split()
                res = self.model.count(
                    [{arg0: s[i * 2], arg1: s[i * 2 + 1]}
                        for i in range((int(len(s) / 2)))],
                    filename)
                if isinstance(res, str):
                    self.view.notfound(res)
                else:
                    self.view.output(res)
            elif command == 2:
                arg = self.view.new().split()
                if len(arg) != 2:
                    self.view.error()
                else:
                    try:
                        if int(arg[1]) > 0:
                            self.model.add_item(arg, filename)
                        else:
                            self.view.error()
                    except ValueError:
                        self.view.error()
            elif command == 3:
                self.view.show_menu()
            else:
                self.view.error()

            command = self.view.get_command()
