from guillotina import testing


def settings_configurator(settings):
    settings.setdefault("applications", [])
    if "simpleapp" not in settings:
        settings["applications"].append("simpleapp")


testing.configure_with(settings_configurator)
