import jwt
import time
import json
from typing import Dict
from common.db import dal
from common.base import logger
from aws_lambda_powertools.event_handler import Response
from aws_lambda_powertools.utilities import parameters


async def user_signup_request_handler(event) -> Dict:
    logger.debug(json.dumps(event.raw_event))
    try:
        request_json = event.json_body
    except (TypeError, ValueError) as error:
        logger.error(str(error))
        return Response(status_code=400, body=json.dumps({"message": "Invalid Input Parameter"}))

    if dal.get_user_by_email(request_json.get("email")):
        return Response(status_code=400, body=json.dumps({"message": "Email Already Exists"}))

    user = dal.create_user(**request_json)
    logger.debug(json.dumps(user.toDict()))
    return Response(status_code=201, body=json.dumps({'user': user.toDict()}))


async def user_signin_request_handler(event) -> Dict:
    try:
        request_json = event.json_body
    except (TypeError, ValueError) as error:
        logger.error(str(error))
        return Response(status_code=400, body=json.dumps({"message": "Invalid Input Parameter"}))

    user = dal.get_user_by_email(request_json.get("email"))
    if not user:
        return Response(status_code=400, body=json.dumps({"message": "User Doesn not exists"}))

    logger.debug(json.dumps(user.toDict()))
    if not user.verify_password(request_json.get('password')):
        return Response(status_code=400, body=json.dumps({"message": "Invalid Password"}))

    payload: dict = {
        "user": user.toDict(),
        "type": "signin",
        "exp": int(time.time() + 3600),
    }
    token = jwt.encode(
        payload, parameters.get_secret("LOGIN_JWT_SECRET"), algorithm="HS256")
    return Response(status_code=200, body=json.dumps({'token': token, "user": user.toDict()}))


async def get_users_request_handler(event) -> Dict:
    return Response(status_code=200, body=json.dumps({'user': event.request_context.identity.user}))
