from django.shortcuts import render, get_object_or_404
from django.http import Http404, HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from django.utils import timezone

from .models import Post


class IndexView(generic.ListView):
    template_name = 'blog/index.html'
    context_object_name = 'latest_post_list'

    def get_queryset(self):
        """ Return last 5 post (not including those set for future) """
        return Post.objects.filter(published_date__lte=timezone.now()).order_by('-pub_date')[:5]
