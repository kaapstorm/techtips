from django.forms import ModelForm

from techtips.tips.models import Tip


class TipForm(ModelForm):
    # TODO: Populate slug on validate
    # TODO: Validate slug unique
    class Meta:
        model = Tip
        exclude = ('is_published', 'slug')
