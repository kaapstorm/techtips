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

from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.core.mail import mail_managers
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import Context, loader, RequestContext
from django.views.decorators.csrf import csrf_protect
from django.views.generic import ListView, DetailView

from techtips.tips.forms import TipForm, UserChangeForm
from techtips.tips.models import Tip


class TipListView(ListView):
    context_object_name = 'tip_list'
    
    def get_queryset(self):
        """If the user is a member of the Moderators group, show all tips,
        otherwise just show published tips.
        """
        if self.request.user.is_authenticated() \
                and self.request.user.groups.filter(name='Moderators').count():
            return Tip.objects.all()
        return Tip.objects.filter(is_published=True)


class TipDetailView(DetailView):
    context_object_name = 'tip'
    
    def get_queryset(self):
        """Allow moderators to see unpublished tips.
        """
        if self.request.user.is_authenticated() \
                and self.request.user.groups.filter(name='Moderators').count():
            return Tip.objects.all()
        return Tip.objects.filter(is_published=True)


def register(request):
    """Uses standard register form
    """
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            user = auth.authenticate(username=request.POST['username'], 
                                     password=request.POST['password1'])
            auth.login(request, user)
            return HttpResponseRedirect(reverse('tip_list_view'))
    else:
        form = UserCreationForm()
    return render_to_response("registration/register.html", 
                              {'form': form},
                              context_instance=RequestContext(request))


def logout(request):
    """Logs out and redirects to the tip list.
    """
    auth.logout(request)
    return HttpResponseRedirect(reverse('tip_list_view'))


@login_required
@csrf_protect
def add_tip(request):
    """Submit a new tip.
    """
    if request.method == 'POST':
        form = TipForm(request.POST)
        if form.is_valid():
            # Save the submission
            tip = form.save(commit=False)
            tip.created_by = request.user
            tip.save()
            # Notify managers of new submission
            c = Context({'tip': tip})
            t = loader.get_template('tips/tip_email.txt')
            text_message = t.render(c)
            t = loader.get_template('tips/tip_email.html')
            html_message = t.render(c)
            mail_managers('New tip submission', text_message,
                          fail_silently=True, html_message=html_message)
            # Confirm submission
            messages.success(request, 
                             'Thank you. Your tip has been submitted.')
            return HttpResponseRedirect(reverse('tip_list_view'))
    else:
        form = TipForm()
    return render_to_response('tips/tip_add.html',
                              {'form': form},
                              context_instance=RequestContext(request))


@login_required
@csrf_protect
def edit_profile(request):
    if request.method == 'POST':
        form = UserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save(commit=False)
            return HttpResponseRedirect(reverse('tip_list_view'))
    else:
        form = UserChangeForm(instance=request.user)
    return render_to_response('registration/edit_profile.html',
                              {'form': form},
                              context_instance=RequestContext(request))
