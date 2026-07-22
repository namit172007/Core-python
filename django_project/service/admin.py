from django.contrib import admin

# Register your models here.
from . models import User, Role, College,Course,Customer,Marksheet,Student, Subject, TimeTable

admin.site.register(Role)
admin.site.register(User)
admin.site.register(College)
admin.site.register(Course)
admin.site.register(Marksheet)
admin.site.register(Student)
admin.site.register(Subject)
admin.site.register(TimeTable)
admin.site.register(Customer)
