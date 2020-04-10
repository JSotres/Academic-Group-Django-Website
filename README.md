# Academic-Group-Django-Website

Django project for a typical academic where specific data of the academic group is manged entirely from the admin site and then delivered to the html templates.

I have used it to build my [group's website](http://www.jsotres.com) so you can make an idea of how it looks like.

## Introduction

Most websites of academic groups contain similar information e.g., research topics, publications, members. etc. This project aims at providing a template for an academic group website consisting on the following main pages:

1. Home
2. Projects
3. Publications
4. Members
5. Contact

All the specific information displayed in these html pages is delivered from a database (currently sqlite) consisting on the following models:

1. **Group Information**. Fields: PI_name, PI_position_ group_name_ group_def, group_short_description, group_long_description.
2. **ResearchField**. Fileds: topic, short_description, long_description, main_image.
3. **Publications**. Fields: authors, year, title, journal, volume, initialPage, publication_type.
4. **Member**. Fields: name, position, initial_year, final_year, mai_image, email.

All this info is entered through the admin page and delivery to the specific html templates.

Additionally, the web contains a form that a viewer can use to contact the academic group. Each entry would generate an instace of the above model of the database that then can be viewed in the admin page:

5. **ContactRequest**. Fields: title, text, contact_info

## Use

I will upload information on how to use (and deploy) the project as soon as I have time. Mean while, if you are intersted in using the code to build your own academic group website, just contact me.

## Contributors

[Javier Sotres](http://www.jsotres.com)
