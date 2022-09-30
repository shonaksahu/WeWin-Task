
import base64
import json
import datetime


def token_generator():
    
    t = {
        "name" : "shonak",
        "email" : "shonak@bot.com",
        "password" : "shonak123",
        "expire" : str(datetime.datetime.now())       
    }
    t = json.dumps(t)
    t = t.encode("ascii")
    base64_bytes = base64.b64encode(t)
    base64_string = base64_bytes.decode("ascii")
    print(f"Encoded string: {base64_string}")
    
token_generator()

    
