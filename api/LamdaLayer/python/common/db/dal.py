import os
import uuid
import base64
from common.clients import get_client
from common.db.models import User
from typing import Optional
from boto3.dynamodb.types import TypeSerializer, TypeDeserializer

Ts = TypeSerializer()
Tds = TypeDeserializer()


def create_user(name: str, email: str, password: str, roles: list) -> User:
    user_entity = User(
        id=str(uuid.uuid4()),
        name=name,
        email=str(email).lower(),
        password=password,
        roles=roles
    )
    user_entity.hash_password(base64.b64encode(os.urandom(32)))
    get_client('dynamodb').put_item(
        TableName='User',
        Item=Ts.serialize(user_entity.toDict()).get('M')
    )
    return user_entity


def get_user_by_id(user_id: str) -> Optional[User]:
    response = get_client('dynamodb').get_item(
        TableName='User',
        Key={'id': {'S': user_id}}
    )
    try:
        return User(**Tds.deserialize({"M": response['Item']}))
    except KeyError:
        return None


def get_user_by_email(email: str) -> Optional[User]:
    response = get_client('dynamodb').query(
        TableName='User',
        IndexName='GetByEmail',
        KeyConditions={
            'email': {
                "AttributeValueList": [
                    {'S': str(email).lower()}
                ],
                "ComparisonOperator": "EQ"
            }
        }
    )
    try:
        return User(**Tds.deserialize({"M": response['Items'][0]}))
    except (KeyError, IndexError):
        return None
