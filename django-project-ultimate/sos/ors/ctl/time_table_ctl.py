from django.shortcuts import render, redirect

from .base_ctl import BaseCtl
from ..models import TimeTable
from ..service.role_service import RoleService
from ..service.time_table_service import TimeTableService
from ..service.course_service import CourseService
from ..service.college_service import CollegeService
from ..service.subject_service import SubjectService
from ..utility.data_validator import DataValidator
from ..utility.html_utility import HtmlUtility


class TimeTableCtl(BaseCtl):

    def preload(self, request):
        course_list = CourseService().search({})
        subject_list = SubjectService().search({})


        self.form["preload_data"]["course_select"] = HtmlUtility.get_list_from_beans(
            "courseId",
            int(self.form.get("course_id") or 0),
            course_list
        )

        self.form["preload_data"]["subject_select"] = HtmlUtility.get_list_from_beans(
            "subjectId",
            int(self.form.get("subject_id") or 0),
            subject_list
        )

    def input_validation(self, request):
        input_error = self.form.get("input_error")
        input_error['error'] = False

        if (DataValidator.is_null(self.form['exam_time'])):
            input_error['exam_time'] = 'Exam Time is required'
            input_error['error'] = True
        if (DataValidator.is_null(self.form['exam_date'])):
            input_error['exam_date'] = 'Exam date is required'
            input_error['error'] = True
        if (DataValidator.is_null(self.form['semester'])):
            input_error['semester'] = 'Semester is required'
            input_error['error'] = True

        if (DataValidator.is_null(self.form['course_id']) or request.POST.get("courseId") == "0"):
            input_error['course_id'] = 'Course is required'
            input_error['error'] = True

        if (DataValidator.is_null(self.form['subject_id']) or request.POST.get("subjectId") == "0"):
            input_error['subject_id'] = 'Subject is required'
            input_error['error'] = True
        return input_error['error']

    def request_to_form(self, request):
        self.form['id'] = int(request.POST.get('id', 0))
        self.form['exam_time'] = request.POST.get('examTime', '')
        self.form['exam_date'] = request.POST.get('examDate', '')
        self.form['semester'] = request.POST.get('semester', '')
        self.form['course_id'] = request.POST.get('courseId', 0)
        self.form['subject_id'] = request.POST.get('subjectId', 0)

    def form_to_model(self, obj):
        obj.id = self.form['id']
        obj.exam_time = self.form['exam_time']
        obj.exam_date = self.form['exam_date']
        obj.semester = self.form['semester']
        obj.course_id = int(self.form['course_id'])
        obj.course_name = CourseService().get(self.form['course_id']).name
        obj.subject_id = int(self.form['subject_id'])
        obj.subject_name = SubjectService().get(self.form['subject_id']).name
        return obj

    def model_to_form(self, obj):
        self.form['id'] = obj.id
        self.form['exam_time'] = obj.exam_time
        self.form['exam_date'] = obj.exam_date
        self.form['semester'] = obj.semester
        self.form['course_id'] = obj.course_id
        self.form['course_name'] = obj.course_name
        self.form['subject_id'] = obj.subject_id
        self.form['subject_name'] = obj.subject_name

    def display(self, request, params={}):
        return render(request, self.get_template(), {'form': self.form,  "preload_data": self.preload(request)})

    def submit(self, request, params={}):
        try:
            time_table = self.form_to_model(TimeTable())
            self.get_service().save(time_table)
            if self.form['id'] > 0:
                self.form['message'] = 'TimeTable Updated Successfully...!!!'
            else:
                self.form['message'] = 'TimeTable Added Successfully...!!!'
        except Exception as e:
            self.form['message'] = str(e)
            self.form['error'] = True
        return render(request, self.get_template(), {'form': self.form,  "preload_data": self.preload(request)})

    def get_service(self):
        return TimeTableService()

    def get_template(self):
        return 'timetable.html'