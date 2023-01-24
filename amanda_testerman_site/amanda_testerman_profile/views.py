from django.shortcuts import render, redirect
from django.views import View
from .models import Comment, ContactInfo
from .forms import CommentForm, ContactForm

# Create your views here.
class HomeView(View):
    def get(self, request):

       comment = Comment.objects.all()
       comment_form = CommentForm()

       html_data = {
        'comments' : comment,
        'comment_form' : comment_form,
       }

       return render(
            request = request,
            template_name = 'index.html',
            context  = html_data,
        )    

    # def post(self, request, comment):

    #     if "add" in request.POST:
    #         comment_form = CommentForm(request.POST)
    #         comment_form.save()    