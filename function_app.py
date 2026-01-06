import azure.functions as func
import logging
import pandas as pd
import io

app = func.FunctionApp(http_auth_level=func.AuthLevel.FUNCTION)

@app.route(route="executar_python")
def trigger_python(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('A função foi disparada pelo Power Automate.')

    # Exemplo simples de criação de dados
    df = pd.DataFrame({"Status": ["Sucesso!"], "Mensagem": ["Rodando no Azure"]})

    # Retornamos apenas uma confirmação por enquanto
    return func.HttpResponse("Código Python executado com sucesso!", status_code=200)
