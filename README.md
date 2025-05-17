

---

````markdown
# 🚗 Car Specification Chatbot (LangGraph + OpenAI GPT-3.5)

A simple command-line chatbot that provides detailed specifications for car models using the power of [LangGraph](https://github.com/langchain-ai/langgraph) and OpenAI's `gpt-3.5-turbo`.

---

## 📋 Features

- Ask about any car model (e.g., **"Tell me about Hyundai Ioniq 5"**)
- Get a structured response including:
  - Engine type
  - Fuel efficiency
  - Top speed
  - Key features
  - Approximate price
- Powered by OpenAI GPT-3.5 and LangGraph for stateful reasoning

---

## 📦 Installation

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/car-spec-chatbot.git
cd car-spec-chatbot
````

### 2. Create and activate a virtual environment (optional but recommended)

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Set your OpenAI API Key

You can set it as an environment variable:

```bash
export OPENAI_API_KEY="your-api-key"  # On Windows use `set`
```

Or directly replace `"YOUR_OPENAI_API_KEY"` in the code (not recommended for production).

---

## 🚀 Usage

Run the chatbot from the terminal:

```bash
python main.py
```

You’ll see:

```
🚗 Car Specification Chatbot (LangGraph + GPT-3.5)
Type 'exit' to quit.
```

Then ask questions like:

```
> Tell me about Tesla Model S
```

---

## 📂 Project Structure

```
car-spec-chatbot/
│
├── main.py              # Main chatbot logic
├── requirements.txt     # Python dependencies
└── README.md            # Project documentation
```

---

## 🧠 How It Works

* **LangGraph** defines a simple state machine with a single node: `get_specs`.
* The node takes a user's car query, builds a prompt, and sends it to **OpenAI GPT-3.5**.
* The model responds with a structured car specification summary.

---

## 📌 Requirements

* Python 3.8+
* [OpenAI Python SDK](https://github.com/openai/openai-python)
* [LangGraph](https://github.com/langchain-ai/langgraph)

---


---

## ✨ Example Output

**Input:**
`Tell me about Toyota Prius`

**Output:**

```
📋 Car Specifications:

Model: Toyota Prius  
Engine Type: 1.8L 4-cylinder hybrid  
Fuel Efficiency: Approx. 58 MPG (city) / 53 MPG (highway)  
Top Speed: ~112 mph  
Key Features: Hybrid Synergy Drive, touchscreen infotainment, adaptive cruise control  
Price Range: $25,000 - $32,000

---
```

```

---

```
