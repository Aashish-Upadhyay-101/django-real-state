from rest_framework.exceptions import APIException


class ProfileNotFound(APIException):
    status_code = 404
    default_detail = "Requested profile doesn't exists"


class NotYourProfile(APIException):
    status_code = 403
    default_detail = "You can't edit others profile"

    