import os
from dotenv import load_dotenv, dotenv_values

# loading variables from .env file
load_dotenv()
class CredentialsUtility(object):

    def __init__(self):
        pass
    @staticmethod
    def get_wc_api_keys():

        wc_key = os.getenv("WC_KEY")
        wc_secret = os.getenv("WC_SECRET")

        if not wc_key or not wc_secret:
            raise Exception("The API credentials must be in environment variable")

        else:
            return {'WC_KEY':wc_key, 'WC_SECRET':wc_secret}



    @staticmethod
    def get_db_credentials():

        db_user = os.getenv("DB_USER")
        db_password = os.getenv("DB_PASSWORD")

        if not db_user or not db_password:
            raise Exception("The Database credentials must be in environment variable")

        else:
            return {'DB_USER':db_user, 'DB_PASSWORD':db_password}


