from huggingface_hub import HfApi

api = HfApi()
info = api.model_info("Chinwendu/lung_ct_detection_model")
print(info)
