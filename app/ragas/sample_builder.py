from ragas import EvaluationDataset
from ragas.dataset_schema import SingleTurnSample


COLUMN_MAPPING = {
  'user_input': 'question',
  'reference': 'reference',
  'response': 'answer',
  'retrieved_contexts': 'context'
}


def build_single_turn_sample(sample: dict,
                             column_mapping=COLUMN_MAPPING) -> SingleTurnSample:
  
  user_input = sample.get(column_mapping['user_input'])
  reference = sample.get(column_mapping['reference'])
  response = sample.get(column_mapping['response'])
  retrieved_contexts = sample.get(column_mapping['retrieved_contexts'])
  
  ## PARCHE PARA CABA
  if isinstance(retrieved_contexts, str):
    retrieved_contexts = retrieved_contexts.split("TÍTULO:")
    retrieved_contexts.pop(0)
  ## PARCHE PARA CABA

  if not user_input or not response:
    print('user_input or response missing')
    return None  
  
  sample = SingleTurnSample(
    user_input= user_input,
    response= response,
    reference= reference,
    retrieved_contexts= retrieved_contexts,
  )

  return sample


def build_ragas_dataset(responses: list[dict]) -> EvaluationDataset:
  
  if len(responses) == 0:
      raise ValueError("No valid samples created - cannot build RAGAS dataset")

  samples = [
    build_single_turn_sample(response) for response in responses
  ]
  
  evaluationDataset = EvaluationDataset(samples = samples)
  return evaluationDataset

