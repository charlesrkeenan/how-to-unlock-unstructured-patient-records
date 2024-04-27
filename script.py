# Import software dependencies
from azure.core.credentials import AzureKeyCredential
from azure.ai.documentintelligence.models import AnalyzeResult
from azure.ai.formrecognizer import DocumentAnalysisClient

# Your Azure Document Intelligence / Cognitive Services endpoint, your resource API key, and your unstructured record's file path
endpoint = ""
key = ""
record = ""

# Create a Document Analysis Client for connecting with the Azure API
document_analysis_client = DocumentAnalysisClient(endpoint=endpoint, credential=AzureKeyCredential(key))

# Open your record as a byte object and call the Azure API to extract the written text and key-value pairs
with open(record, "rb") as f:
    poller = document_analysis_client.begin_analyze_document(
        model_id="prebuilt-document",
        document=f)
result: AnalyzeResult = poller.result()

# Print the results to your console
print(f"Record content:\n{result.content}")
print("Key-value pairs:")
for kv_pair in result.key_value_pairs:
    if kv_pair.key and kv_pair.value:
        print(f'{kv_pair.key.content}: {kv_pair.value.content}')