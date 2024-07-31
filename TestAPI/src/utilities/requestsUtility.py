import os
import requests
from TestAPI.src.configs.hosts_config import API_HOSTS
from requests_oauthlib import OAuth1
import logging as logger

from TestAPI.src.utilities.credentialsUtility import CredentialsUtility


class RequestsUtility(object):
    def __init__(self):
        self.env = os.environ.get('ENV', 'test')
        self.base_url = API_HOSTS[self.env]

        wc_creds = CredentialsUtility.get_wc_api_keys()
        self.auth = OAuth1(wc_creds['WC_KEY'], wc_creds['WC_SECRET'])

    def assert_status_code(self):  #verify status code of the call
        assert self.status_code == self.expected_status_code, f"Bad Status Code" \
                                                              f"Expcted Status code {self.expected_status_code}, Actual Status code is {self.status_code}" \
                                                              f"URL:{self.url}, Response Json : {self.rs_json}"

    def post(self, endpoints, payload=None, headers=None, expected_status_code=200):
        if not headers:
            headers = {"Content-Type": "application/json"}

        self.url = self.base_url + endpoints

        rs_api = requests.post(url=self.url, data=payload, headers=headers, auth=self.auth)

        self.status_code = rs_api.status_code
        self.expected_status_code = expected_status_code
        self.rs_json = rs_api.json()

        self.assert_status_code()


        logger.debug(f"POST API response is {self.rs_json}")

        return self.rs_json

    def get(self, endpoints, payload=None, headers=None, expected_status_code=200):
        if not headers:
            headers = {"Content-Type": "application/json"}

        self.url = self.base_url + endpoints

        rs_api = requests.get(url=self.url, data=payload, headers=headers, auth=self.auth)

        self.status_code = rs_api.status_code
        self.expected_status_code = expected_status_code
        self.rs_json = rs_api.json()

        self.assert_status_code()

        logger.debug(f"GET API response is {self.rs_json}")

        return self.rs_json

