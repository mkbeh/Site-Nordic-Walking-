from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Q
from django.views.decorators.cache import cache_page

from .models import Post, Instructor
from .forms import SearchForm, CommentForm
from blog import utils


def search_posts(request, query):
    q_obj = Q(title__icontains=query) | Q(body__icontains=query)
    found_posts = Post.objects.filter(q_obj, status='published')[:10]

    return render(request, 'blog/search.html', {'query': query, 'found_posts': found_posts})


def search_form_actions(request):
    if 'query' in request.GET:
        form = SearchForm(request.GET)

        if form.is_valid():
            query = form.cleaned_data['query']
            return query


def index(request):
    posts = Post.published.all()[:3]
    form = SearchForm()
    query = search_form_actions(request)

    if query:
        return redirect('blog:search_posts', query=query)

    return render(request, 'blog/blog.html', {'posts': posts, 'form': form})


def post_detail(request, year, month, day, post):
    post = get_object_or_404(
        Post,
        slug=post,
        status='published',
        publish__year=year,
        publish__month=month,
        publish__day=day
    )

    comments = post.comments.filter(active=True)
    new_comment = None

    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)

        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.post = post
            new_comment.save()
    else:
        comment_form = CommentForm()

    return render(
        request,
        'blog/detail.html',
        {'post': post,
         'comments': comments,
         'new_comment': new_comment,
         'comment_form': comment_form}
    )


def about_event(request):
    page_objs = Post.published.all().order_by('-publish')
    page = utils.get_pagination_page(request, page_objs)

    form = SearchForm()
    query = search_form_actions(request)

    if query:
        return redirect('blog:search_posts', query=query)

    return render(request,
                  'blog/about_event.html',
                  {'page_objs': page.object_list, 'page': page, 'form': form})


@cache_page(15*60)
def instructors_list(request):
    instructors = Instructor.objects.all().order_by('-initials')
    page = utils.get_pagination_page(request, instructors)

    return render(request, 'blog/instructors_list.html', {'instructors': page.object_list, 'page': page})
