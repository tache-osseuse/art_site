from django.shortcuts import render, redirect
from django.urls import reverse
from . models import Course_Announce
from educational_app.models import Course
from .forms import ClassAnnounceForm
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin, PermissionRequiredMixin
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from users.decorators import check_profile_activation

@login_required(login_url='/login/')
@check_profile_activation
def announces(request):
    if hasattr(request.user, 'student_profile'):
        group = request.user.student_profile.group
        context = { 'announces': Course_Announce.objects.filter(course__in=Course.objects.filter(groups=group).all()).order_by('-publish_date') }
    elif hasattr(request.user, 'teacher_profile'):
        context = { 'announces': Course_Announce.objects.filter(course__in=Course.objects.filter(author=request.user.teacher_profile).all()).order_by('-publish_date') }
    elif hasattr(request.user, 'admin_profile'):
        announces = Course_Announce.objects.all().order_by('-publish_date')
        context = { 'announces': announces }
    return render(request, 'informing/announces.html', context)

def delete_announce(request, id):
    announce = Course_Announce.objects.get(pk=id)
    if request.method == 'POST':
        announce.delete()
        return redirect('main')
    context = { 'item': announce , 'name': 'объявление' }
    return render(request, 'informing/announce_delete.html', context)

class CourseAnnounceCreateView(LoginRequiredMixin, CreateView):
    form_class = ClassAnnounceForm
    template_name = 'informing/announce_create.html'

    def get_success_url(self):
        return reverse('announces')

    def dispatch(self, request):
        if not request.user.is_authenticated:
            return HttpResponse(status=400)
        if not hasattr(request.user, 'teacher_profile'):
            return HttpResponse(status=400)
        else:
            return super(CourseAnnounceCreateView, self).dispatch(request)

    def get_form_kwargs(self):
        kwargs = super(CourseAnnounceCreateView, self).get_form_kwargs()
        kwargs.update({'user': self.request.user})
        return kwargs

    def form_valid(self, form):
        form.instance.author = self.request.user.teacher_profile
        return super().form_valid(form)