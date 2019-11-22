from guillotina import testing


def settings_configurator(settings):
    settings.setdefault("applications", [])
    if "simpleserver" not in settings:
        settings["applications"].append("simpleserver")


testing.configure_with(settings_configurator)
