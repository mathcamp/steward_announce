""" Client commands """

def do_list(client):
    """ Format the response from announce.list """
    response = client.cmd('announce/list').json()
    lines = []
    for announcement in response:
        lines.append("[{}] {}".format(announcement['id'], announcement['text']))
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
    data = {'text': text}
    if color:
        data['color'] = color
    client.cmd('announce', **data)

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
    ids = [a['id'] for a in announcements]
    aid = None
    while aid not in ids:
        if aid:
            print "Unrecognized id"
        aid = raw_input('Delete id? ')
    client.cmd('announce/delete', id=aid)

