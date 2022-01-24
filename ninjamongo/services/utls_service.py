
def print_response_json(status,message,payload = {}):
    return {
        "status":status,
        "message":message,
        "payload":payload
    }