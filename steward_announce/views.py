""" Endpoints """
from pyramid.view import view_config

from .models import Announcement


@view_config(route_name='announce', permission='announce')
def announce(request):
    """ Add an announcement """
    text = request.param('text')
    data = request.param('color', {}, type=dict)
    announcement = Announcement(text, **data)
    request.db.add(announcement)
    pub_data = dict(data)
    pub_data['text'] = text
    request.subreq('pub', name='announce', data=pub_data)
    return request.response

@view_config(route_name='announce_list', renderer='json')
def list(request):
    """ List all announcements """
    return request.db.query(Announcement).all()

@view_config(route_name='announce_clear', permission='announce')
def clear(request):
    """ Clear all announcements """
    request.db.query(Announcement).delete()
    return request.response

@view_config(route_name='announce_delete', permission='announce')
def delete(request):
    """ Delete a specific announcement """
    aid = request.param('id')
    request.db.query(Announcement).filter_by(id=aid).delete()
    return request.response
