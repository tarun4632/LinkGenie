# LinkGenie

LinkGenie is a powerful URL analyzer built using Streamlit and LangChain. It allows users to input multiple URLs, process their content, and ask questions about the information contained within those web pages.

![LinkGenie Screenshot](https://raw.githubusercontent.com/yourusername/URLGenie/main/linkgenie_screenshot.png)

## Features

- Process up to 3 URLs simultaneously
- Extract and analyze content from web pages
- Ask questions about the processed content
- Get answers with source citations
- Dark mode interface for comfortable viewing

## Project Structure

```
URLGenie/
├── OpenAI_Project/
│   ├── requirements.txt
│   ├── .env
│   └── main.py
├── Gemma_Project/
│   ├── requirements.txt
│   └── main.py
├── linkgenie_screenshot.png
└── README.md
```

## Setup and Installation

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/URLGenie.git
   cd URLGenie
   ```

2. Set up the OpenAI Project:
   ```
   cd OpenAI_Project
   pip install -r requirements.txt
   ```
   Create a `.env` file and add your OpenAI API key:
   ```
   OPENAI_API_KEY=your_api_key_here
   ```

3. Set up the Gemma Project:
   ```
   cd ../Gemma_Project
   pip install -r requirements.txt
   ```

## Usage

1. To run the OpenAI version:
   ```
   cd OpenAI_Project
   streamlit run app.py
   ```

2. To run the Gemma version:
   ```
   cd Gemma_Project
   streamlit run app.py
   ```

3. Open your web browser and navigate to the provided local URL (usually `http://localhost:8501`).

4. Enter up to 3 URLs in the sidebar and click "Process URLs".

5. Once processing is complete, ask questions about the content in the main input field.

## Technologies Used

- Streamlit
- LangChain
- OpenAI GPT-3.5 Turbo (for OpenAI Project)
- FAISS for vector storage and retrieval
- SentenceTransformers (for Gemma Project)

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License.
