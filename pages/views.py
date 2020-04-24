from django.shortcuts import render
from django.views.generic import TemplateView, CreateView, ListView, DetailView
from .models import ContactRequest, Publications, Member, GroupInformation, ResearchField


class HomePageView(TemplateView):
    template_name = 'home.html'

    def group_information_list(self):
        return GroupInformation.objects.get(pk=1)


class PublicationsListPageView(ListView):
    model = Publications
    template_name = 'publications.html'

    def group_information_list(self):
        return GroupInformation.objects.get(pk=1)

    def paperslists(self):
        return Publications.objects.filter(
            publication_type='Paper').order_by('-year')

    def reviewslists(self):
        return Publications.objects.filter(
            publication_type='Review').order_by('-year')

    def chapterslists(self):
        return Publications.objects.filter(
            publication_type='Chapter').order_by('-year')

    def proceedingslists(self):
        return Publications.objects.filter(
            publication_type='Proceeding').order_by('-year')


class MembersPageView(TemplateView):
    template_name = 'members.html'

    def group_information_list(self):
        return GroupInformation.objects.get(pk=1)

    def currentmemberslist(self):
        return Member.objects.filter(
            final_year=0)

    def currentPI(self):
        return GroupInformation.objects.get(pk=1)

    def currentpostdocs(self):
        return Member.objects.filter(final_year=0, position='Postdoc')

    def currentphds(self):
        return Member.objects.filter(final_year=0, position='PhD')

    def currenttechnicians(self):
        return Member.objects.filter(final_year=0, position='Technician')

    def currentmasterstudents(self):
        return Member.objects.filter(final_year=0, position='MSc')

    def currentguestphdstudents(self):
        return Member.objects.filter(final_year=0, position='Guest_PhD')

    def currentgueststudents(self):
        return Member.objects.filter(final_year=0, position='Guest_Student')

    def previousmemberslist(self):
        return Member.objects.exclude(final_year=0).order_by('-initial_year')

    def previouspostdocs(self):
        return Member.objects.exclude(final_year=0).filter(position='Postdoc').order_by('-initial_year')

    def previousphds(self):
        return Member.objects.exclude(final_year=0).filter(position='PhD').order_by('-initial_year')

    def previoustechnicians(self):
        return Member.objects.exclude(final_year=0).filter(position='Technician').order_by('-initial_year')

    def previousmasterstudents(self):
        return Member.objects.exclude(final_year=0).filter(position='MSc').order_by('-initial_year')

    def previousguestphdstudents(self):
        return Member.objects.exclude(final_year=0).filter(position='Guest_PhD').order_by('-initial_year')

    def previousgueststudents(self):
        return Member.objects.exclude(final_year=0).filter(position='Guest_Student').order_by('-initial_year')


class MembersDetailView(DetailView):
    model = Member
    template_name = 'memberdetail.html'

    def group_information_list(self):
        return GroupInformation.objects.get(pk=1)


class ResearchPageView(ListView):
    model = ResearchField
    template_name = 'research.html'

    def group_information_list(self):
        return GroupInformation.objects.get(pk=1)


class ResearchFieldView(DetailView):
    model = ResearchField
    template_name = 'researchfield.html'

    def group_information_list(self):
        return GroupInformation.objects.get(pk=1)


class ContactPageView(CreateView):
    model = ContactRequest
    template_name = 'contact.html'
    fields = '__all__'

    def group_information_list(self):
        return GroupInformation.objects.get(pk=1)


class RequestReceivedPageView(TemplateView):
    template_name = 'request_received.html'

    def group_information_list(self):
        return GroupInformation.objects.get(pk=1)
