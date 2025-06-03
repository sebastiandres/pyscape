from helpers import text, hyperlink

def revisar(respuesta):
    suma = sum(range(1,1001))
    if respuesta == None:
        text("Intenta cambiar el valor de la variable `respuesta`.", "info")
    elif respuesta == suma:
        hyperlink("¡Correcto! Haz click aquí para avanzar al siguiente desafío", "sala_06.html", "success")
    else:
        text("No es la respuesta correcta. Inténtalo nuevamente.", "warning")

if __name__ == "__main__":
    revisar(None)
    revisar(sum(range(1,1001)))
    revisar(False)
