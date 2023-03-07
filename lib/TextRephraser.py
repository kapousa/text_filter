import os
import re

import openai

from lib.constants.k import F, S, T


class TextRephraser:

    def __init__(self):
        ''' Constructor for this class. '''
        self.k_path = ''

    def reprashe_sentence(self, user_text):

        oak = "{0}{1}{2}".format(F, S, T)
        openai.api_key = oak
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
        _path = 'apk.gkey'
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
