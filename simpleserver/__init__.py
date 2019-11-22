from guillotina import configure


def includeme(root, settings):
    configure.scan("simpleserver.api")
