from service.models import Customer
from .BaseDAO import BaseDAO


class CustomerDAO(BaseDAO):

    def get_model(self):
        return Customer

    def get_Unique(self):
        return ["name"]

    def populate(self, obj):
        return obj
