import os


os.environ['DJANGO_SETTINGS_MODULE'] = 'website_nordic_walking.settings'


def create_dir(path):
    if not os.path.isdir(path):
        os.mkdir(path)
