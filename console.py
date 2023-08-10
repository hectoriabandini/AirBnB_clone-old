#!/usr/bin/python3

""" The console! command line interpreter for HBnB """
import cmd
from models import base_model
import json
import os.path
class HBNBCommand(cmd.Cmd):
    """ console class """
    prompt = "(hbnb)"
    class_mapping = {"BaseModel": base_model.BaseModel}

    def do_quit(self, arg):
        """ Quit command to exit the program """
        return True

    def do_EOF(self, arg):
        """ ctrl + D to exit the program """
        print()
        return True
    def emptyline(self):
        pass
    def do_create(self, arg):
        """Creates a new instance of BaseModel"""
        if not arg:
            print("* class name missing *")
            return

        try:
            new_instance = self.class_mapping[arg]()
            new_instance.save()
            print(new_instance.id)
        except:
            print("* class doesn't exist *")
if __name__ == '__main__':
    HBNBCommand().cmdloop()
