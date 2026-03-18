from typing import Dict

from ninja import Schema


class VoteSchema(Schema):
    option: str


class PollOutListSchema(Schema):
    id: int
    question: str


class CreatePollSchema(Schema):
    question: str
    text: Dict[str, str]


class PollOutSchema(Schema):
    id: int
    question: str
    text: Dict[str, str]


class ErrorSchema(Schema):
    error: str
