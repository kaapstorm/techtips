# This file is part of Tech Tip of the Day.
# 
# Tech Tip of the Day is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# 
# Tech Tip of the Day is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with Tech Tip of the Day.  If not, see <http://www.gnu.org/licenses/>.

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
    