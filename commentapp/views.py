from django.shortcuts import render
from django.urls import reverse
# Create your views here.
from django.views.generic import CreateView
from articleapp.models import Article
from commentapp.models import Comment
from commentapp.froms import CommentCreationForm

class CommentCreateView(CreateView):
    model = Comment
    form_class = CommentCreationForm
    template_name = 'commentapp/create.html'

    def form_valid(self, form):
        temp_comment = form.save(commit=False)
        temp_comment.article = Article.objects.get(pk=self.request.POST['article_pk'])
        temp_comment.writer = self.request.user
        temp_comment.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('articleapp:detail', kwargs={'pk':self.object.article.pk})
    