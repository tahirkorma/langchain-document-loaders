from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_community.document_loaders import TextLoader
from dotenv import load_dotenv

load_dotenv()
model = ChatGoogleGenerativeAI(model='gemini-2.0-flash')
parser = StrOutputParser()

prompt = PromptTemplate(
    template = 'write a short summary for the following \n {text}',
    input_variables=['text']
)

#load file
import os
base_path = os.path.dirname(__file__)
file_path = os.path.join(base_path,"documents", "india.txt")
loader = TextLoader(file_path, encoding = "utf-8")

docs=loader.load()

print(type(docs))
print(len(docs))
# print(docs[0].page_content)
print(docs[0].metadata)

chain = prompt | model | parser

print(chain.invoke({'text':docs[0].page_content}))