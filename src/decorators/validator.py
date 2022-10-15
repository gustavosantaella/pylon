from functools import wraps
import inspect

def validator(validatorName: str, **args):
    is_middleware = 'middleware' in args or False
    def decorator(function):
        @wraps(function)
        def validate(*param ,**params):
            path = inspect.getfile(function).split('\\')
            src_idnex = path.index('src')
            modules_index = path.index('modules')
            to_index = is_middleware == False and 2 or 0
            path_folder= '.'.join(path[src_idnex:modules_index + to_index])
            path = is_middleware == True and f'middlewares.{validatorName}' or f'validators.validate_{validatorName}'
            validator_file = f"{path_folder}.{path}"
            module = __import__(validator_file, fromlist=[validatorName])
            func = getattr(module, validatorName)
            return func(function, *param, **params)
        return validate
    return decorator