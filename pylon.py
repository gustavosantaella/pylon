import argparse
from os import mkdir, path
from time import sleep

module_directory = "./src/modules"
middlewares_directory = "./src/middlewares"

def required_args(required_args:dict):
    for required_arg in required_args:
            if not args[required_arg]:
             raise Exception(f"{required_arg} parameter is required.")
def create_controller(args):
    required_args(
        ['directory', "filename", "controller"]
    ) 
    directory = args['directory']
    filename  = args['filename'] + "_controller"
    directory_destination = f"{module_directory}/{directory}"
    controller = args['controller'][0].upper() + args['controller'][1:] 
    if not path.exists(directory_destination):
        mkdir(directory_destination)
    file_path = f"{directory_destination}/{filename}.py"
    if path.exists(file_path):
        raise Exception("filename already exists")
    with open(file_path, "w+") as main_file, open("./stubs/controller.stub", "r") as stub_file:
        stub_lines = stub_file.readlines()
        class_name_index =stub_lines.index("class {{class_name}}:\n")
        stub_lines[class_name_index] = f"class {controller}:\n"        
        for line in stub_lines:
            main_file.write(line)
  
def create_middleware(args):          
    required_args(
        ["middleware"]
    ) 
    
    middleware = args["middleware"]
    middlewares_path = f"{middlewares_directory}/{middleware}.py"
    if  path.exists(middlewares_path):
        raise Exception("Middleware alredy exists")
    with open(middlewares_path, "w+") as main_file, open("./stubs/middleware.stub", "r") as stub_file:
        stub_lines = stub_file.readlines()
        middleware_name_index =stub_lines.index("def {{middleware_name}}(next, *arg, **args):\n")
        stub_lines[middleware_name_index] = f"def {middleware}(next, *arg, **args):\n"        
        for line in stub_lines:
            main_file.write(line)  
 
    
parser = argparse.ArgumentParser(description='Short args to create resources')
parser.add_argument('-c', '--controller',   action="store", dest='controller', help="Create a new controller")
parser.add_argument('-mi', '--middleware',   action="store", dest='middleware', help="Create a new middleware")
parser.add_argument('-f', '--filename',   action="store", dest='filename', help="filename of the resource")
parser.add_argument('-r', '--route',   dest='route', help="Create a route prefix")
parser.add_argument('-dir', '--directory',   dest='directory', help="specif a directory module")


args = parser.parse_args()

actions = {
    # "controller": create_controller,
    "middleware": create_middleware,
}
args = vars(args)

        
if __name__ == "__main__":
    for arg in args:
        if arg in actions:
            actions[arg](args)
    