def success_response(data, message=None):
    return {"success": True, "message": message, "data": data}

def error_response(message=None):
    return {"success": False, "message": message, "data": None}