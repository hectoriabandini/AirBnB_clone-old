#!/usr/bin/python3

""" The console! command line interpreter for HBnB """
import cmd

class HBNBCommand(cmd.Cmd):
    """ console class """
    prompt = "(hbnb)"

    def do_quit(self, arg):
        """ Quit command to exit the program """
        return True

    def do_EOF(self, arg):
        """ ctrl + D to exit the program """
        print()
        return True
    def emptyline(self):
        pass



if __name__ == '__main__':
    HBNBCommand().cmdloop()
