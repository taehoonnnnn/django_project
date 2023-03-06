from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views.generic import RedirectView
from django.utils.decorators import method_decorator

from projectapp.models import Project
from subscribeapp.models import Subscription


# Create your views here.

@method_decorator(login_required, 'get')
class SubscriptionView(RedirectView):

    def get_redirect_url(self, *args, **kwargs):
        return reverse('projectapp:detail', kwargs={'pk': self.request.GET.get('project_pk')})

    def get(self, request, *args, **kwargs):
        project = get_object_or_404(Project, pk=self.request.GET.get('project_pk'))
        user = self.request.user
        subscription = Subscription.objects.filter(user=user, project=project)

        if subscription.exists():
            subscription.delete()
        else:
            Subscription(user=user, project=project).save()
        return super(SubscriptionView, self).get(request, *args, **kwargs)