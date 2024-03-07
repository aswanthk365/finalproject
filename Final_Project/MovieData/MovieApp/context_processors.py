from .models import Category

def categ_context(request):
    catetgory_liinks = Category.objects.all()
    return dict(catetgory_liinks=catetgory_liinks)