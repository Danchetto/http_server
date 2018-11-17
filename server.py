#!/usr/bin/env python
from core.ServerController import ServerController
from utils.ConfigParser import load_config

if __name__ == '__main__':
    config = load_config()
    server = ServerController(config['listen'], config['thread_limit'], config['document_root'])
    server.run()
