from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from django.views import generic
from . import models


class TypeListView(generic.ListView):
    model = models.Type
    template_name= 'beer_stories/type_list.html'


class TypeDetailView(generic.DetailView):
    model = models.Type
    template_name = 'beer_stories/type_details.html'
    

class TypeCreateView(LoginRequiredMixin,generic.CreateView):
    model = models.Type
    template_name = 'beer_stories/type_create.html'
    fields = ('types', 'country_name', 'color', 'filtered')
    
    def get_success_url(self) -> str:
        messages.success(self.request, _('type created succesfully').capitalize())
        return reverse('type_list')
    
    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)


class TypetUpdateView(LoginRequiredMixin, UserPassesTestMixin, generic.UpdateView):
    model = models.Type
    template_name = 'beer_stories/type_update.html'
    field = ('types', 'country_name', 'color', 'filtered')


def index(request: HttpRequest) -> HttpResponse:
    context = {
        'types_count': models.Type.objects.count(),
        'reviews_count': models.Review.objects.count(),
        'users_count': models.get_user_model().objects.count(),
    }
    return render(request, 'beer_stories/index.html', context)

def review_list(request: HttpRequest) -> HttpResponse:
    return render(request, 'beer_stories/review_list.html', {
        'review_list': models.Review.objects.all(),
    })

def review_detail(request: HttpRequest, pk: int) ->HttpResponse:
    return render(request, 'beer_stories/review_detail.html', {
        'review': get_object_or_404(models.Review, pk=pk),
    } )