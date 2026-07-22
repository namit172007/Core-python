from django.shortcuts import render, redirect

from .base_ctl import BaseCtl
from ..models import User
from ..service.student_service import StudentService
from ..utility.data_validator import DataValidator


class StudentListCtl(BaseCtl):

    def request_to_form(self, request):
        self.form['first_name'] = request.POST.get('firstName')

    def display(self, request, params={}):
        student_list = self.get_service().search(self.form)
        self.form['list'] = student_list
        return render(request, self.get_template(), {'form': self.form})

    def submit(self, request, params={}):

        if request.POST.get('operation', '') == "next":
            self.form['page_no'] = int(request.POST['pageNo'])
            self.form['page_no'] += 1
        if request.POST.get('operation', '') == "previous":
            self.form['page_no'] = int(request.POST['pageNo'])
            self.form['page_no'] -= 1
        if request.POST.get('operation', '') == "search":
            self.form['page_no'] = 1

        student_list = self.get_service().search(self.form)
        self.form['list'] = student_list
        return render(request, self.get_template(), {'form': self.form})

    def get_service(self):
        return StudentService()

    def get_template(self):
        return 'studentlist.html'