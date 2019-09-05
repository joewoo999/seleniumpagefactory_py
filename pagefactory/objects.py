def require_not_none(obj, raise_msg: str = None) -> bool:
    if obj is not None:
        return True
    elif raise_msg is None:
        return False
    else:
        raise ReferenceError(raise_msg)
