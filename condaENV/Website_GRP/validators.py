from django.core.exceptions import ValidationError


def validate_image_size(value):
    filesize = value.size
    sizelimit = 10485760                # size limit here in bytes. 1 KB = 1024 Bytes; 1 MB = 1024 KB
    limit2human = sizelimit/1048576     # translate the weird number to human-readable MB

    if filesize > sizelimit:         # for testing purpose limit is 10 MB. 10MB = 10485760 bytes // 100 MB = 1048576000
        raise ValidationError("The maximum file size is " + str(limit2human) + "MB")
    else:
        return value
