from components.config import AGENT_ENDPOINT, AGENT_KEY, AGENT_NAME
import json
from azure.ai.inference import ChatCompletionsClient
from azure.ai.inference.models import SystemMessage, UserMessage
from azure.core.credentials import AzureKeyCredential

endpoint = AGENT_ENDPOINT
model_name = AGENT_NAME

client = ChatCompletionsClient(
    endpoint=endpoint,
    credential=AzureKeyCredential(AGENT_KEY),
)

def chat_completion(system_prompt: str):
    response = client.complete(
    messages=[
        SystemMessage(content=system_prompt),
    ],
    max_tokens=800,
    temperature=1.0,
    top_p=1.0,
    frequency_penalty=0.0,
    presence_penalty=0.0,
    model=model_name
    )

    data = json.loads(response.choices[0].message.content)
    return data