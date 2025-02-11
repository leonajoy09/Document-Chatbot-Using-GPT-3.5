This project is a Document Chatbot designed to assist users by fetching content from online documents (in PDF format), extracting relevant text, and enabling question-answer interactions through the GPT-3.5 (Davinci-002) model from OpenAI. The chatbot processes user queries by referring to the content extracted from the PDF file, providing accurate answers based on the given document.

**Key Features**
1. Document Fetching
Downloads PDF content from a user-specified URL.
Ensures successful document retrieval with error handling for download failures.

2. Text Extraction
Utilizes PyPDF2 to read and extract textual data from the fetched PDF content.

3. Natural Language Processing with GPT-3.5
Uses OpenAI’s Davinci-002 model to process user questions.
Answers queries based on the context of the document text.

4. Interactive Chat Interface
Simple command-line chatbot interface for user interactions.
Type "exit" to terminate the chatbot session.

**How It Works**
The program fetches and reads a document from the specified PDF URL.
Extracted text is stored for context reference.
The user asks questions, and the chatbot responds using GPT-3.5 with contextual answers.
The chatbot continues until the user exits by typing "exit."
