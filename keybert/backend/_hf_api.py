from ._base import BaseEmbedder
import numpy as np
import json
from typing import List
import requests

class HfApiEmbeddingModel:
    def __init__(self, multilingual= False, key: str= ""):
        super().__init__()
        self.model_name =  "all-MiniLM-L6-v2" if not multilingual else "paraphrase-xlm-r-multilingual-v1"
        self.key = key
    
    def embed(self, documents: List[str]) -> np.ndarray:
        headers = {"Authorization": f"Bearer {self.key}"}
        API_URL = f"https://api-inference.huggingface.co/pipeline/feature-extraction/sentence-transformers/{self.model_name}"
        data = json.dumps({"inputs": list(documents)})
        response = requests.request("POST", API_URL, headers=headers, data=data)
        print(response.content.decode("utf-8"))
        return np.array(json.loads(response.content.decode("utf-8")))

