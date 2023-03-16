from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse

from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from .models import Course
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin, PermissionRequiredMixin
from users.models import Teacher_Profile

class CourseCreateView(LoginRequiredMixin, CreateView):
    model = Course
    template_name = 'educational/course_create.html'
    fields = ['title', 'groups', 'description']

    def dispatch(self, request):
        if not request.user.is_authenticated:
            return HttpResponse(status=400)
        if not request.user.groups.all().first().name == 'Teachers':
            return HttpResponse(status=400)
        else:
            return super(CourseCreateView, self).dispatch(request)

    def form_valid(self, form):
        # проверка (до перехода по url)
        form.instance.author = Teacher_Profile.objects.filter(user=self.request.user).first()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('main')

def get_course(request, id):
    if Course.objects.filter(pk=id):
        return render(request, 'educational/course.html', {'course': Course.objects.filter(pk=id).first()})
    else: return render(request, 'base_app/error.html', {'error': 'Такого курса нет!'})

