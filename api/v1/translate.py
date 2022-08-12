from core.config import settings
from transformers import PreTrainedTokenizerFast, T5ForConditionalGeneration

tokenizer = PreTrainedTokenizerFast(
    tokenizer_file=f"{settings.MODEL_DATA}/tokenizer.json"
)

model = T5ForConditionalGeneration.from_pretrained(
    f"{settings.MODEL_DATA}/pytorch_model.bin",
    config=f"{settings.MODEL_DATA}/config.json",
    return_dict=True,
)


def generate_translation(target_lang: str, input: str) -> str:
    input_ids = tokenizer(
        f"translate English to {target_lang}: {input}", return_tensors="pt"
    ).input_ids

    outputs = model.generate(input_ids, max_length=128)

    decoded = tokenizer.decode(outputs[0], skip_special_tokens=True)

    return decoded
