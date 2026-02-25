import base64
from imaplib import IMAP4_SSL as IMAP
from os import environ
import requests

from dotenv import load_dotenv

from . import CONFIG

if __name__ == "__main__":
    load_dotenv()

    # print(CONFIG)

    emcon = CONFIG["email"]
    CLIENT_ID = emcon["client_id"]
    TENANT_ID = emcon["tenant_id"]
    CLIENT_SECRET = environ[emcon["client_secret_env_var"]]
    SCOPE = emcon["scopes"][0]

    token_url = f"https://login.microsoftonline.com/{TENANT_ID}/oauth2/v2.0/token"
    data = {
        "grant_type": "client_credentials",
        "client_id": CLIENT_ID,
        "client_secret": CLIENT_SECRET,
        "scope": SCOPE,
    }
    response = requests.post(token_url, data=data)
    # TODO check status code
    access_token = response.json()["access_token"]
    # print(access_token)

    response = requests.get(
        emcon["example_query"]["url"],
        headers={
            "content-type": "application/json",
            "Authorization": f"Bearer {access_token}",
        },
    )
    print(response.text)

    # TODO factor out token retreval into separate method
    # auth_string = f"user={TENANT_ID}\1auth=Bearer {access_token}\1\1"
    # auth_string = "user=%s\1auth=Bearer %s\1\1" % (TENANT_ID, access_token)
    # auth_string = "user=%s\1auth=Bearer %s\1\1" % (emcon["account_login"], access_token)
    # auth_string = f"user={config['email']['account_login']}\\x01auth=Bearer\\x01{access_token}\\x01\\x01"
    # auth_string = (
    #     f"user={emcon['account_login']}\\"
    #     f"x01auth=Bearer\\"
    #     f"x01{access_token}"
    #     f"\\x01\\x01"
    # )

    # def xoauth2_callback(resp):
    #     print("response:")
    #     print(resp)
    #     print("")
    #     return auth_string
    #
    # with IMAP(
    #     host=emcon["incoming"]["server"], port=emcon["incoming"]["port"]
    # ) as imap_connection:
    #     imap_connection.authenticate("XOAUTH2", xoauth2_callback)
    #     # imap_connection.authenticate(
    #     #     "XOAUTH2",
    #     #     # lambda _: f"user={emcon['account_login']}\1auth=Bearer {access_token}\1\1".encode(),
    #     #     lambda _: f"user={TENANT_ID}\1auth=Bearer {access_token}\1\1".encode(),
    #     # )
