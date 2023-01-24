from django.forms import ModelForm


from amanda_testerman_profile.models import Comment, ContactInfo


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['comment']

class ContactForm(ModelForm):
    class Meta:
        model = ContactInfo
        fields = ['name', 'phone', 'email']