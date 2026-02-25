from ragas import evaluate
from ragas import EvaluationDataset
from ragas.llms import LangchainLLMWrapper
from ragas.embeddings import LangchainEmbeddingsWrapper
from langchain_openai import AzureChatOpenAI, AzureOpenAIEmbeddings

from ragas.metrics import ContextRecall, ContextPrecision, Faithfulness, AnswerRelevancy, SemanticSimilarity

from dotenv import load_dotenv
load_dotenv()


def initilize_evaluator(config: dict[str]) -> tuple:
  llm = AzureChatOpenAI(
    azure_deployment = config['llm'].get('model'),
    api_version = config['llm'].get('api_version'),
  )
  emb = AzureOpenAIEmbeddings(
    azure_deployment = config['llm'].get('embeddings'),
    api_version = config['llm'].get('api_version'),
  )
  
  evaluator_llm = LangchainLLMWrapper(llm)
  evaluator_emb = LangchainEmbeddingsWrapper(emb)
  
  return (evaluator_llm, evaluator_emb)


def run_ragas_evaluation(dataset: EvaluationDataset,
                         config: dict[str]) -> dict[str]:
  
  evaluator_llm, evaluator_emb = initilize_evaluator(config)
  
  metrics = [SemanticSimilarity(), AnswerRelevancy(), ContextPrecision(), Faithfulness(),  ContextRecall()]
  
  results = evaluate(
    dataset= dataset,
    metrics= metrics,
    llm= evaluator_llm,
    embeddings= evaluator_emb
  )
  
  print(results)
  return results