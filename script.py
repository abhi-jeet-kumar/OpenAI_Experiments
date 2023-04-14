import configparser
import logging
import os
import openai


log = logging.getLogger(__name__)
log.setLevel(logging.DEBUG)
log.addHandler(logging.StreamHandler())
log.__format__ = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'

try:
    # Read config.cfg file
    config = configparser.ConfigParser()
    config.read('config.cfg', encoding='utf-8')
    api_key = config.get('OPEN API', 'OPEN_API_SECRET_KEY')
    openai.api_key = api_key
    log.debug(openai.Model.list())
except Exception as e:
    log.error('Config file not loaded')
    log.error(e)
    