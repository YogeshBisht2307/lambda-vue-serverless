import jwt
import json
import logging
from functools import wraps
from typing import Optional, Callable, Any
from aws_lambda_powertools.utilities import parameters
from aws_lambda_powertools.event_handler import Response
from common.db.dal import get_user_by_id


logger = logging.getLogger()
logger.setLevel(logging.DEBUG)


def login_required(application) -> Callable:
    def decorated_function(handler: Callable) -> Callable:
        @wraps(handler)
        def wrapped(*args, **kwargs) -> Optional[Any]:
            token = application.current_event.get_header_value(
                name="X-APP-TOKEN", case_sensitive=False)
            if not token:
                return Response(status_code=401, body=json.dumps({"message": "Authorization Error"}))

            payload = jwt.decode(
                token.encode('utf-8'), parameters.get_secret("LOGIN_JWT_SECRET"), algorithms=["HS256"]
            )

            if payload['type'] != 'signin':
                return Response(status_code=401, body=json.dumps({"message": "Authorization Error"}))

            application.current_event.raw_event['requestContext']['identity']['user'] = payload['user']
            return handler(*args, **kwargs)
        return wrapped
    return decorated_function
