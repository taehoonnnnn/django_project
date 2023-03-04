
from django.http import HttpResponseForbidden

from commentapp.models import Comment

def comment_ownership_required(func):
    def decorated(request, *args, **kwargs):
        comment = Comment.objects.get(pk=kwargs['pk'])

        print('닉네임',comment.writer, request.user)
        print(comment)

        if not comment.writer == request.user:
            return HttpResponseForbidden()
        return func(request, *args, **kwargs)

    return decorated