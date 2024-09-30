from promptflow.client import PFClient

pf_client = PFClient()

flow_path = "../rag_pf"
flow_input = {"text": "What's the engine's temperature range?"}
flow_output = pf_client.test(flow=flow_path, inputs=flow_input)
print(flow_output)

