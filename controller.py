from model import Model
from view import View
from model import Format
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
        self.format = Format()

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
        self.model.load(filename)
        command = self.view.get_command()
        while command != 4:
            if command == 0:
                self.view.show_db(iter(self.model))
            elif command == 1:
                s = self.view.input().split()
                res = self.model.count(self.format.LineToList(s))
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
                            self.model.add_item(arg)
                        else:
                            self.view.error()
                    except ValueError:
                        self.view.error()
            elif command == 3:
                self.view.show_menu()
            elif command == 5:
                self.model.sort(0)
            elif command == 6:
                self.model.sort(1)
            elif command == 7:
                self.model.sort(2)
            elif command == 8:
                self.model.sort(3)
            else:
                self.view.error()

            command = self.view.get_command()

        self.model.save(filename)
