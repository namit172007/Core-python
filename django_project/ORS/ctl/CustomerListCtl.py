from django.shortcuts import render
from .BaseCtl import BaseCtl
from service.service.CustomerService import CustomerService
from ORS.utility.HtmlUtility import HtmlUtility


class CustomerListCtl(BaseCtl):

    def preload(self, request):
        customer_list = CustomerService().search({})
        self.preload_data["customer_select"] = HtmlUtility.get_list_from_beans(
            "customer_ID",
            int(self.form.get("customer_ID") or 0),
            customer_list,
        )
        return self.preload_data

    def request_to_form(self, requestForm):
        self.form["name"] = requestForm.get("name", None)
        self.form["phone"] = requestForm.get("phone", None)
        self.form["email"] = requestForm.get("email", None)
        self.form["city"] = requestForm.get("city", None)
        self.form["page_number"] = int(requestForm.get("page_number", 1))

    def display(self, request, params={}):
        self.page_list = self.get_service().search(self.form, page_number=1)
        res = render(
            request,
            self.get_template(),
            {"pageList": self.page_list, "form": self.form, "preload_data": self.preload(request)},
        )
        return res

    def submit(self, request, params={}):
        self.request_to_form(request.POST)
        page_number = self.form.get("page_number", 1)
        self.page_list = self.get_service().search(self.form, page_number=page_number)
        res = render(
            request,
            self.get_template(),
            {
                "pageList": self.page_list,
                "form": self.form,
                "preload_data": self.preload(request),
            },
        )
        return res

    def get_template(self):
        return "ors/CustomerList.html"

    def get_service(self):
        return CustomerService()
