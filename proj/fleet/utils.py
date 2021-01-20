def underscore_to_uppercase(s):
    ns = ''.join([i.capitalize() for i in s.split('_')])
    return ns


def uppercase_field_name(fields):
    new_fields = tuple(underscore_to_uppercase(item) for item in fields)

    return new_fields


def has_common_member(a, b):
    a_set = set(a)
    b_set = set(b)
    if a_set & b_set:
        return True
    else:
        return False
