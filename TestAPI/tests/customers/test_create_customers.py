import pdb

import pytest
import logging as logger

from TestAPI.dao.customers_dao import CustomersDAO
from TestAPI.src.helpers.customers_helper import CustomerHelper
from TestAPI.src.utilities.genericUtility import generate_random_email_and_password


@pytest.mark.tcid29
def test_create_customer_only_email_and_password():

    logger.info(" test new customer only with email and password")
    random_info = generate_random_email_and_password()
    logger.info(random_info)

    email=random_info['email']
    password=random_info['password']

    # Create payload
    # payload ={'email':email, 'password':password}  not gone use because using helper class for payload


    #make the call
    cust_obj = CustomerHelper()
    cust_api_info = cust_obj.create_customer(email=email, password=password)

    # verify email in the response

    assert cust_api_info['email'] == email, f"Create customer api returned the wrong email. Email: {email}"

    #import pdb; pdb.set_trace()   #to inspect api call is successfull or nor python debugger




   #verify customer is created in the database

    cust_dao = CustomersDAO()
    cust_info = cust_dao.get_customer_by_email(email)

    id_in_api = cust_api_info['id']
    id_in_db = cust_info[0]['ID']

    assert id_in_api==id_in_db,f"Create customer response ID is not same as in the database  Email: {email}"
