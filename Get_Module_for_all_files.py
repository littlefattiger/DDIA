import argparse
import ast
from pathlib import Path
from collections import namedtuple

Import = namedtuple("Import", ["module", "name", "alias"])

def init_args(argv=None):
    p = argparse.ArgumentParser('Get_Module_for_all_files.py',
                                description='This is to get all distinct imported modules in the file path')
    p.add_argument('-p', '--path', help='File path you want to get all modules of python file', default=f'{Path(__file__).parent.resolve()}')

    args = p.parse_args(argv)   
    return args


def get_imports_for_file(file):
    with open(file) as fh:        
       root = ast.parse(fh.read(), file)
    
    modules_list_tuple = []

    for node in ast.iter_child_nodes(root):
        if isinstance(node, ast.Import):
            module = []
        elif isinstance(node, ast.ImportFrom):  
            module = node.module
        else:
            continue
        for n in node.names:
            modules_list_tuple.append(Import(module, n.name, n.asname))
    
    modules_set_from_file = set()

    for imported_tuple in modules_list_tuple:
        if not imported_tuple.module:
            modules_set_from_file.add(imported_tuple.name)
        else:
            modules_set_from_file.add(imported_tuple.module)
    # return distinct module names from that path
    return modules_set_from_file


def get_imports_from_path(path):

    # Get all python files for that path, exclude this file
    all_py_files = [str(py_file.absolute()) for py_file in Path(path).glob('**/*') if str(py_file.absolute()).endswith('.py') ]
    current_py_name = str(Path(__file__))
    if  current_py_name in all_py_files:
        all_py_files.remove(current_py_name)
    
    modules_set_in_list = [
        get_imports_for_file(py_file_name)
        for py_file_name in all_py_files
    ]
    # Put the result in set to remove duplicate modules
    return list(set().union(*modules_set_in_list))

def run():
    args = init_args()
    all_distinct_modules = get_imports_from_path(args.path)
    all_distinct_modules.sort()
    # Print out all modules for the path
    print(f"Here is all modules for path: {args.path}\n")
    print(all_distinct_modules)
    print("\n")
    return 

if __name__ == "__main__": 
    run()