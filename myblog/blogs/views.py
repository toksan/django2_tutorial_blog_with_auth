from django.urls import reverse, reverse_lazy
from django.http import HttpResponse
from django.views import generic
from django.shortcuts import redirect
from django.core.exceptions import PermissionDenied
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from .models import Post

"""
Django Auth

The LoginRequired mixin
https://docs.djangoproject.com/en/2.0/topics/auth/default/#the-loginrequired-mixin

The login_required decorator
https://docs.djangoproject.com/en/2.0/topics/auth/default/#the-login-required-decorator
@login_required
"""


class IndexView(generic.ListView):
    model = Post
    paginate_by = 5
    ordering = ['-updated_at']
    # template_name = 'blogs/post_list.html'


class DetailView(generic.DetailView):
    model = Post
    # template_name = 'blogs/post_confirm_delete.html'


class CreateView(LoginRequiredMixin, generic.edit.CreateView):  # The LoginRequired mixin
    model = Post
    fields = ['title', 'text']  # '__all__'

    # template_name = 'blogs/post_form.html'

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        # https://docs.djangoproject.com/en/2.0/topics/class-based-views/generic-editing/#models-and-request-user
        form.instance.author = self.request.user
        return super(CreateView, self).form_valid(form)


class UpdateView(LoginRequiredMixin, generic.edit.UpdateView):  # The LoginRequired mixin
    model = Post
    fields = ['title', 'text']  # '__all__'

    # template_name = 'blogs/post_form.html'

    def dispatch(self, request, *args, **kwargs):
        # ownership validation
        obj = self.get_object()
        if obj.author != self.request.user:
            raise PermissionDenied('You do not have permission to edit.')

        return super(UpdateView, self).dispatch(request, *args, **kwargs)


class DeleteView(LoginRequiredMixin, generic.edit.DeleteView):  # The LoginRequired mixin
    model = Post
    success_url = reverse_lazy('blogs:index')

    # blogs/post_confirm_delete.html

    def dispatch(self, request, *args, **kwargs):
        # ownership validation
        obj = self.get_object()
        if obj.author != self.request.user:
            raise PermissionDenied('You do not have permission to delete.')

        return super(DeleteView, self).dispatch(request, *args, **kwargs)


@login_required
def help(request):
    return HttpResponse("Member Only Help Page")
