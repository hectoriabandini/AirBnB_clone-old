#!/usr/bin/python3
"""Custom Python Command Line Interface for managing object instances."""
import cmd
import shlex
import models
from datetime import datetime
from models.base_model import BaseModel
from models import storage
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb)"
    __classes = [
        "Amenity",
        "BaseModel",
        "City",
        "Place",
        "Review",
        "State",
        "User"
    ]

    def precmd(self, line):
        """Call the original precmd method to maintain its behavior"""
        line = super().precmd(line)

        
        print()

        return line

    def do_create(self, args):
        """create an instance of a class ,save it and print id
        """
        args = args.split()
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        else:
            new_instance = eval(args[0] + '()')
            models.storage.save()
            print(new_instance.id)

    def do_show(self, args):
        """Display the string representation of a specific instance.
        """
        arg_lists = args.split()
        if len(arg_lists) == 0:
            print("** class name missing **")
        elif arg_lists[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        elif len(arg_lists) == 1:
            print("** instance id missing **")
        else:
            obj = models.storage.all()
            key_value = arg_lists[0] + '.' + arg_lists[1]
            if key_value in obj:
                print(obj[key_value])
            else:
                print("** no instance found **")

    def do_destroy(self, args):
        """Delete an instance
        """
        args = args.split()
        objects = models.storage.all()

        if len(args) == 0:
            print('** class name missing **')
        elif args[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print('** instance id missing **')
        else:
            key = args[0] + '.' + args[1]
            if key in objects.keys():
                objects.pop(key, None)
                models.storage.save()
            else:
                print('** no instance found **')

    def do_all(self, args):
        """Display a string representation of all instances   
        """
        args = args.split()
        objects = models.storage.all()
        new_string = []

        if len(args) == 0:
            for obj in objects.values():
                new_string.append(obj.__str__())
            print(new_string)
        elif args[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        else:
            for obj in objects.values():
                if obj.__class__.__name__ == args[0]:
                    new_string.append(obj.__str__())
            print(new_string)

    def do_update(self, args):
        """update an instance
        """
        objects = models.storage.all()
        args = args.split(" ")

        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        elif len(args) == 2:
            print("** attribute name missing **")
        elif len(args) == 3:
            print("** value missing **")
        else:
            key = args[0] + '.' + args[1]
            obj = objects.get(key, None)

            if not obj:
                print("** no instance found **")
                return

            setattr(obj, args[2], args[3].lstrip('"').rstrip('"'))
            models.storage.save()

    def check_class_name(self, name=""):
        """Check if stdin user typed class name and id."""
        if len(name) == 0:
            print("** class name missing **")
            return False
        else:
            return True

    def check_class_id(self, name=""):
        """Check class id"""
        if len(name.split(' ')) == 1:
            print("** instance id missing **")
            return False
        else:
            return True

    def found_class_name(self, name=""):
        """Find the name class."""
        if self.check_class_name(name):
            args = shlex.split(name)
            if args[0] in HBNBCommand.__classes:
                if self.check_class_id(name):
                    key = args[0] + '.' + args[1]
                    return key
                else:
                    print("** class doesn't exist **")
                    return None

    def do_quit(self, args):
        """<Quit> Command To Exit The Program"""
        return True

    def do_EOF(self, args):
        """Handles end of file"""
        return True

    def emptyline(self):
        """dont execute anything when user
           press enter an empty line
        """
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()
