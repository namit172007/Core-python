from django.http import HttpResponse


def sos_test(request):
    return HttpResponse('<h1>SOS Project Test</h1>')
