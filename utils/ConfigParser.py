def load_config():
    try:
        f = open('httpd.conf')
    except IOError:
        raise Exception("Config file not found")
    config = {}

    lines = f.read().splitlines()
    for line in lines:
        key, value = line.split(" ")
        if key in ('listen', 'thread_limit', 'document_root'):
            config[key] = value
    f.close()
    return config
