from langchain_community.document_loaders import DirectoryLoader, PyPDFLoader, TextLoader, CSVLoader

import os
base_path = os.path.dirname(__file__)
file_path = os.path.join(base_path,"documents")

loader = DirectoryLoader(
    path=file_path,
    glob='*.pdf',
    loader_cls=PyPDFLoader
)

docs = loader.lazy_load()

for doc in docs:
    print(doc.metadata)