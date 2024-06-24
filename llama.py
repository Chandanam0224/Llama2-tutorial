
from clarifai.client.workflow import Workflow

# Your PAT (Personal Access Token) can be found in the Account's Security section

# Initialize the workflow_url
workflow_url = "https://clarifai.com/buvzaa4h6c5f/GenAI-2/workflows/workflow-d6a45c"
text_classfication_workflow = Workflow(
    url= workflow_url , pat="b7e1e8b542284462a1483ee6bdd8a06c"
)
result = text_classfication_workflow.predict_by_bytes(b"I hate you", input_type="text")
print(result.results[0].outputs[0].data)
