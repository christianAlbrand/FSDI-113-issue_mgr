from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
)

from .models import Issue, Status
from django.urls import reverse_lazy
from django.contrib.auth.mixins import (
    LoginRequiredMixin,
    UserPassesTestMixin
)

class IssueListView(LoginRequiredMixin, ListView):
    template_name = "issues/list.html"
    model = Issue

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        team_name = self.request.user.team.name
        published = Status.objects.get(name="Done")
        context["title"] = "Done"
        context["issue_list"] = (
            Issue.objects
            .filter(
                status=published,
                reporter__team__name =team_name
                )
            .order_by("created_on").reverse()
        )
        return context

class IssueDetailView(UserPassesTestMixin, DetailView):
    template_name = "issues/detail.html"
    model = Issue

    def test_func(self):
        issue = self.get_object()
        if issue.status.name == "Done":
            return True
        elif issue.status.name == "In Progress":
            if (self.request.user.is_authenticated
                    and self.request.user == issue.reporter):
                return True
        elif (issue.status.name == "To Do"
                and self.request.user.is_authenticated):
            return True
        else:
            return False

class IssueCreateView(UserPassesTestMixin, LoginRequiredMixin, CreateView):
    template_name = "issues/new.html"
    model = Issue
    fields = ["name", "summary", "description", "reporter", "assignee", "status", "priority_level"]

    def form_valid(self, form):
        form.instance.reporter = self.request.user
        return super().form_valid(form)
    
    def test_func(self):
        if self.request.user.role.name == "product owner":
            return True
        else:
            return False

class IssueUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    template_name = "issues/edit.html"
    model = Issue
    fields = ["name", "summary", "description", "reporter", "assignee", "status", "priority_level"]
    
    def test_func(self):
        if self.request.user.role.name == "developer":
            return True
        else:
            return False
        
class IncompleteIssueView(LoginRequiredMixin, ListView):
    template_name = "issues/incompleteIssues.html"
    model = Issue

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        team_name = self.request.user.team.name
        incomplete = Status.objects.filter(name__in=["To Do", "In Progress"])
        context["title"] = "Incomplete Issues"
        context["issue_list"] = (
            Issue.objects
            .filter(status__in=incomplete)
            .filter(
                status__in=incomplete,
                reporter__team__name =team_name
                )
            .order_by("created_on")
        )
        return context
# Create your views here.
