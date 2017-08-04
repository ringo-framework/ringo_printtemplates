# This file offers a mimetype detection based on python-magic.
# There are two packages with that name (pypi- oriented version and
# linux-distributed versions). Two syntax versions need to be covered here.
import magic

def check_mime_type_from_buffer(data):
    try:
        magic_ = magic.open(magic.MAGIC_MIME_TYPE)
        magic_.load()
    except AttributeError:
        return magic.from_buffer(data, mime=True)
    return magic_.buffer(data)


def check_mime_type_from_file(data):
    try:
        magic_ = magic.open(magic.MAGIC_MIME_TYPE)
        magic_.load()
    except AttributeError:
        return magic.from_file(data, mime=True)
    return magic_.file(data)

# Validator for formbar
def odt_validator(field, data, form):
    v_data = data[field]
    if not v_data:
        if form._item.id is not None:
            # this is an update of an existing template entry, which does not
            # require a new file
            return True
        else:
            return False
    if check_mime_type_from_buffer(v_data) == "application/vnd.oasis.opendocument.text":
        return True

    return False
