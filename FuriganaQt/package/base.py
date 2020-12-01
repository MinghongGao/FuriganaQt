import os
from FuriganaQt.package.config import Config
from FuriganaQt.package import constants
import toml


def override_using_user_defined_config(config):
    print(os.getcwd())
    with open(constants.CONFIG_FILE, 'r') as config_file:
        data = toml.load(config_file)
        for attr in data:
            config.__setattr__(attr, data[attr])


def create_config():
    config = Config()
    config.def_field('VERSION', type_=str, default='0.0.1')
    override_using_user_defined_config(config)
    return config
