from django.forms import ModelForm

from techtips.tips.models import Tip


class TipForm(ModelForm):
    """This form is used by site visitors to submit tips
    """
    class Meta:
        model = Tip
        fields = ('title', 'content_markdown')
    
    def clean_title(self):
        # TODO: Populate slug 
        # TODO: Validate slug unique
        pass
    