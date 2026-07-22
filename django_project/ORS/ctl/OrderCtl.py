from datetime import datetime

from django.shortcuts import render
from .BaseCtl import BaseCtl
from service.utility.DataValidator import DataValidator
from service.models import Order
from service.service.OrderService import OrderService
from service.service.CustomerService import CustomerService
from ORS.utility.HtmlUtility import HtmlUtility


class OrderCtl(BaseCtl):
    def preload(self, request):
        """Load college list for the college dropdown before rendering the form."""
        order_list = OrderService().search({})

        self.preload_data["order_list"] = order_list

        self.preload_data["customer_select"] = HtmlUtility.get_list_from_beans(
            "customer_ID",
            int(self.form.get("customer_ID") or 0),
            self.preload_data["customer_list"],
        )

        return self.preload_data

    def request_to_form(self, requestForm):
        self.form["id"] = requestForm.get("id", 0)
        self.form["name"] = requestForm.get("name", "")
        self.form["phone"] = requestForm.get("phone", "")
        self.form["email"] = requestForm.get("email", "")
        self.form["city"] = requestForm.get("city", "")
        self.form["customer_ID"] = requestForm.get("customer_ID", 0)
        self.form["customerName"] = requestForm.get("customerName", "")

    def model_to_form(self, obj):
        if obj is None:
            return
        self.form["id"] = obj.id
        self.form["name"] = obj.name
        self.form["phone"] = obj.phone
        self.form["email"] = obj.email
        self.form["city"] = obj.city
        self.form["customer_ID"] = int(obj.customer_ID) if obj.customer_ID else 0
        self.form["customerName"] = obj.customerName

    def form_to_model(self, obj):
        """Populate a Student model instance from the form dictionary."""
        pk = int(self.form.get("id", 0))
        if pk > 0:
            obj.id = pk
        obj.name = self.form.get("name", "")
        obj.phone = self.form.get("phone", "")
        obj.email = self.form.get("email", "")
        obj.city = self.form.get("city", "")
        obj.customer_ID = self.form.get("customer_ID", 0)
        obj.customerName = self.get_customer_name(obj.customer_ID)
        return obj

    def input_validation(self):
        """Validate required fields and populate inputError messages."""
        super().input_validation()
        inputError = self.form.get("inputError", {})
        if DataValidator.isNull(self.form.get("name")):
            inputError["name"] = "Name can not be null"
            self.form["error"] = True

        if DataValidator.isNull(self.form.get("city")):
            inputError["city"] = "City can not be null"
            self.form["error"] = True

        if DataValidator.isNull(self.form.get("phone")):
            inputError["phone"] = "Mobile Number can not be null"
            self.form["error"] = True
        elif not DataValidator.isMobileNumber(self.form.get("phone")):
            inputError["phone"] = "Mobile Number must be 10 digits"
            self.form["error"] = True

        if DataValidator.isNull(self.form.get("email")):
            inputError["email"] = "Email can not be null"
            self.form["error"] = True
        elif not DataValidator.isEmail(self.form.get("email")):
            inputError["email"] = "Email must be a valid email address"
            self.form["error"] = True

        if (
            DataValidator.isNull(self.form.get("customer_ID"))
            or self.form.get("customer_ID") == "0"
        ):
            inputError["customer_ID"] = "Customer can not be null"
            self.form["error"] = True
        elif self.get_college_name(self.form.get("customer_ID")) == "":
            inputError["customer_ID"] = "Please select a valid college"
            self.form["error"] = True

        return self.form.get("error", False)

    def display(self, request, params={}):
        """Render the Student form, loading existing student data when an id is provided."""
        if params["id"] > 0:
            r = self.get_service().get(params["id"])
            self.model_to_form(r)
        res = render(
            request,
            self.get_template(),
            {"form": self.form, "preload_data": self.preload(request)},
        )
        return res

    def submit(self, request, params={}):
        """Save the Student form data and re-render the form with a success message."""
        r = self.form_to_model(Order())
        self.get_service().save(r)
        self.form["id"] = r.id
        self.form["error"] = False
        self.form["message"] = "Data is saved"
        self.model_to_form(r)
        res = render(
            request,
            self.get_template(),
            {"form": self.form, "preload_data": self.preload(request)},
        )
        return res

    def get_customer_name(self, college_id):
        if DataValidator.isNull(college_id):
            return ""
        customer = CustomerService().get(customer_id)
        if customer is None:
            return ""
        return customer.name

    def get_template(self):
        """Return the template path for the Student form."""
        return "ors/Customer.html"

    def get_service(self):
        """Return the StudentService instance for database operations."""
        return OrderService()
