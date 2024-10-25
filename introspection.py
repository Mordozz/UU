def introspection_info(obj):
    obj_name = type(obj).__name__
    obj_attr = [attr for attr in dir(obj) if not callable(getattr(obj, attr)) and not attr.startswith('__')]
    obj_method = [method for method in dir(obj) if callable(getattr(obj, method)) and not method.startswith('__')]
    obj_module = obj.__module__ if hasattr(obj, '__module__') else 'None'
    obj_doc = obj.__doc__ if hasattr(obj, '__doc__') else 'No documentation'

    introspection_result = {
        'type': obj_name,
        'attributes': obj_attr,
        'methods': obj_method,
        'module': obj_module,
    }

    return introspection_result


class Type:
    def __init__(self, name):
        self.name = name
        self.number = 43
        self.type = 'Memo'

    def declaring_name(self):
        return self.name

    def abstract(self):
        return False


inspect = Type('new_class')
print(introspection_info(inspect))
