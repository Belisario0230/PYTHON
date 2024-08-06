
# Ejemplo de uso
from Ventas_Modulo import enviar_correo_asunto_cuerpo
if __name__ == "__main__":
    destinatario = "buitragolievanob3002@hotmail.com"
    asunto = "Consulta sobre seguridad privada"
    cuerpo = "Estimado equipo de Supervigilancia,\n\nTengo una consulta sobre seguridad privada en mi empresa. ¿Podrían proporcionarme más información?\n\nAtentamente,\n[Nombre]"

    enviar_correo_asunto_cuerpo(destinatario, asunto, cuerpo)
