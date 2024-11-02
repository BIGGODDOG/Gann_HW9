from django.urls import path, re_path
from my_app.views import index, app_review, book_review, search_person

urlpatterns = [
    re_path(r'^index/.*$', index), 
    re_path(r'^app_review/.*$', app_review, name="app_review"),  
    re_path(r'^book_review/.*$', book_review, name="book_review"),  
    re_path(r'^search_person/.*$', search_person, name="search_person"),  
    # re_path(r"^.+$", index)
]