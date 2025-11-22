from openai import OpenAI

# for backward compatibility, you can still use `https://api.deepseek.com/v1` as `base_url`.
client = OpenAI(api_key="sk-520366701d2f41d2a7e21e36b60ecaae", base_url="https://api.deepseek.com")
print(client.models.list())