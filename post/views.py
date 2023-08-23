from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, ListView

from comment.forms import CommentForm
from post.form import PostModelForm
from post.models import Post


class IndexView(ListView):
    model = Post
    template_name = "post/index.html"


class AddPost(CreateView):
    form_class = PostModelForm
    template_name = "post/add_post.html"
    success_url = reverse_lazy("post:index")

    def post(self, request, *args, **kwargs):
        form = PostModelForm(self.request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect("post:index")
        else:
            errors = form.errors
            print(errors)
            return render(request, "post/add_post.html", locals())


class PostDetail(DetailView):
    model = Post
    template_name = "post/post_detail.html"

    def get_object(self, queryset=None):
        obj = super().get_object(queryset=queryset)
        obj.increase_views()
        self.object = obj
        return self.object

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        comment_form = CommentForm()
        context["comment_form"] = comment_form
        comments = self.object.band_object.all()
        context["comments"] = comments
        return context


def user_thumb_up(request):
    object_pk = request.GET.get("object_pk")
    post = Post.objects.get(id=object_pk)
    total_thumb_up = post.thumb_up+1
    post.increase_thumb_up()
    return HttpResponse(total_thumb_up)


def user_thumb_down(request):
    object_pk = request.GET.get("object_pk")
    post = Post.objects.get(id=object_pk)
    total_thumb_down = post.thumb_down+1
    post.increase_thumb_down()
    return HttpResponse(total_thumb_down)