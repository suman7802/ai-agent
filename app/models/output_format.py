from typing import Optional
from pydantic import BaseModel, Field


class Output_format(BaseModel):
    step: str = Field(
        ...,
        description="The step ID. Example: START, PLAN, OBSERVE, TOOL, OUTPUT, RESULT",
    )

    content: Optional[str] = Field(
        None,
        description="The optional string content for the step.",
    )

    tool: Optional[str] = Field(
        None,
        description="The ID of the tool to call. Example: get_weather, get_joke",
    )

    input: Optional[str] = Field(
        None,
        description="The optional string input for the tool.",
    )
