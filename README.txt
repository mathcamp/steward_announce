Steward Announce
================
This is a Steward extension for posting announcements. When people connect to
Steward, they will see the announcements.

Setup
=====
To use steward_announce, just add it to your includes either programmatically::

    config.include('steward_announce')

or in the config.ini file::

    pyramid.includes = steward_announce

Make sure you include it in the client config file as well.

Usage
=====
After inclusion, the client will have a few commands that begin with
'announce'. These will allow you to create and delete announcements.

Configuration
=============

* **announce.storage** - The backend to use for storing the announcements. Required.
    * memory - Store the announcements in memory (transient)
    * sqlitedict - Use steward_sqlitedict as the backend
    * <dotted_path> - You may provide a dotted path name to a class that implements ``steward_announce.storage.IStorage``

Permissions
===========
* **announce** - This permission is required to create or delete announcements
