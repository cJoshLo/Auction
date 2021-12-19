from django.forms import ModelForm
from .models import *

class ListingForm(ModelForm):
    class Meta:
        model = Items
        fields = ['title', 'description', 'image' , 'startingBid']

class CommentForm(ModelForm):
    class Meta:
        model = Comments
        fields = ['comment']

class BidForm(ModelForm):
    class Meta:
        model = Bid
        fields = ['offer']

# class newListingForm(ModelForm):
#     class Meta:
#         model = ListingForm
#         fields = ['title', 'description', 'startingBid']

# class newPictureForm(ModelForm):
#     class Meta:
#         model = Picture
#         fields = ['picture', 'alt_text']

# class newBidForm(ModelForm):
#     class Meta:
#         model = Bid
#         fields = ['offer']

# class newCommentForm(ModelForm):
#     class Meta:
#         model = Comments
#         fields = ['comment']
        # widgets = {
        #     'comment': forms.TextInput(attrs={
        #         'class': 'form-control',
        #         'placeholder': 'Leave your comment here'
        #     })
        # }