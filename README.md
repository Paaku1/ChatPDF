# ChatPDF Reader - A Streamlit Application for PDF Content Extraction with OpenAI GPT-3


ChatPDF Reader is a user-friendly web application that harnesses the power of OpenAI's GPT-3 language model and Streamlit to simplify the process of extracting and summarizing content from PDF documents. This project streamlines the experience of working with PDFs by allowing users to interact with a conversational AI interface to extract text, generate summaries, and more.

## Table of Contents

- [Getting Started](#getting-started)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)

## Getting Started

ChatPDF Reader is designed to be easy to set up and use. Follow these steps to get started:

### Prerequisites

Before running ChatPDF Reader, ensure you have the following prerequisites installed:

- Python 3.x
- pip (Python package manager)
- OpenAI API key (Sign up at [OpenAI](https://beta.openai.com/signup/) if you don't have one)
- Poppler (for PDF processing)

### Installation

1. Clone the ChatPDF Reader repository to your local machine:

   ```bash
   git clone https://github.com/yourusername/chatPDF-reader.git
   ```

2. Navigate to the project directory:

   ```bash
   cd chatPDF-reader
   ```

3. Create a virtual environment (optional but recommended):

   ```bash
   python -m venv venv
   ```

4. Activate the virtual environment:

   - On Windows:

     ```bash
     venv\Scripts\activate
     ```

   - On macOS and Linux:

     ```bash
     source venv/bin/activate
     ```

5. Install the required Python packages:

   ```bash
   pip install -r requirements.txt
   ```

6. Install Poppler for PDF processing. Instructions vary depending on your operating system, so please follow the relevant installation guide:

   - [Poppler Installation Guide for Windows](https://stackoverflow.com/a/55777185)
   - [Poppler Installation Guide for macOS](https://stackoverflow.com/a/47372678)
   - [Poppler Installation Guide for Linux](https://poppler.freedesktop.org/)

7. Configure your OpenAI API key:

   Create a `.env` file in the project directory and add your API key:

   ```
   OPENAI_API_KEY=your-api-key-here
   ```

8. Start the Streamlit application:

   ```bash
   streamlit run app.py
   ```

The ChatPDF Reader application should now be running locally and accessible in your web browser.

## Usage

1. Open your web browser and navigate to [http://localhost:8501](http://localhost:8501).

2. You will be greeted with the ChatPDF Reader interface, which resembles a chatbot.

3. Start a conversation by typing your instructions in plain English. For example:

   ```
   Extract text from the PDF document located at "example.pdf."
   Summarize the extracted content.
   ```

4. The chatbot will respond with the extracted text and a summary.

5. Download the extracted text or summary as needed.

## Contributing

We welcome contributions to improve ChatPDF Reader. To contribute, follow these steps:

1. Fork the repository on GitHub.

2. Clone your forked repository to your local machine.

3. Create a new branch for your feature or bug fix.

4. Make your changes and commit them with descriptive commit messages.

5. Push your changes to your forked repository on GitHub.

6. Create a pull request to the main ChatPDF Reader repository.

We appreciate your contributions!
