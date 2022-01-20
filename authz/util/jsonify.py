from flask import current_app

DEBUG_MSG_CODES = {
        "100": "ok",
        "101": "Unsupported Media Type",
        "103": "Database Error",
        "107": "Not Implemented"
        }

def jsonify(state={}, metadata={}, status={}, code=100, headers={}):
    data = state
    data.update(metadata)
    if current_app.debug:
        data["message"] = DEBUG_MSG_CODES[str(code)]
    data["code"] = code
    return data, status, headers
