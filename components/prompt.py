PROMPT_TEMPLATE = """
Your task is to generate {n} questions and the expected answers for those questions.

The questions and expected answers you need to do, are from {source} and only from this source.
These questions must be a continuation of a first interaction made by another LLM.
You must be exhaustive with your questions, continuing the line of the first question asked, the end goal is to try to break the response from the other LLM.
The first question was: "{question}"
With its expected answer: "{expected_answer}"


The resposnse i need must be in json format, like this: 
{{
    "list_of_answers": [
        {sets}
    ]
}}

The response must be in neutral spanish, and must not include any slang.
"""