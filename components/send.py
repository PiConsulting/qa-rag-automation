import pandas as pd
import requests
import time

from components.chat_completions import chat_completion
from components.compare_text import compare_text
from components.config import sets
from components.prompt import PROMPT_TEMPLATE

def send_requests(file_path: str, url: str):
    excel_file = pd.ExcelFile(file_path)
    sheet_names = excel_file.sheet_names

    output_columns = ['id', 'conversation_id','consulta','respuesta_esperada', 'respuesta_obtenida', 'similitud', 'tiempo']
    output_data = []

    # itera por cada hoja del archivo excel
    for i in range(len(sheet_names)):
      
        sheet_name = sheet_names[i]
        df = pd.read_excel(file_path, sheet_name=sheet_name)
        headers = {
        'Content-Type': 'application/json',
        }
  
        conversation_id = "" 
        
        # itera por cada pregunta de la hoja
        for j, row in df.iterrows():
            question = row['consulta']
            expected_answer = row['respuesta_esperada']
            source = row['fuente']     

            PROMPT = PROMPT_TEMPLATE.format(n=3,
                                            source=source,
                                            question=question,
                                            expected_answer=expected_answer,
                                            sets=sets)     
            


            # MODIFICAR EL BODY DEPENDIENDO LA NECESIDAD DEL CASO
            body = {
            "conversation_id": conversation_id,
            "endpoint_selected": "Tramites",
            "query": question
            }

            init_time = time.time()

            try:
                response = requests.post(url, headers=headers, json=body)
                print(i+1, response)
                data = response.json()

                if conversation_id == "":
                    conversation_id = data['conversation_id']

                obtained_answer = data['answer']
                response_time = round(time.time() - init_time, 2)

            except:
                obtained_answer = 'Respuesta no recuperada por un error en la solicitud'
                print(f'Solicitud {i+1}: Tuvo errores ')

            similarity = compare_text(expected_answer, obtained_answer)
            output_data.append([i+1, conversation_id,question, expected_answer, obtained_answer, similarity, response_time])

            if similarity > 0.2:
                generated_data_set = chat_completion(PROMPT)
                
                list_of_generated_questions = generated_data_set['list_of_answers']

                # itera por cada pregunta generada por la ia
                for k in range(len(list_of_generated_questions)):
                    body['question'] = list_of_generated_questions[k]['question']
                    body['conversation_id'] = conversation_id

                    init_time_generated = time.time()

                    try:
                        response = requests.post(url, headers=headers, json=body)
                        data = response.json()
                        generated_obtained_answer = data['answer']
                        generated_response_time = round(time.time() - init_time_generated, 2)

                    except:
                        obtained_answer = 'Respuesta no recuperada por un error en la solicitud'
                        print(f'Solicitud {i+1}.{k+1}: Tuvo errores ')

                    generated_expected_answer = list_of_generated_questions[k]["expected_answer"]

                    similarity = compare_text(generated_expected_answer, generated_obtained_answer)
                    output_data.append([i+1, conversation_id, list_of_generated_questions[k]['question'], generated_expected_answer, generated_obtained_answer, similarity, generated_response_time])

                    if similarity < 0.2: 
                        conversation_id = ""
                        break

            conversation_id = ""


    df_answers = pd.DataFrame(output_data, columns=output_columns)
    df_answers.to_excel(f'./files/resultados.xlsx', index=False)                
                 