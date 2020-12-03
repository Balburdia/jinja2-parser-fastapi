"""Main file for FastAPI application."""
from html import escape
from random import choice
from typing import Dict

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from jinja2 import Environment, exceptions, meta
from starlette.middleware.cors import CORSMiddleware

import app.utils as validators
from app.core.config import settings
from app.models.input import RenderInput


app = FastAPI(
    title=settings.PROJECT_NAME,
    description="Jinja2 Render Live with FastAPI"
)

# Set all CORS enabled origins
if settings.BACKEND_CORS_ORIGINS:
    app.add_middleware(
        CORSMiddleware,
        allow_origins=[str(origin) for origin in settings.BACKEND_CORS_ORIGINS],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

app.mount("/static", StaticFiles(directory="app/static"), name="static")


templates = Jinja2Templates(directory="app/templates")


@app.get("/", include_in_schema=False, response_class=HTMLResponse)
async def main(request: Request):
    """Render index page into root endpoint."""
    return templates.TemplateResponse("index.html", {"request": request})


@app.post('/api/v1/render', response_class=HTMLResponse, summary="Jinja2 Render",
          description="Use Jinja2 to render a template using the values provided.")
def render(conversion_input: RenderInput):
    """Render a template using the values provided by the user.

    :param conversion_input: pydantic input model to deal with endpoint parameters.
    :return: jinja2 rendered html.
    """
    jinja2_env = Environment()
    jinja2_env.trim_blocks = conversion_input.trim_blocks
    jinja2_env.lstrip_blocks = conversion_input.lstrip_blocks

    # Load the template
    try:
        jinja2_tpl = jinja2_env.from_string(conversion_input.template)
    except (exceptions.TemplateSyntaxError, exceptions.TemplateError) as e:
        return f"Syntax error in jinja2 template: {e}"

    dummy_values = ['Dorime', 'Interimo', 'adapare', 'Ameno', 'Latire', 'Latiremo',
                    'Omenare', 'imperavi', 'Dimere', 'matiro', 'Matiremo', 'emulari']

    values = {}
    if conversion_input.dummy_values:
        # List template variables (introspection)
        vars_to_fill = meta.find_undeclared_variables(jinja2_env.parse(conversion_input.template))

        for v in vars_to_fill:
            values[v] = choice(dummy_values)
    else:
        # Call the right validation method based on input type
        try:
            values = getattr(validators, f"validate_{conversion_input.input_type}")(conversion_input.values)
        except ValueError as e:
            return str(e)

    # If ve have empty var array or other errors we need to catch it and show
    try:
        rendered_jinja2_tpl = jinja2_tpl.render(values)
    except (exceptions.TemplateRuntimeError, ValueError, TypeError) as e:
        return f"Error in your values input filed: {e}"

    if conversion_input.show_whitespaces:
        # Replace whitespaces with a visible character (will be grayed with javascript)
        rendered_jinja2_tpl = rendered_jinja2_tpl.replace(' ', u'•')

    return escape(rendered_jinja2_tpl).replace('\n', '<br />')


@app.get("/api/v1/health", summary="Health check", description="Check if the API is up.")
async def get_health_check_status() -> Dict:
    """Generate a health check response for the applications."""
    return {"status": "UP", "details": "Application is running normally."}
