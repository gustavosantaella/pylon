from glob import glob
import os

def register_modules():
    try:
        path = os.path.join(f'{__file__}', '../../src/modules/**/*_controller.py')
        files = glob(path, recursive=True)
        files = "".join(files).split('/')
        for file in files:
            join = "".join(file)
            module = join.replace('\\', '.')
            index = module.find('.py')
            # module = module[0:index]
            if 'modules' in module and 'controller' in module:
                # module = module.replace(".py", "")
                __import__(f'src.{module[0:-3]}')
    except Exception as e:
        raise Exception(f'An error ocurred to find module; {e}')
    


