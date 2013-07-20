""" Client commands """

def do_list(client):
    """ Format the response from announce.list """
    response = client.cmd('announce/list').json()
    lines = []
    for i, announcement in enumerate(response):
        lines.append("[{}] {}".format(i, announcement['text']))
    print '\n'.join(lines)

def do_announce(client, *words, **kwargs):
    """
    Create a new announcement

    Notes
    -----
    example::

        announce This is a very important announcements color=red

    """
    text = ' '.join(words)
    color = kwargs.pop('color', None)
    if kwargs:
        raise TypeError("Unrecognized keyword arguments %s" % kwargs)
    params = {'text': text}
    data = {}
    params['data'] = data
    if color:
        data['color'] = color
    client.cmd('announce', **params)

def do_clear(client):
    """ Clear all announcements """
    client.cmd('announce/clear')

def do_delete(client):
    """ Delete an announcement """
    announcements = client.cmd('announce/list').json()
    if not announcements:
        print "No announcements to delete"
        return
    do_list(client)
    index = -1
    while index < 0 or index >= len(announcements):
        try:
            index = int(raw_input('Delete id? '))
        except ValueError:
            pass
    client.cmd('announce/delete', id=announcements[index]['id'])
