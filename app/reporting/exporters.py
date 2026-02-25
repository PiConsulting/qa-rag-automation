import time 
from pathlib import Path
from ragas import EvaluationDataset

def save_metrics(output_path: str,
                 results: EvaluationDataset):
  
  output_path = Path(output_path)
  output_path.parent.mkdir(parents= True, exist_ok= True)
  
  timestr = time.strftime("%Y%m%d-%H%M%S")
  base_name = output_path.stem
  extension = output_path.suffix
  timestamped_path = output_path.parent / f"{base_name}_{timestr}{extension}"
  
  handle_output_file_format(timestamped_path, results)
  return results
  
  
def handle_output_file_format(output_path: str, 
                              results: EvaluationDataset):
  
  results_copy = results
  results_copy = results_copy.to_pandas()
  
  if output_path.suffix == '.xlsx':
    results_copy.to_excel(output_path)
    
  elif output_path.suffix == '.csv':
    results_copy.to_csv(output_path)
  
  elif output_path.suffix == '.json':
    results_copy.to_json(output_path)
  
  else:
    raise ValueError('ValueError: Unsupported file format')