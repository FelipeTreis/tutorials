from django.shortcuts import get_object_or_404, render

from app.models import Content


def home(request):
    data = Content.objects.filter(is_published=True).order_by('id')

    return render(request, 'app/pages/home.html', context={'contents': data})


def content(request, id):
    data = get_object_or_404(Content, is_published=True, pk=id)

    return render(request, 'app/pages/content_view.html', context={'content': data, 'is_detail_view': True})
