import yaml
from app.datasets.loader import load_test_cases
from app.datasets.validator import validate_dataset_schema
from app.datasets.preprocessing import preprocess_dataframe
from app.client.rag_client import RAGClient
from app.ragas.sample_builder import build_ragas_dataset
from app.ragas.evaluate import run_ragas_evaluation
from app.reporting.exporters import save_metrics

# Cargar dataset (.json, .xlsx, .csv)
df = load_test_cases('./app/data/raw/input.xlsx')

# Validacion de columnas y tipo de datos
df = validate_dataset_schema(df)

# Estructuracion y refinamiento de textos
df = preprocess_dataframe(df)

# Carga de variables de configuracion
with open('./app/config/config.yaml', 'r') as file:
  config_data = yaml.load(file, Loader= yaml.FullLoader)
  
# Inicializa la interaccion con el RAG cliente
client = RAGClient(config_data)

# Captura las respuestas
responses = client.query_batch(df['user_input'], df['reference'])

# Crea un archivo .json con todas las respuestas obtenidas
save_responses = client.save_api_responses(responses, './app/data/processed/outcome.json')

# Crea el dataset de ragas
dataset = build_ragas_dataset(responses)

# Ejecuta la medicion de Ragas
results = run_ragas_evaluation(dataset, config_data)

# Crea los archivos de resultados (.json, .xlsx, .csv)
exported_results = save_metrics('./app/data/processed/results_outcome.json', results)
exported_results = save_metrics('./app/data/processed/results_outcome.xlsx', results)



### Emitir graficos con kpi usando ()
# https://mode.com/blog/python-interactive-plot-libraries

# portal azure
# - recursos para generar reportes (consumiendo)

# levantar recurso de ragas
# - simil a mlflow