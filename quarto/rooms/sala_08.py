from helpers import text, hyperlink

def revisar(autorizar_acceso):

    acceso_tripulante_uno = autorizar_acceso(True, "Alta")
    acceso_tripulante_dos = autorizar_acceso(True, "Baja")
    acceso_tripulante_tres = autorizar_acceso(False, "Alta")

    if acceso_tripulante_uno == True and acceso_tripulante_dos == False and acceso_tripulante_tres == False:
        hyperlink("¡Correcto! Avanza a la siguiente página", "sala_09.html", "success")
    else:
        text("No es la respuesta correcta. Inténtalo nuevamente.", "warning")

def autorizar_acceso(tarjeta, resistencia_traje):

    # Escribe tu respuesta aquí
    if tarjeta == True and resistencia_traje == "Alta":
        return True
    else:
        return False


if __name__ == "__main__":
    revisar(autorizar_acceso)
