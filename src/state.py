from typing import TypedDict, Any

from src.user_profile import UserProfile


class ConversationState(TypedDict):
    messages: list
    user_profile: UserProfile
    response: str