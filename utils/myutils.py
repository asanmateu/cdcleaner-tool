def strip_dict(d):
    """ Removes whitespaces in dictionary key value pairs given an input dictionary. """
    return {k.strip(): strip_dict(v) if isinstance(v, dict) else v.strip() for k, v in d.items()}

