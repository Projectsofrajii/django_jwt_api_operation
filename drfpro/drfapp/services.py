import dataclasses
import datetime
from typing import TYPE_CHECKING
import jwt
from django.conf import settings
from .import models

if TYPE_CHECKING:
    from .models import RsmUserMaster

@dataclasses.dataclass
class UserDataClass:
    user_name: str
    mobile: int
    email_id: str
    password: str = None
    user_id: int = None

    @classmethod
    def from_instance(cls,user: "RsmUserMaster") -> "UserDataClass":
        return cls(
            user_name=user.user_name,
            mobile=user.mobile,
            email_id=user.email_id,
            user_id = user.user_id
        )

def user_email_selector(email_id:str) -> "RsmUserMaster":
    user = models.RsmUserMaster.objects.filter(email_id=email_id).first()
    return user

def create_token(email_id:str) -> "RsmUserMaster":
    payload = dict(
        email_id=email_id,
        exp = datetime.datetime.utcnow()+datetime.timedelta(hours=24),
        iat=datetime.datetime.utcnow()
    )
    token = jwt.encode(payload,settings.JWT_SECRET,algorithm="HS256")
    return token

