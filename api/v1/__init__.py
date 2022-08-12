from fastapi import APIRouter
from fastapi.responses import JSONResponse

from core.config import settings
from schemas.translate import Language

from .translate import generate_translation

router = APIRouter(
    prefix=settings.URL_PREFIX,
    tags=["translate"],
    responses={404: {"description": "Not found"}},
)


@router.post("/translate")
async def translate_text(
    input_text: str,
    destination_language: Language,
    source_language: str = "en",
) -> JSONResponse:
    translated_text = None

    if destination_language == Language.GERMAN:
        translated_text = generate_translation("German", input_text)
    elif destination_language == Language.FRENCH:
        translated_text = generate_translation("French", input_text)
    else:
        translated_text = generate_translation("Romanian", input_text)

    return JSONResponse(content={"translation": translated_text})
