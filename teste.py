import azure.functions as func
import logging

app = func.FunctionApp(http_auth_level=func.AuthLevel.FUNCTION)

@app.route(route="executar_python")
def trigger_python(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('O Power Automate disparou a função.')

    resultado = "Olá! O código rodou com sucesso no Azure."
    
    return func.HttpResponse(f"Sucesso: {resultado}", status_code=200)
