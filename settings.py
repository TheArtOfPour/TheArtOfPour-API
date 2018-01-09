from eve_sqlalchemy.config import DomainConfig, ResourceConfig
from simple.tables import Yeast, Hops, Fermentables, Styles
import os

file_path = os.path.abspath(os.path.join(os.getcwd(), os.pardir))
DEBUG = True
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + file_path + '\\db\\training.db'
SQLALCHEMY_TRACK_MODIFICATIONS = False
RESOURCE_METHODS = ['GET', 'POST']

# CORS disabled
X_DOMAINS = '*'

PAGINATION = False

# @todo : add authentication

# The following two lines will output the SQL statements executed by
# SQLAlchemy. This is useful while debugging and in development, but is turned
# off by default.
# --------
# SQLALCHEMY_ECHO = True
# SQLALCHEMY_RECORD_QUERIES = True

# The default schema is generated using DomainConfig:
DOMAIN = DomainConfig({
    'styles': ResourceConfig(Styles),
    'yeast': ResourceConfig(Yeast),
    'hops': ResourceConfig(Hops),
    'fermentables': ResourceConfig(Fermentables),
}).render()

