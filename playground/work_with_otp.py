import datetime
import jwt
import time

secret = "jksadjjdsafjklfsda;jflkads"
wrong_secret = "ssdgaasdddd"

payload = {
    "my_name": "Daniil",
    "age": 16,
    "exp": datetime.datetime.now(datetime.timezone.utc) + datetime.timedelta(seconds=500),
}

encode_jwt = jwt.encode(
    payload=payload,
    key=secret,
    algorithm="HS256"
)
print(encode_jwt)
time.sleep(15)

decoded = jwt.decode(
    encode_jwt,
    wrong_secret,
    algorithms=["HS256"],
    # # options={
    # #     "verify_signature": False
    # }
)
print(decoded)
