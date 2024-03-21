import os
import inspect


def save_class_docstrings(class_, output_file):
    """saves the docstring of each method in the class in output_file"""
    with open(output_file, 'a') as f:
        f.write(f"Class: {class_.__name__}\n\n")

        members = inspect.getmembers(class_)
        methods = [member for member in members if inspect.isfunction(member[1]) and not member[0].startswith('__')]
        for method in methods:
            method_docstring = inspect.getdoc(method[1])
            if method_docstring:
                f.write(f"{method[0]} Method: \n")
                f.write(method_docstring + "\n\n")
