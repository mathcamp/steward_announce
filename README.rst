Steward Announce
================
This is a Steward extension for posting announcements. When people connect to
Steward, they will see the announcements.

Setup
=====
Steward_announce depends on steward_sqlalchemy. To use steward_announce, just
add it to your includes either programmatically::

    config.include('pyramid_tm')
    config.include('steward_sqlalchemy')
    config.include('steward_announce')

or in the config.ini file::

    pyramid.includes = 
        pyramid_tm
        steward_sqlalchemy
        steward_announce

Make sure you include it in the client config file as well.

Usage
=====
After inclusion, the client will have a few commands that begin with
'announce'. These will allow you to create and delete announcements.

Permissions
===========
::

    # This permission is required to create or delete announcements
    announce.perm.announce = group1 group2
