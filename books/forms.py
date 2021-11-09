from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import Book, User

class UserCreationForum(UserCreationForm):

    class Meta:
        model = User
        fields = ('username','email')

class UserChangeForm(UserChangeForm):

    class Meta:
        model = User
        fields = ('username', 'email')

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ["title", "author"]
