from django.shortcuts import render, redirect
from django.views import View
from .models import Comment, ContactInfo
from .forms import CommentForm, ContactForm
from django.contrib import messages

# Create your views here.
about_me_info = "My name is Amanda Testerman and I am a Software Engineer. I started my path in Web Development in a very non traditional and unique learning environment. I feel that the beginning learning experience gave me an edge not found in most Web Developers. I did not have internet access while learning Web Development fundamentals. Html, CSS, Bootstrap, and Javascript were all taught, learned, experimented with, and implemented without the use of resources that are available to the average SE. Since the beginning of my journey I have been fueling my desire and passion for this field with continued education and persistence. I have had the pleasure of and Web Development Education Apprenticeship where I learned many valuable skills that I will carry with me throughout my career in the professional workplace as well as in my coding journey."
skills = "I have become knowledgeable in HTML, CSS, Javascript, jQuery, Python, and Django. I have some experience with React. I have created a guided multi page website, put together a few home pages as class projects and am currently putting together my first multi page portfolio website for myself. I have collaborated on a team project to develop an app for parents and children to assign chores and keep track of allowances for finished chores. The app sets up children and assigns them chores for the days of the week, The children can see what chores are assif=gned to them and mark them complete as they are done. I have utilized javascript functions, python functions,object methods, django framework, displaying database information, I have created databases with appropriate models and forms, and in a few smaller class projects and have recently learned prototypical inheritance and am learning to implement it into personal projects. I have created simple game logic for an assignment and continue to create needed functions for class exercises."

class HomeView(View):
    def get(self, request):
        #grabbing all contacts and comments from data base and the the Forms to be able to use information to pass into HTML

       comments = Comment.objects.all()
       comment_form = CommentForm()
       contact = ContactInfo.objects.all()
       contact_form = ContactForm()
        #setting up context data for display in html
       html_data = {
        'comments' : comments,
        'comment_form' : comment_form,
        'contact_form' : contact_form,
        'contact': contact, 
        'about_me' : about_me_info,
        'skills' : skills
       }

       return render(
            request = request,
            template_name = 'index.html',
            context  = html_data,
        )    
 # github.com/sobrien-banyan/Imma-chore
    def post(self, request):
        #if the add button is clicked on the comment form
        if "add" in request.POST:
            #the comment information in the text feild will be saved to database
            comment_form = CommentForm(request.POST).save()
            return redirect('home')
            #if the create button is clicked on the contacts form
        elif "create" in request.POST:
            #the information from all feilds will be saved to the database
            contact_form = ContactForm(request.POST).save()
            #the feild "is_created" on the form will be set to True
            contact_form.is_created = True
            contact_form.save()
            #imported messages for alert message to let users know their information was saved succesfully
            messages.success(request, "I have recieved your contact info and will response as soon as possible. Thank you!" )
            return redirect('home')
