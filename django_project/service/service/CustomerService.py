from service.dao.CustomerDAO import CustomerDAO
from .BaseService import BaseService


class CustomerService(BaseService):

    def get_dao(self):
        return CustomerDAO()
