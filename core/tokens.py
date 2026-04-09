import tiktoken


def estimar_tokens(texto_usuario: str, modelo: str) -> int:
    try:
        encoding = tiktoken.encoding_for_model(modelo)
    except KeyError:
        encoding = tiktoken.get_encoding("cl100k_base")

    return len(encoding.encode(texto_usuario))