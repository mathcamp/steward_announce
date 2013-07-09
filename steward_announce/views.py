""" Endpoints """
from pyramid.httpexceptions import HTTPBadRequest
from pyramid.view import view_config
from steward import colors

@view_config(route_name='announce', permission='announce')
def announce(request):
    """ Add an announcement """
    text = request.param('text')
    color = request.param('color', None)
    if not hasattr(colors, color):
        raise HTTPBadRequest("%s is not a valid color!" % color)
    kw = {}
    if color is not None:
        kw ['color'] = color
    storage(request).add(text, **kw)
    data = dict(kw)
    data['text'] = text
    request.subreq('pub', name='announce', data=data)
    return request.response

@view_config(route_name='announce_list', renderer='json')
def list(request):
    """ List all announcements """
    return storage(request).list()

@view_config(route_name='announce_clear', permission='announce')
def clear(request):
    """
    Clear all announcements
    """
    storage(request).clear()
    return request.response

@view_config(route_name='announce_delete', permission='announce')
def delete(request):
    """ Delete a specific announcement """
    aid = request.param('id')
    storage(request).delete(aid)
    return request.response

def storage(request):
    """ Convenience method for accessing the storage object """
    return request.registry.announce_storage(request)
