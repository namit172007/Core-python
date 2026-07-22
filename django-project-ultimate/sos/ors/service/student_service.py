from django.db import connection

from ..models import Student
from ..utility.data_validator import DataValidator
from django.core.paginator import Paginator


class StudentService:

    def save(self, obj):
        print('student service orm save()')
        duplicate = self.find_by_login(obj.email)

        if obj.id > 0:
            duplicate = duplicate.exclude(id=obj.id)

        if duplicate.exists():
            raise Exception('Student already exist')

        if obj.id == 0:
            obj.id = None

        obj.save()

    def get(self, pk):
        print('student service orm get()')
        try:
            obj = Student.objects.get(id=pk)
            return obj
        except Student.DoesNotExist:
            return None

    def delete(self, id):
        print('student service orm delete()')
        obj = self.get(id)
        obj.delete()

    def find_by_login(self, email):
        print('student service orm find_by_login()')
        obj = Student.objects.filter(email=email)
        return obj

    def authenticate(self, email, mobile_number):
        print('student service orm authenticate()')
        query = Student.objects.all()

        query = query.filter(email=email.strip())
        query = query.filter(mobile_number=mobile_number.strip())

        if len(query) > 0:
            return query.first()
        else:
            return None

    def search(self, params):
        print('student service orm search()')

        page_no = int(params.get("page_no", 1))
        page_size = int(params.get('page_size', 0))

        query = Student.objects.all()

        value = params.get("first_name", '')
        if DataValidator.is_not_null(value):
            query = query.filter(first_name__istartswith=value.strip())

        if (page_size == 0):
            return query

        paginator = Paginator(query, page_size)

        page_obj = paginator.get_page(page_no)

        params["has_next"] = page_obj.has_next()
        params["has_previous"] = page_obj.has_previous()
        params["index"] = (page_no - 1) * page_size

        return page_obj