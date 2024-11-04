from .protocol.common import API
from terminal_app.env import source
import os

api = source(".laba2.env")

if bool(int(api.get("FLASK_PROD", 0))):
    os.system(f"cd api/ && {api["GUNICORN"]}")
else:
    API.run(debug=True, port=int(api["GA_PORT"]), host=api["GA_HOST"])
