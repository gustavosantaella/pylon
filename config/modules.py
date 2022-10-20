from glob import glob
import os

def register_modules():
    try:
       
        path = os.path.join(f'{__file__}', './../../src/modules/**/*_controller.py')
        files = glob(path, recursive=True)
        files = "".join(files).split('/')
        del files[0]
        for file in files:
            
            join = "".join(file)
            module = join.replace('\\', '.')     
            
            if 'modules' in module and 'controller' in module :
                # print(module)
                index = module.find('.py')
               
                try:
                    __import__(f'src.{module[0:-3]}') 
                    print(module[0:-3])
                except Exception as e:    
                    module = module[0:index]
                    print(module)
                    # print(module)
                    __import__(f'src.{module}') 
    except Exception as e:
        raise Exception(f'An error ocurred to find module; {e}')
    


