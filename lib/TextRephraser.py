import os
import re

import openai


class TextRephraser:

    k_path = ''

    def __init__(self, k_path):
        ''' Constructor for this class. '''
        self.k_path = k_path

    def reprashe_sentence(self, user_text):
        _path = "{0}{1}".format(self.k_path, '/static/apk.gkey')
        with open(_path) as f:
            contents = f.read()

        openai.api_key = contents
        # Define the GPT-3 prompt that will be used to generate rephrased paragraphs
        text = "Please rephrase the follwing text: {}".format(user_text)
        prompt = (text)
        # Define the OpenAI API parameters
        parameters = {
            "model": "text-davinci-002",
            "prompt": prompt,
            "temperature": 0.7,
            "max_tokens": 100,
            "top_p": 1,
            "frequency_penalty": 0,
            "presence_penalty": 0
        }

        # Call the OpenAI API to generate rephrased paragraphs
        response = openai.Completion.create(**parameters)

        # Extract the rephrased paragraphs from the OpenAI API response
        rephrased_paragraphs = response.choices[0].text

        # Clean up the rephrased paragraphs
        rephrased_paragraphs = re.sub('\n', '', rephrased_paragraphs)
        rephrased_paragraphs = re.sub('\t', '', rephrased_paragraphs)

        # Print the rephrased paragraphs
        return rephrased_paragraphs

    def summary_sentence(self, user_text):
        _path = "{0}{1}".format(self.k_path, '/static/apk.gkey')
        with open(_path) as f:
            contents = f.read()

        # Define the GPT-3 prompt that will be used to generate rephrased paragraphs
        text = "Please summary the follwing text: {}".format(user_text)
        prompt = (text)
        # Define the OpenAI API parameters
        parameters = {
            "model": "text-davinci-002",
            "prompt": prompt,
            "temperature": 0.7,
            "max_tokens": 100,
            "top_p": 1,
            "frequency_penalty": 0,
            "presence_penalty": 0
        }

        # Call the OpenAI API to generate rephrased paragraphs
        response = openai.Completion.create(**parameters)

        # Extract the rephrased paragraphs from the OpenAI API response
        rephrased_paragraphs = response.choices[0].text

        # Clean up the rephrased paragraphs
        rephrased_paragraphs = re.sub('\n', '', rephrased_paragraphs)
        rephrased_paragraphs = re.sub('\t', '', rephrased_paragraphs)

        # Print the rephrased paragraphs
        return rephrased_paragraphs
