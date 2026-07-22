from django.shortcuts import render, redirect

from .base_ctl import BaseCtl
from ..models import TimeTable
from ..service.time_table_service  import TimeTableService
from ..utility.data_validator import DataValidator


class TimeTableListCtl(BaseCtl):

    def request_to_form(self, request):
        self.form['semester'] = request.POST.get('semester')

    def display(self, request, params={}):
        time_table_list = self.get_service().search(self.form)
        self.form['list'] = time_table_list
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

        time_table_list = self.get_service().search(self.form)
        self.form['list'] = time_table_list
        return render(request, self.get_template(), {'form': self.form})

    def get_service(self):
        return TimeTableService()

    def get_template(self):
        return 'timetablelist.html'