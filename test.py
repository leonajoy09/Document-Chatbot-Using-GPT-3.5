import os
import openai

# Set up OpenAI API key
openai.api_key = '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'

# Function to read text from all .txt files in the "documents" folder


def read_documents(folder_path):
    documents = []
    for file_name in os.listdir(folder_path):
        if file_name.endswith('.txt'):
            file_path = os.path.join(folder_path, file_name)
            with open(file_path, 'r', encoding='utf-8') as file:
                documents.append(file.read())
    return documents

# Function to ask questions and get answers from GPT-3.5


def ask_question(question, documents):
    prompt = f"Question: {question}\nContext:\n" + '\n'.join(documents)
    response = next(openai.Completion.create(
        engine="davinci-002", prompt=prompt, max_tokens=150))
    return response.choices[0].text.strip()

# Main function


def main():
    documents_folder = "documents"
    documents = read_documents(documents_folder)

    print("Welcome to the Document Chatbot!")
    while True:
        user_question = input("You: ")
        if user_question.lower() == 'exit':
            print("Exiting the chatbot.")
            break
        else:
            answer = ask_question(user_question, documents)
            print("Chatbot:", answer)


if __name__ == "__main__":
    main()
