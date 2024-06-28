from TestAPI.src.utilities.genericUtility import generate_random_email_and_password

import json

from TestAPI.src.utilities.requestsUtility import RequestsUtility


class CustomerHelper(object):

    def __init__(self):
        self.requests_utilities = RequestsUtility()

    def create_customer(self, email=None, password=None, **kwargs):

        if not email:
            ep = generate_random_email_and_password()

        if not password:
            password = "Password1"

        payload = dict()
        payload['email'] = email
        payload['password'] = password
        payload.update(kwargs)


        create_user_json = self.requests_utilities.post('customers', payload=json.dumps(payload), expected_status_code=201)

        return create_user_json
