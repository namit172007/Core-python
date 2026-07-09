from django.http import HttpResponse


def test_sos(request):
    return HttpResponse("<h1>Hello Th is is Django Project</h1>")
