""" Steward extension for sharing public announcements """
from steward import colors


def include_client(client):
    """ Add client commands """
    client.set_cmd('announce', 'steward_announce.client:do_announce')
    client.set_cmd('announce.clear', 'steward_announce.client:do_clear')
    client.set_cmd('announce.delete', 'steward_announce.client:do_delete')
    client.set_cmd('announce.list', 'steward_announce.client:do_list')

    # TODO
    #client.sub('announce')
    announcements = client.cmd('announce/list').json()
    for announcement in announcements:
        text = announcement['text']
        if announcement.get('color'):
            text = getattr(colors, announcement['color'])(text)
        print text


def includeme(config):
    """ Configure the app """
    config.add_route('announce', '/announce')
    config.add_route('announce_list', '/announce/list')
    config.add_route('announce_clear', '/announce/clear')
    config.add_route('announce_delete', '/announce/delete')

    config.scan()
