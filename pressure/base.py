from bson import  ObjectId

def convert_to_params(params):
    """
    参数转换
    Parameters
    ----------
    params

    Returns
    -------
    params dict
    """
    if not isinstance(params, dict):
        return params

    for k, v in params.items():
        if isinstance(v, dict):
            params[k] = convert_to_params(v)
        if isinstance(v, ObjectId):
            params[k] = str(v)

    return params