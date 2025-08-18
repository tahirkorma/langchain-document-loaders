from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
from langchain_community.document_loaders import PyPDFLoader

import os
base_path = os.path.dirname(__file__)
file_path = os.path.join(base_path,"documents", "Research Project - Tahir Korma.pdf")


loader = PyPDFLoader(file_path)
docs = loader.load()

print(len(docs))
print(docs[0].page_content)
print(docs[0].metadata)

load_dotenv()
model = ChatGoogleGenerativeAI(model='gemini-2.0-flash')
parser = StrOutputParser()

prompt = PromptTemplate(
    template = 'write the name of the author of this research project \n {report}',
    input_variables=['report']
)

chain = prompt | model | parser
print(chain.invoke({'report':docs[0].page_content}))