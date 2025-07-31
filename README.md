<h1>📘 Ask Your PDF – AI-powered Q&A with PDF Files</h1>

<p>
A simple and interactive web app built using <strong>Streamlit</strong> and <strong>OpenAI's GPT</strong> that allows you to upload a PDF document and <strong>ask questions about its content</strong>.
This tool uses <code>PyMuPDF</code> to extract text and then leverages GPT (via OpenAI's API) to understand and answer user queries based on the PDF context.
</p>

<hr>

<h2>🚀 Features</h2>
<ul>
  <li>✅ Upload any <strong>PDF document</strong></li>
  <li>✅ Extract full text content from the PDF</li>
  <li>✅ Ask <strong>natural language questions</strong> about the content</li>
  <li>✅ Receive intelligent, context-aware answers using <strong>OpenAI's GPT engine</strong></li>
  <li>✅ Clean and simple <strong>Streamlit UI</strong></li>
</ul>

<hr>

<h2>🛠️ Tech Stack</h2>
<ul>
  <li><a href="https://streamlit.io/">Streamlit</a> – for building the UI</li>
  <li><a href="https://platform.openai.com/docs">OpenAI GPT (Codex)</a> – for generating answers</li>
  <li><a href="https://pymupdf.readthedocs.io/en/latest/">PyMuPDF (fitz)</a> – for extracting text from PDF</li>
  <li><a href="https://www.python.org/">Python</a> – as the programming language</li>
</ul>

<hr>

<h2>📷 Demo</h2>
<p>
  <img src="https://user-images.githubusercontent.com/yourusername/demo.gif" alt="App Demo" />
</p>
<p><em>(Add your own GIF or screenshot of the app in action)</em></p>

<hr>

<h2>📂 How It Works</h2>
<ol>
  <li><strong>Upload a PDF</strong> through the Streamlit interface.</li>
  <li>The app extracts all textual content using <code>PyMuPDF</code>.</li>
  <li>You type a <strong>question</strong> related to the content of the PDF.</li>
  <li>The app sends the full text and your question to OpenAI's API.</li>
  <li>GPT processes it and responds with an intelligent answer.</li>
</ol>

<hr>

<h2>🔧 Setup & Installation</h2>

<pre><code>git clone https://github.com/yourusername/ask-your-pdf.git
cd ask-your-pdf

# (Optional) Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Add your OpenAI API key in the script

# Run the Streamlit app
streamlit run app.py
</code></pre>

<hr>

<h2>🧠 Example Use Cases</h2>
<ul>
  <li>Academic research papers – ask about key findings</li>
  <li>Legal documents – query specific clauses or terms</li>
  <li>Business reports – extract insights quickly</li>
  <li>Any lengthy document – get instant, summarized answers</li>
</ul>

<hr>

<h2>📌 Notes</h2>
<ul>
  <li>Make sure to use a valid OpenAI API key.</li>
  <li>The app uses the <strong>Davinci Codex engine</strong>; you can change it to other models like <code>gpt-3.5-turbo</code> if needed.</li>
  <li>Large PDFs may take time to process and may incur higher token costs with OpenAI API.</li>
</ul>

<hr>

<h2>📃 License</h2>
<p>
  MIT License. See <a href="LICENSE">LICENSE</a> for more details.
</p>

<hr>

<h2>🙌 Contributing</h2>
<p>
  Contributions, ideas, and suggestions are welcome! Feel free to fork this project and submit a PR.
</p>

<hr>

<h2>📬 Contact</h2>
<p>
  For feedback or questions, reach out via GitHub Issues or connect on <a href="https://linkedin.com/in/yourprofile">LinkedIn</a>.
</p>
