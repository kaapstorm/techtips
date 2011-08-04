from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.mail import mail_managers
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import Context, loader, RequestContext
from django.views.generic import ListView, DetailView

from techtips.tips.forms import TipForm
from techtips.tips.models import Tip


class TipListView(ListView):
    context_object_name = 'tip'
    
    def get_queryset(self):
        if self.request.user.is_authenticated(): # TODO: and is_manager()
            return Tip.objects.all()
        return Tip.objects.filter(is_published=True)


class TipDetailView(DetailView):
    context_object_name = 'tip'
    
    # TODO: Is this the best way to do this? In __init__()?
    def __init__(self, *args, **kwargs):
        super(TipDetailView, self).__init__(*args, **kwargs)
        if self.type == 'ajax': 
            # Use AJAX template if instance was passed type='ajax'
            self.template_name = 'tips/tip_detail_ajax.html'
    
    def get_queryset(self):
        if self.request.user.is_authenticated(): # TODO: and is_manager()
            return Tip.objects.all()
        return Tip.objects.filter(is_published=True)


@login_required
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
            mail_managers('New submission', text_message, 
                          fail_silently=True, html_message=html_message)
            # Confirm submission
            messages.success(request, 'Thank you. Your tip has been submitted.')
            return HttpResponseRedirect('tip_list_view')
    else:
        form = TipForm()
    return render_to_response('tips/tip_add.html',
                              {'form': form},
                              context_instance=RequestContext(request))
