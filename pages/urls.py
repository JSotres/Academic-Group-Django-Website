from django.urls import path
from .views import HomePageView, MembersPageView, MembersDetailView, ResearchPageView, ContactPageView, RequestReceivedPageView, PublicationsListPageView, ResearchFieldView

urlpatterns = [
    path('', HomePageView.as_view(),
         name='home'),
    path('publications/', PublicationsListPageView.as_view(),
         name='publications'),
    path('members/', MembersPageView.as_view(),
         name='members'),
    path('members/<int:pk>/', MembersDetailView.as_view(),
         name='membersdetail'),
    path('research/', ResearchPageView.as_view(),
         name='research'),
    path('research/<int:pk>/', ResearchFieldView.as_view(),
         name='researchfield'),
    path('contact/', ContactPageView.as_view(),
         name='contact'),
    path('request_received/', RequestReceivedPageView.as_view(),
         name='contact_request_acknowledged'),
    ]
