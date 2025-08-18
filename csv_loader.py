from langchain_community.document_loaders import DirectoryLoader, CSVLoader

import os
base_path = os.path.dirname(__file__)
file_path = os.path.join(base_path,"documents")

loader = DirectoryLoader(
    path=file_path,
    glob='*.csv',
    loader_cls=CSVLoader
)
#load through lazy load
docs = loader.lazy_load()

for doc in docs:
    print(doc.metadata)

#load through without lazy load to fetch row
doc_row = loader.load()
print(doc_row[5].metadata)
print(doc_row[5].page_content)
