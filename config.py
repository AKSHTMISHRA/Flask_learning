import os

# Secret_ky is used for security reason

class Config(object):
    SECRET_KY = os.environ.get('SECRET_KY') or "secret_string"