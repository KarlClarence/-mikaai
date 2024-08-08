import openai

openai.api_key = "02017651e86e42de9e815ec3ef8aab76"
openai.api_base = "https://mika-1.openai.azure.com/"

# 列出所有可用的 engines
engines = openai.Engine.list()

for engine in engines['data']:
    print(engine['id'])
