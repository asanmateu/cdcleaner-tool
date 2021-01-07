def strip_dict(d):
    """ Removes whitespaces in dictionary key value pairs given an input dictionary. """
    return {k.strip(): strip_dict(v) if isinstance(v, dict) else v.strip() for k, v in d.items()}


def df_to_object_type(df):
    """ Converts columns in dataframe to object type. """
    return df.apply(lambda x: x.astype(str))


def strip_df(df):
    """ Removes whitespaces in each dataframe object type column values. """
    return df.apply(lambda x: x.str.strip() if x.dtype == "object" else x)


def strip_lst(lst):
    """ Strips whitespaces from elements in a list"""
    return [i.strip() for i in lst]
