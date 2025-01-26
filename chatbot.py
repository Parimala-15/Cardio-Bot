import os
import re
from PyPDF2 import PdfReader
from langchain_community.embeddings import SentenceTransformerEmbeddings
from langchain_community.vectorstores import Chroma
from langchain.prompts import PromptTemplate
from langchain.schema import Document
from langchain_community.llms import LlamaCpp
import warnings
import fitz  # PyMuPDF
import requests
from dotenv import load_dotenv
import cohere

# Load environment variables from .env file
load_dotenv()

# Define the Cohere API key directly in the code (replace with your actual API key)
COHERE_API_KEY = "ppjDiRLoosIzqc0iFHZ53OkVNkxlQvexXIAUciPL"

# Clear Hugging Face cache function
def clear_cache():
    cache_dir = os.path.expanduser("~/.cache/huggingface/transformers")
    if os.path.exists(cache_dir):
        for root, dirs, files in os.walk(cache_dir, topdown=False):
            for name in files:
                os.remove(os.path.join(root, name))
            for name in dirs:
                os.rmdir(os.path.join(root, name))

clear_cache()
print("Cache cleared.")

# Path to your repaired PDF file
pdf_file_path = r"C:\\Users\\parim\\Downloads\\healthyheart (1)_repaired.pdf"

# Open the PDF file
pdf_document = fitz.open(pdf_file_path)

# Get the number of pages in the PDF
num_pages = pdf_document.page_count
print(f"Number of pages in the PDF: {num_pages}")

# Initialize an empty string to hold the extracted text
pdf_text = ""

# Extract text from all pages
for page_num in range(num_pages):
    page = pdf_document.load_page(page_num)  # Get each page
    pdf_text += page.get_text()  # Extract text from the page

# Optionally, save the extracted text to a .txt file with UTF-8 encoding
with open("extracted_text.txt", "w", encoding="utf-8") as file:
    file.write(pdf_text)

print("Text extraction completed successfully.")

# Function to chunk text into smaller pieces
def chunk_text(text, chunk_size):
    return [text[i:i + chunk_size] for i in range(0, len(text), chunk_size)]

# Initialize an empty list to store text from each page
text = [page.get_text() for page in pdf_document]
chunks = [chunk for page in text for chunk in chunk_text(page, chunk_size=1000) if chunk.strip()]
documents = [Document(page_content=chunk) for chunk in chunks]

# Create the vector store (optional step for context retrieval)
# If you still want to use vector search, you can continue using it as per your design
# Otherwise, skip this part and focus on using Cohere for responses

# Set up the Llama model correctly (if you're using local models)
try:
    # Path to the Llama model (update this path as needed)
    llm_model_path = r'C:\\Users\\parim\\Documents\\cardio-bot\\BioMistral-7B.Q4_K_M.gguf'

    # Load the LLM model
    llm = LlamaCpp(
        model_path=llm_model_path,
        temperature=0.2,
        max_tokens=2048,
        top_p=0.95,
        context_length=32768  # Include the context length directly here
    )
    print("LLM model loaded successfully!")

except Exception as e:
    print(f"Error loading LLM model: {e}")
    llm = None  # Set llm to None or a mock value

# Define the get_response function to use Cohere API
def get_response(query):
    try:
        # Initialize Cohere client
        co = cohere.Client(COHERE_API_KEY)

        # Generate a response using Cohere's generate endpoint
        response = co.generate(
            model="command-xlarge-nightly",
            prompt=query,
            max_tokens=1000 # Increased max_tokens for longer responses
        )

        # Extract and return the generated response
        return response.generations[0].text.strip()

    except Exception as e:
        return f"Error connecting to the Cohere API: {e}"

# Define a function to handle longer responses in case of truncation
def get_long_response(query):
    try:
        co = cohere.Client(COHERE_API_KEY)

        response = co.generate(
            model="command-xlarge-nightly",
            prompt=query,
            max_tokens=1000 # Adjust this value
        )

        # Check if the response is cut off and needs more tokens
        full_response = response.generations[0].text.strip()

        # If it's cut off, request more tokens
        while len(full_response.split()) < 1000:  # Adjust this threshold as needed
            response = co.generate(
                model="command-xlarge-nightly",
                prompt=query,
                max_tokens=1000
            )
            full_response += response.generations[0].text.strip()

        return full_response

    except Exception as e:
        return f"Error connecting to the Cohere API: {e}"

# Example usage of the get_response function
if __name__ == "__main__":
    query = "What are the risk factors for heart health?"
    response = get_long_response(query)
    print(response)

# Clean up
pdf_document.close()
print("Resources cleaned up successfully!")
