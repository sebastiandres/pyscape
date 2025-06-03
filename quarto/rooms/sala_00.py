from helpers import text, hyperlink

def revisar(answer):
    if answer == "PySchool2025":
        hyperlink("¡Correcto! Haz click aquí para avanzar al siguiente desafío", "sala_01.html", "success")
    else:
        incorrect_answer = f"""Estás probando nuevas respuestas, muy bien.  
        Recuerda que la respuesta es PySchool2025"""
        text(incorrect_answer, "warning")


if __name__ == "__main__":
    revisar(None)
    revisar("PySchool2024")
    revisar("PySchool2025")
