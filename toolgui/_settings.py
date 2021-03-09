import toolgui
import configparser

_UNSET = object()

def settings(name):
    """
    @settings(name)

    Decorator to serialize a class's static variables in the toolgui.ini file.
    """
    def dec(settings_class):
        @toolgui.on_app_quit()
        def save_settings():
            config = configparser.ConfigParser()
            config.read("toolgui.ini")
            if not config.has_section(name):
                config.add_section(name)
            for var in dir(settings_class):
                if not var.startswith("_"):
                    val = getattr(settings_class, var)
                    config.set(name, var, str(val))
            with open("toolgui.ini", 'w') as configfile:
                config.write(configfile)

        @toolgui.on_app_start()
        def load_settings():
            config = configparser.ConfigParser()
            config.read("toolgui.ini")
            if not config.has_section(name):
                config.add_section(name)
            for var in dir(settings_class):
                if not var.startswith("_"):
                    val = config.get(name, var, fallback=_UNSET)
                    if val is not _UNSET:
                        setattr(settings_class, var, val)
        return settings_class
    return dec