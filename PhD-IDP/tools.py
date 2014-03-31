import json
import os

def convert_to_utf8(my_input):
    """
    Recursively encodes all strings of an input dictionary as UTF-8. Useful to eliminate unicode strings.

    @param my_input: A dictionary object.

    @return: Encoded dictionary.
    """
    if isinstance(my_input, dict):
        return {convert_to_utf8(key): convert_to_utf8(value) for key, value in my_input.iteritems()}
    elif isinstance(my_input, list):
        return [convert_to_utf8(element) for element in my_input]
    elif isinstance(my_input, unicode):
        return my_input.encode('utf-8')
    else:
        return my_input

def load_dic_in_json(filename):
    return convert_to_utf8(json.loads("".join(open(filename,"r").readlines())))

def save_dic_in_json(this, there):
    open(there, "w").write(json.dumps(this, sort_keys=False, indent=4, separators=(',', ': ')))

def create_dir(_dir):
    if not os.path.exists(_dir):
        os.makedirs(_dir)