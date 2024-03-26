import requests
import PyPDF2
import openai

# OpenAI API key
openai.api_key = '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'

# Function to download and extract text content from the document


def fetch_document_content(document_url):
    response = requests.get(document_url)
    if response.status_code == 200:
        return response.content
    else:
        print("Failed to download the document.")
        return None

# Funcption to extract text content from the PDF document


def extract_text_from_pdf(pdf_content):
    pdf_reader = PyPDF2.PdfFileReader(pdf_content)
    text = ""
    for page_num in range(pdf_reader.numPages):
        text += pdf_reader.getPage(page_num).extractText()
    return text

# Function to read document text


def read_document(document_text):
    return [document_text]

# Function to ask questions and get answers from GPT-3.5


def ask_question(question, documents):
    prompt = f"Question: {question}\nContext:\n" + '\n'.join(documents)
    response = openai.Completion.create(
        model="davinci-002",
        prompt=prompt,
        max_tokens=150
    )
    return response['choices'][0]['text'].strip()

# Main function


def main():
    document_url = "https://doi.org/10.48550/arXiv.2307.06435"
    document_content = fetch_document_content(document_url)
    if document_content:
        document_text = extract_text_from_pdf(document_content)
        documents = read_document(document_text)

        print("Welcome to the Document Chatbot!")
        while True:
            user_question = input("You: ")
            if user_question.lower() == 'exit':
                print("Exiting the chatbot.")
                break
            else:
                answer = ask_question(user_question, documents)
                print("Chatbot:", answer)
    else:
        print("Failed to fetch document content. Exiting.")


if __name__ == "__main__":
    main()
