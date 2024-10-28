from openai import OpenAI
import os
class NVIDIA:
    def __init__(self) -> None:
        api_key = os.environ.get("NVIDIA_API")
        self.client = OpenAI(
            base_url = "https://integrate.api.nvidia.com/v1",
            api_key = api_key
        )
    def call(self, prompt):
        completion = self.client.chat.completions.create(
        model="meta/llama-3.2-3b-instruct",
        messages=[{"role":"user","content":prompt}],
        temperature=0.2,
        top_p=0.7,
        max_tokens=1024,
        stream=True
        )

        for chunk in completion:
            if chunk.choices[0].delta.content is not None:
                print(chunk.choices[0].delta.content, end="")

nvidia = NVIDIA()
nvidia.call("Teach me concurency in golang")