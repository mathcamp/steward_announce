""" Storage interfaces for the announcements """

class IStorage(object):
    """
    Storage interface for announcements

    Provides an abstraction layer on top of whatever storage backend is
    available

    """
    def __init__(self, request):
        self.request = request

    def add(self, text, **kw):
        """
        Save an announcement

        Parameters
        ----------
        text : str
            The text of the announcement
        kw : dict
            Any additional parameters for the announcement

        """
        raise NotImplementedError

    def delete(self, aid):
        """
        Delete an announcement

        Parameters
        ----------
        aid : str
            The id of the announcement to delete

        """
        raise NotImplementedError

    def list(self):
        """ Get all announcements """
        raise NotImplementedError

    def clear(self):
        """ Delete all announcements """
        raise NotImplementedError

class IDictStorage(IStorage):
    """ Mixin for storage classes backed by a dict-like structure """
    @property
    def db(self):
        """ Access the underlying db dict """
        raise NotImplementedError

    def add(self, text, **kw):
        aid = 1
        while aid in self.db:
            aid += 1
        kw['text'] = text
        self.db[aid] = kw

    def delete(self, aid):
        del self.db[aid]

    def list(self):
        announcements = []
        for aid, data in self.db.iteritems():
            data['id'] = aid
            announcements.append(data)
        return announcements

    def clear(self):
        self.db.clear()

class SqliteDictStorage(IDictStorage):
    """ Storage interface that uses steward_sqlitedict """
    @property
    def db(self):
        return self.request.sqld('announce')

class MemoryStorage(IDictStorage):
    """ Transient storage interface that just uses memory """
    @property
    def db(self):
        if not hasattr(self.request.registry, 'announce_db'):
            self.request.registry.announce_db = {}
        return self.request.registry.announce_db
