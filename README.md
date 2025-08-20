# LangChain Document Loaders

This repository highlights the **most commonly used document loaders in LangChain**, which are essential for bringing raw data into a standardized `Document` format. Document loaders serve as the entry point for processing data before applying text splitters, embeddings, and retrieval pipelines.  

---

## 📌 Top Used Document Loaders

- **CSVLoader** → For loading structured tabular data from `.csv` files.  
- **DirectoryLoader** → For bulk ingestion of multiple files from directories.  
- **PyPDFLoader** → For parsing and extracting text from PDF documents.  
- **TextLoader** → For reading plain text (`.txt`) files.  
- **WebBaseLoader** → For fetching and parsing web pages directly from URLs.  

---

## 🔎 Notes
- These represent the **top-used loaders** in practical LLM applications, but LangChain supports many others (e.g., JSONLoader, UnstructuredFileLoader, EverNoteLoader, etc.).  
- Choosing the right loader depends on your data source (local files, web content, structured datasets, etc.).  
- Loaders are typically combined with **text splitters** to prepare data for downstream tasks such as embeddings, question answering, and RAG.  

---

## 📚 Resources
- [LangChain Document Loaders Documentation](https://python.langchain.com/docs/modules/data_connection/document_loaders/)
