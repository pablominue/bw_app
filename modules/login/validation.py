import json

def validate_credentials(user: str, password)-> bool:
    existing = json.loads(
        open('./credentials.json').read()
    )
    if user in list(existing.keys()):
        print(existing.get(user))
        if str(password) == str(existing.get(user)):
            return True
    
    return False

validate_credentials('admin', 1234)