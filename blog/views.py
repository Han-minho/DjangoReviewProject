from django.shortcuts import render, get_object_or_404, redirect
from blog.models import Post, Comment
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.views.generic import ListView
from blog.forms import EmailPostForm, CommentForm
from django.core.mail import send_mail
from django.views.decorators.http import require_POST


# Create your views here.
def post_list(request):
    post_list = Post.published.all()
    # 페이지 당 3개의 게시물로 페이지네이션
    paginator = Paginator(post_list, 3)
    page_number = request.GET.get('page')
    try:
        posts = paginator.page(page_number)
    except PageNotAnInteger:
        # page_number가 정수가 아닌 경우 첫번째 페이지 제공
        posts = paginator.page(1)
    except EmptyPage:
        # page_number가 범위를 벗어난 경우 결과의 마지막 페이지 제공
        posts = paginator.page(paginator.num_pages)
    return render(request, 'blog/post/list.html',
                  {'posts': posts})


def post_detail(request, year, month, day, post):
    # try:
    #     post = Post.published.get(id=id)
    # except Post.DoesNotExist:
    #     raise Http404("No Post found.")
    post = get_object_or_404(Post,
                             status=Post.Status.PUBLISHED,
                             slug=post,
                             publish__year=year,
                             publish__month=month,
                             publish__day=day)
    # List of active comments for this post
    comments = post.comments.filter(active=True)
    # Form for users to comment
    form = CommentForm()
    return render(request,
                  'blog/post/detail.html',
                  {'post': post,
                   'comments': comments,
                   'form': form})


class PostListview(ListView):
    queryset = Post.published.all()
    context_object_name = 'posts'
    paginate_by = 3
    template_name = 'blog/post/list.html'


def post_share(request, post_id):
    post = get_object_or_404(Post, id=post_id, status=Post.Status.PUBLISHED)
    sent = False
    if request.method == 'POST':
        form = EmailPostForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            post_url = request.build_absolute_uri(post.get_absolute_url())
            subject = f"{cd['name']} 님이 {post.title}을(를) 추천합니다."
            message = f"{post.title}을(를) {post_url} 에서 읽어보세요.\n\n" \
                      f"{cd['name']}의 의견: {cd['comments']}"
            send_mail(subject, message, 'hihi6024@gmail.com', [cd['to']])
            sent = True
    else:
        form = EmailPostForm()
    return render(request, 'blog/post/share.html', {'post': post,
                                                    'form': form,
                                                    'sent': sent})


@require_POST
def post_comment(request, post_id):
    post = get_object_or_404(Post, id=post_id, status=Post.Status.PUBLISHED)
    comment = None
    # A comment was posted
    form = CommentForm(data=request.POST)
    if form.is_valid():
        # Create a Comment object without saving it to database
        comment = form.save(commit=False)
        # Assign the post to the comment
        comment.post = post
        # Save the comment to the database
        comment.save()
    return render(request,
                  'blog/post/comment.html',
                  {'post': post,
                   'form': form,
                   'comment': comment})
