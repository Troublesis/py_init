from dynaconf import Dynaconf

settings = Dynaconf(
    envvar_prefix=False,
    load_dotenv=True,
    root_path="src/config",
    settings_files=["settings.toml", "secrets.toml"],
    environments=True,
)

# `envvar_prefix` = export envvars with `export DYNACONF_FOO=bar`.
# `settings_files` = Load these files in the order.


if __name__ == "__main__":
    # https://dynaconf.readthedocs.io/en/docs_223/guides/accessing_values.html
    print(type(settings.get(("a_dict"))))
    print(settings.as_bool("a_boolean"))
    print(settings.as_json("a_dict"))

    print(settings.get("b_dict"))
    print(settings.get("number"))
    # print(settings.from_env("production").get_fresh("number"))
    # print(settings.get("number", fresh=True))
    print(settings.get(["mysql"][0], fresh=True))

    # export ENV_FOR_DYNACONF=production
    # print(settings.from_env("default").number)
