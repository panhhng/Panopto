import hashlib

def generate_auth_code(userkey, servername, shared_secret):
    payload = f"{userkey}@{servername}"
    signed_payload = f"{payload}|{shared_secret}"
    m = hashlib.sha1()
    m.update(signed_payload.encode('utf-8'))
    return m.hexdigest().upper()
