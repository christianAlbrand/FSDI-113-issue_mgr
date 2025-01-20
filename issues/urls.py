from django.urls import path
from issues import views

urlpatterns = [
    path("",views.IssueListView.as_view(), name="list"),
    path("<int:pk>/", views.IssueDetailView.as_view(), name="detail"),
    path("<int:pk>/edit/", views.IssueUpdateView.as_view(), name="edit"),
    path("incompleteIssues/", views.IncompleteIssueView.as_view(), name="incomplete"),
    path("new/",views.IssueCreateView.as_view(), name="new"),
]