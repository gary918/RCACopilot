import os

from langchain_openai import AzureChatOpenAI
from langchain.chains import RetrievalQA
from langchain_community.retrievers import (
    AzureAISearchRetriever,
)

import streamlit as st
import sys
sys.path.append('../..')

from dotenv import load_dotenv, find_dotenv
_ = load_dotenv(find_dotenv()) # read local .env file

class OpenAIClient :
    def __init__(self, api_key=None):
        self.api_key = api_key or os.getenv("OPENAI_API_KEY")
        self.retriever = AzureAISearchRetriever(
            api_key=os.getenv("AZURE_SEARCH_API_KEY"),
            content_key="content",
            top_k=1,
            index_name=os.getenv("AZURE_SEARCH_INDEX_NAME"),
        )
        self.llm = AzureChatOpenAI(
            temperature=0,
            openai_api_version=os.getenv("AZURE_OPENAI_API_VERSION"),
            azure_deployment=os.getenv("AZURE_OPENAI_DEPLOYMENT_NAME")
        )

    def complete(self, prompt, max_tokens=100):
        """
        Completes the prompt using the OpenAI API.

        Args:
            prompt (str): The prompt to complete.
            max_tokens (int): The maximum number of tokens to generate.

        Returns:
            str: The completion of the prompt.
        """
        #response = self.retriever.invoke(prompt)
        chain_type = 'stuff'
        chain = RetrievalQA.from_chain_type(
            llm=self.llm,
            chain_type=chain_type,
            retriever=self.retriever,
            return_source_documents=True,
            metadata={"application_type": "question_answering"},
        )

        response=chain.invoke({"query": prompt}, max_tokens=max_tokens)
        return response



if __name__ == "__main__":
    openai_clinet = OpenAIClient()
    print(openai_clinet.complete("What is the engine temperature range?")['result'])