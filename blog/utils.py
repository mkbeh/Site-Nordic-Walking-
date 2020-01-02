from django.core.paginator import Paginator


def get_pagination_page(request, objs, per_page=10):
    paginator = Paginator(objs, per_page)

    if 'page' in request.GET:
        page_num = request.GET['page']
    else:
        page_num = 1

    return paginator.get_page(page_num)
