from django.shortcuts import render, redirect

from .base_ctl import BaseCtl
from ..models import Subject
from ..service.subject_service import SubjectService
from ..utility.data_validator import DataValidator


class SubjectCtl(BaseCtl):

    def input_validation(self, request):
        input_error = self.form.get("input_error")
        input_error['error'] = False

        if (DataValidator.is_null(request.POST.get("name", ''))):
            input_error['name'] = 'Name is required'
            input_error['error'] = True
        if (DataValidator.is_null(request.POST.get("description", ''))):
            input_error['description'] = 'Description is required'
            input_error['error'] = True
        if (DataValidator.is_null(request.POST.get("courseId", ''))):
            input_error['course_id'] = 'Course Id is required'
            input_error['error'] = True
        if (DataValidator.is_null(request.POST.get("courseName", ''))):
            input_error['course_name'] = 'Course Name is required'
            input_error['error'] = True
        return input_error['error']


    def request_to_form(self, request):
        self.form['id'] = int(request.POST.get('id', 0))
        self.form['name'] = request.POST.get('name')
        self.form['description'] = request.POST.get('description')
        self.form['course_id'] = request.POST.get('courseId')
        self.form['course_name'] = request.POST.get('courseName')

    def form_to_model(self, obj):
        obj.id = self.form['id']
        obj.name = self.form['name']
        obj.description = self.form['description']
        obj.course_id = self.form['course_id']
        obj.course_name = self.form['course_name']
        return obj

    def model_to_form(self, obj):
        self.form['id'] = obj.id
        self.form['name'] = obj.name
        self.form['description'] = obj.description
        self.form['course_id'] = obj.course_id
        self.form['course_name'] = obj.course_name

    def display(self, request, params={}):
        return render(request, self.get_template(), {'form': self.form})

    def submit(self, request, params={}):
        try:
            subject = self.form_to_model(Subject())
            self.get_service().save(subject)
            if self.form['id'] > 0:
                self.form['message'] = 'Subject Updated Successfully...!!!'
            else:
                self.form['message'] = 'Subject Added Successfully...!!!'
        except Exception as e:
            self.form['message'] = str(e)
            self.form['error'] = True
        return render(request, self.get_template(), {'form': self.form})

    def get_service(self):
        return SubjectService()

    def get_template(self):
        return 'subject.html'