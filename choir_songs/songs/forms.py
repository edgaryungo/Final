from django.forms import ModelForm 
from .models import Song, Album

class SongForm(ModelForm):
    class Meta:
        model = Song
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            new_css = {
                'class': 'form-control'
            }
            self.fields[str(field)].widget.attrs.update(
                new_css
            )
        self.fields['name'].widget.attrs.update({'placeholder':'Song name'})
        self.fields['body'].widget.attrs.update({'placeholder':'Song body'})

class AlbumForm(ModelForm):
    class Meta:
        model = Album
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            new_css = {
            'class': 'form-control'
            }
            self.fields[str(field)].widget.attrs.update(
                new_css
            )
        
        self.fields['name'].widget.attrs.update({'placeholder':'Album name'})