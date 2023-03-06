import re

import openai


class TextRephraser:

    def reprashe_sentence(self, user_text):
        # Set up the OpenAI API key
        openai.api_key = "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"

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
        # Set up the OpenAI API key
        openai.api_key = "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"

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
