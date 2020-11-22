def underscore_to_uppercase(s):
    ns = ''.join([i.capitalize() for i in s.split('_')])
    return ns


def uppercase_field_name(fields):
    new_fields = tuple(underscore_to_uppercase(item) for item in fields)
    print(fields, '====', new_fields)
    
    return new_fields
