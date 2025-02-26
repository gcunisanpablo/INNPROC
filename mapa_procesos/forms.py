from django import forms
from .models import VideoTutorial


class VideoTutorialForm(forms.ModelForm):
    class Meta:
        model = VideoTutorial
        fields = ["title", "icon_class", "video_id"]
