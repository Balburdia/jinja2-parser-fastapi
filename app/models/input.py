"""Input models for the API endpoints."""
from typing import Literal

from pydantic import BaseModel, Field


class RenderInput(BaseModel):
    """Input model to jinja2 render endpoint."""

    template: str = Field(..., description="Template to be rendered.")
    input_type: Literal['json', 'yaml'] = Field(default="json", description="Define the values input type.")
    values: str = Field(default="", description="Values to use when replacing variables on the template.")
    dummy_values: bool = Field(default=False, description="If True use dummy values to fill template variables.")
    show_whitespaces: bool = Field(default=False, description="Show whitespaces after rendering.")
    trim_blocks: bool = Field(default=False, description="If True, render the template with trim_blocks.")
    lstrip_blocks: bool = Field(default=False, description="If True, render the template with lstrip_bloks.")


    class Config:
        """Model example."""

        schema_extra = {
            "example": {
                "template": "Hi, {{ name }}!",
                "dummy_values": False,
                "input_type": 'yaml',
                "values": "name: 'John'",
                "show_whitespaces": False,
                "trim_blocks": False,
                "lstrip_blocks": False
            }
        }
