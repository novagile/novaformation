from datetime import datetime
from fabric.api import *

SSH_GITHUB_FINGERPRINT = "|1|qSj0QarP8KNPbgrsQCBD/5UAwMg=|zVVtpj1neIw6WR8MgjC6rTRaBcg= ssh-rsa AAAAB3NzaC1yc2EAAAABIwAAAQEAq2A7hRGmdnm9tUDbO9IDSwBK6TbQa+PXYPCPy6rbTrTtw7PHkccKrpp0yVhp5HdEIcKr6pLlVDBfOLX9QUsyCOV0wzfjIJNlGEYsdlLJizHhbn2mUjvSAHQqZETYP81eFzLQNnPHt4EVVUh7VfDESU84KezmD5QlWpXLmvU31/yMf+Se8xhHTvKSCZIFImWwoG6mbUoWf9nzpIoaSjB+weqqUUmpaaasXVal72J+UX2B+2RPW3RcT0eOzQgqlJL3RKrTJvdsjE3JEAvGq3lGHSZXy28G3skua2SmVi/w4yCE6gbODqnTWlg7+wC604ydGXA8VJiS5ap43JXiUFFAaQ=="


# Configuration
settings = {}


def prod():
    "Set variables for mirror server"
    env.host_string = "novagile@doc.novapost.fr"
    settings['doc_dir'] = '/home/novagile/www/formation-python'



def update():
    "update doc from git"
    with cd(settings['doc_dir']):
        run('git pull origin master')
        #run('make update')
        run('landslide config.cfg')