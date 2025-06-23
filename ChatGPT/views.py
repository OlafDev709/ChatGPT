from django.shortcuts import render
from django.http import JsonResponse
import os
from openai import OpenAI
from decouple import config

SECRET_KEY = config("SECRET_KEY")
# openai.api_key = SECRET_KEY

# def get_completion(prompt):
#     client = OpenAI(api_key=SECRET_KEY)
#     print(prompt)
#     response = client.responses.create(
#         model="gpt-40",
#         input=prompt,
#         # max_tokens=1024,
#         introductions = "You are a helpful assistant. Please answer the following question based on the provided prompt.",
#         # n=1,
#         # stop=None,
#         # temperature=0.5,
#     )
#     # query = openai.Completion.create(
#     #     engine="text-davinci-003",
#     #     prompt=prompt,
#     #     max_tokens=1024,
#     #     n=1,
#     #     stop=None,
#     #     temperature=0.5,
#     # )

#     # response = query.choices[0].text
#     print(response)
#     return response.output_text


# def query_view(request):
#     if request.method == 'POST':
#         # prompt = request.POST.get('prompt')
#         client = OpenAI(api_key=SECRET_KEY)
#         response = client.responses.create(
#             model="gpt-4o",
#             instructions="You are a coding assistant that talks like a pirate.",
#             input="How do I check if a Python object is an instance of a class?",
#         )
#         # response = SECRET_KEY
#         return JsonResponse({'response': response.output_text})
#     return render(request, 'index.html')


# integrate API of ChatGPT with Django
# import openai
def query_view(request):
    if request.method == 'POST':
        client = OpenAI(api_key=SECRET_KEY)
        prompt = request.POST.get('prompt')
        completion = client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {
                    "role": "system",
                    "content": "You are a helpful assistant that talks like a code assistant.",
                },
                {
                    "role": "user",
                    "content": prompt,
                },
            ],
        )

        print(completion.choices[0].message.content)
        return JsonResponse({'response': completion.choices[0].message.content})
    return render(request, 'index.html')
