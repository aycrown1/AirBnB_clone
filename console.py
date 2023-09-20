#!/usr/bin/python3
""" The Console program for the HBnB clone
"""
import cmd
import sys
from models.base_model import BaseModel
from models.__init__ import storage
from models.city import City
from models.place import Place
from models.state import State
from models.amenity import Amenity
from models.review import Review
from models.user import User

"""
Attribute:
    classes (dictionary):  maps class names to their corresponding class objects.
"""
classes = {'BaseModel': BaseModel,
              'User': User, 'Place': Place,
              'State': State, 'City': City,
              'Amenity': Amenity,
              'Review': Review}

class HBNBCommand(cmd.Cmd):
    """
    HBNBCommand (class): Command-line interpreter that inherits from the cmd.Cmd class.
    """
    prompt = '(hbnb) '

    def do_quit(self, args):
        """Quit command to exit the program.
        Usage:
            quit
        """
        sys.exit()

    def do_EOF(self, args):
        """
        Exits the program if the user types in EOF (Ctrl+D).
        Usage:
            Ctrl-D
        """
        sys.exit()

    def do_create(self, args):
        """
        Creates a new instance of BaseModel,
        saves it (to the JSON file) and prints the id.
             Usage:
                 create <class name>
        """
        args = args.split()
        if not args:
            print("** class name missing **")
        elif args[0] not in classes:
            print("** class doesn't exist **")
        else:
            new_instance = classes.get(args[0])()
            print(new_instance.id)
            storage.save()

    def do_show(self, args):
        """
        Prints the string representation of an instance based on the class name and id.
            Usage: show <class name> <instance ID>
        """
        args = args.split()
        if not args:
            print("** class name missing **")
            return
        if args[0] not in classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        key = "{}.{}".format(args[0], args[1])
        obj = storage.all().get(key)
        if obj is None:
            print("** no instance found **")
        else:
            print(obj)

    def do_all(self, args):
        """
        Prints all string representation of all instances based or not on the class name.
             Usage:
                 all <class name> or <class name>.all()
        """
        args = args.split()
        obj_list = []
        if not args:
            for obj in storage.all().values():
                obj_list.append(str(obj))
            print(obj_list)
            return

        class_name = args[0]

        if class_name not in classes:
            print("** class doesn't exist **")
            return

        if len(args) > 1 and args[1] == "all()":
            obj_list = []
            for obj in storage.all().values():
                if obj.__class__.__name__ == class_name:
                    obj_list.append(str(obj))
            print(obj_list)
        else:
            obj_list = []
            for obj in storage.all().values():
                if obj.__class__.__name__ == class_name:
                    obj_list.append(str(obj))
            print(obj_list)

    def do_update(self, args):
        """
        Updates an instance based on the class name and id by adding or
        updating attribute (save the change into the JSON file).
        Usage:
            update <class name> <Instance ID> <attribute name> "<attribute value>"
        """
        args = args.split()
        if not args:
            print("** class name missing **")
            return
        if args[0] not in classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        key = "{}.{}".format(args[0], args[1])
        obj = storage.all().get(key)
        if obj is None:
            print("** no instance found **")
        else:
            if len(args) < 3:
                print("** attribute name missing **")
            elif len(args) < 4:
                print("** value missing **")
            else:
                attr_name = args[2]
                attr_value = ' '.join(args[3:])
                setattr(obj, attr_name, attr_value)
                storage.save()

    def do_destroy(self, args):
        """
        Deletes an instance based on the class name and id (save the change into the JSON file).
            Usage:
                destroy <class name> <instance ID>
                <class name>.destroy(<id>)
        """
        args = args.split()
        if not args:
            print("** class name missing **")
            return
        if args[0] not in classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        key = "{}.{}".format(args[0], args[1])
        obj = storage.all().get(key)
        if obj is None:
            print("** no instance found **")
        else:
            del storage.all()[key]
            storage.save()

    def do_count(self, args):
        """
            Counts/retrieves the number of instances.
        """
        obj_list = []
        storage = FileStorage()
        storage.reload()
        objects = storage.all()
        try:
            if len(args) != 0:
                eval(args)
        except NameError:
            print("** class doesn't exist **")
            return
        for key, val in objects.items():
            if len(args) != 0:
                if type(val) is eval(args):
                    obj_list.append(val)
            else:
                obj_list.append(val)
        print(len(obj_list))


    def emptyline(self):
        """Empty line method - does nothing"""
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
