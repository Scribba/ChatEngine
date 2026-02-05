from typing import TypedDict, Any, NotRequired



class ConversationState(TypedDict):
    messages: list
    user_profile: dict[str, Any]
    response: NotRequired[str]