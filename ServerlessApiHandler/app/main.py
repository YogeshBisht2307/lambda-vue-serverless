import asyncio
from typing import Dict
from common.base import login_required
from app.handlers import get_users_request_handler
from app.handlers import user_signup_request_handler
from app.handlers import user_signin_request_handler
from aws_lambda_powertools.event_handler import APIGatewayRestResolver, CORSConfig
from aws_lambda_powertools.utilities.typing import LambdaContext

application = APIGatewayRestResolver(cors=CORSConfig(allow_origin="*"))


@application.post("/auth/signin")
def signin_handler() -> Dict:
    return asyncio.run(user_signin_request_handler(application.current_event))


@application.post("/auth/signup")
def signup_handler() -> Dict:
    return asyncio.run(user_signup_request_handler(application.current_event))


@application.get("/users")
@login_required(application)
def get_users_handler() -> Dict:
    return asyncio.run(get_users_request_handler(application.current_event))


def lamba_event_handler(event: dict, context: LambdaContext) -> dict:
    return application.resolve(event, context)
