from django.core.paginator import EmptyPage, Paginator


def paginate_response(items, serializer, page_size, page_number) -> dict:
    """
    The objective with this method is return a default json to all GET paginated requests
    """
    # Validate and format inputs
    page_size = int(page_size or 50)
    page_number = int(page_number or 1)

    # Create paginator
    paginator = Paginator(items, page_size)
    try:
        objects = paginator.page(page_number)
        results = serializer(objects, many=True).data
    except EmptyPage:
        results = []

    # Mount return body
    body = {
        'total_count': paginator.count,
        'page_number': page_number,
        'page_size': page_size,
        'results': results
    }

    return body
