from django.shortcuts import render
from django.http import HttpResponse
from django.http import Http404
from django.db.models import Prefetch

from guide.models import Exhibition, Artwork, Media, Category, Tour

def object_photos(request, collection):
    request.session['object-mode'] = 'photos';
    coll = Exhibition.objects.filter(slug=collection, is_live=True)
    if coll:
        media = Media.objects.filter(kind='image', position='0', artwork__exhibition=coll).order_by('artwork__title')
        #Split media into two arrays (one for each column)
        left = []
        right = []
        leftH = 0
        rightH = 0
        for m in media:
            if leftH <= rightH:
                left.append(m)
                leftH += (m.height / m.width)
            else:
                right.append(m)
                rightH += (m.height / m.width)

        mediaCol = {'left' : left, 'right' : right}
        context = {'c': coll.first(), 'media': mediaCol}
        return render(request, "objects/photos.html" , context)
    else:
        raise Http404("Not Found")

def object_list(request, collection):
    request.session['object-mode'] = 'list';
    coll = Exhibition.objects.filter(slug=collection, is_live=True)
    if coll:
        art = Artwork.objects.filter(exhibition=coll).order_by('title')
        context = {'c': coll.first(), 'art': art}
        return render(request, "objects/list.html" , context)
    else:
        raise Http404("Not Found")

def object_cats(request, collection):
        coll = Exhibition.objects.filter(slug=collection, is_live=True)
        if coll:
            cats = Category.objects.filter(artwork__exhibition=coll).distinct().order_by('title')
            context = {'c': coll.first(), 'cats': cats}
            return render(request, "objects/categories.html" , context)
        else:
            raise Http404("Not Found")

def object_category(request, collection, category):
    request.session['object-mode'] = 'category/' + category;
    coll = Exhibition.objects.filter(slug=collection, is_live=True)
    cat = Category.objects.filter(slug=category)
    if coll and cat:
        art = Artwork.objects.filter(exhibition=coll, category=cat)
        context = {'c': coll.first(), 'cat': cat.first(), 'art': art}
        return render(request, "objects/category.html" , context)
    else:
        raise Http404("Not Found")

def object(request, collection, object):
    if 'object-mode' not in request.session:
        back_url = 'photos'
    else:
        back_url = request.session['object-mode']
    coll = Exhibition.objects.filter(slug=collection, is_live=True)
    if coll:
        obj = Artwork.objects.filter(slug=object, exhibition=coll).first()
        objs = Artwork.objects.filter(exhibition=coll).order_by('title')
        media = get_object_media(obj)
        info = get_object_bar_info(objs, obj)
        context = {'c': coll.first(), 'object': obj, 'collect_info':info, 'media' : media, 'back': back_url}
        return render(request, "objects/object.html" , context)
    else:
        raise Http404("Not Found")

def object_w_category(request, collection, category, object):
    if 'object-mode' not in request.session:
        back_url = 'photos'
    else:
        back_url = request.session['object-mode']
    coll = Exhibition.objects.filter(slug=collection, is_live=True)
    cat =  Category.objects.filter(slug=category)
    if coll and cat:
        obj = Artwork.objects.filter(slug=object, exhibition=coll, category=cat).first()
        objs = Artwork.objects.filter(exhibition=coll, category=cat).order_by('title')
        media = get_object_media(obj)
        info = get_object_bar_info(objs, obj)
        context = {'c': coll.first(), 'object': obj, 'collect_info':info, 'back': back_url, 'media' : media, 'category': cat}
        return render(request, "objects/object.html" , context)
    else:
        raise Http404("Not Found")

def object_w_tour(request, collection, tour, object):
    if 'object-mode' not in request.session:
        back_url = 'photos'
    else:
        back_url = request.session['object-mode']
    coll = Exhibition.objects.filter(slug=collection, is_live=True)
    if coll:
        t =  Tour.objects.filter(slug=tour, exhibition=coll)
        if t:
            obj = Artwork.objects.filter(slug=object, exhibition=coll, tour=t).first()
            objs = Artwork.objects.filter(exhibition=coll, tour=t).order_by('tourartwork__position')
            media = get_object_media(obj)
            info = get_object_bar_info(objs, obj)
            context = {'c': coll.first(), 'object': obj, 'collect_info':info, 'media':media, 'back': back_url, 'tour': t.first()}
            return render(request, "objects/object.html" , context)

    raise Http404("Not Found")

def object_search(request, object):
    back_url = 'find'
    objs = Artwork.objects.filter(slug=object)
    if objs:
        obj = objs.first()
        media = get_object_media(obj)
        info = get_object_bar_info(objs, obj)
        context = {'object': obj, 'collect_info':info, 'media':media, 'back': back_url}
        return render(request, "objects/object.html" , context)

    raise Http404("Not Found")

def get_object_bar_info(obj_set, obj):
    indx = -1
    c = 0
    for a in obj_set:
        if a.uuid == obj.uuid:
            indx = c
            break
        c += 1

    if indx == -1:
        return None

    info = {}
    count = obj_set.count()
    info['count'] = count
    if indx > 0:
        info['prev'] = obj_set[indx-1]
    if indx < count - 1:
        info['next'] = obj_set[indx+1]

    indx += 1
    info['current'] = indx
    return info

def get_object_media(obj):
    photos = Media.objects.filter(kind='image', artwork=obj).order_by('position')
    audio = Media.objects.filter(kind='audio', artwork=obj).order_by('position')
    return {'images': photos, 'audio': audio}
