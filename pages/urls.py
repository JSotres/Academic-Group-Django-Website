from django.urls import path
from .views import HomePageView, MembersPageView, ResearchPageView, ContactPageView, RequestReceivedPageView, PublicationsListPageView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('publications/', PublicationsListPageView.as_view(), name='publications'),
    path('members/', MembersPageView.as_view(), name='members'),
    path('research/', ResearchPageView.as_view(), name='research'),
    path('contact/', ContactPageView.as_view(), name='contact'),
    path('request_received/', RequestReceivedPageView.as_view(), name='contact_request_acknowledged'),
    ]
