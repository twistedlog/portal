
def get_upload_location(instance, filename):
    return u"%s/%s" % (instance.id, filename)
