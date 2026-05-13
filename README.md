# 🏋️‍♂️ AI Health & Fitness Plan Generator

An AI-powered health and fitness planning tool that creates personalized wellness strategies using OpenAI's GPT-4, Google's Gemini, and local Ollama models with Streamlit. This application combines tailored diet plans, safe workout routines, and lifestyle adjustments to support various health goals including blood sugar control, weight loss, muscle gain, and overall wellness.

> **NEW**: Explicit AI provider selection including local model support via Ollama!

---

## ⚡ Quick Start (5 minutes)

```bash
# 1. Install dependencies
pip install -r requirements.txt

# 2. Set up API keys (optional - skip if using Ollama)
# Create .env file with your API keys (see instructions below)

# 3. Run the app
streamlit run app.py

# 4. Open browser at http://localhost:8501
```

---

## 📋 Prerequisites

Choose ONE of the following:

- **Option 1**: [OpenAI API Key](https://platform.openai.com/api-keys) (requires paid account)
- **Option 2**: [Google Gemini API Key](https://aistudio.google.com/app/apikey) (FREE)
- **Option 3**: [Local Ollama](https://ollama.com/) instance (FREE & Private)

**Also Required**: Python 3.8 or higher

---

## 🔧 Installation Steps

### 1. Clone or Download Repository
```bash
cd /path/to/Health-and-Fitness-AI-App
```

### 2. Install Required Packages
```bash
pip install -r requirements.txt
```

### 3. Set Up API Keys (If Using Cloud Providers)

Create a `.env` file in the project directory:

```bash
cp .env.example .env
```

Then edit `.env` and add your API key(s):

```
OPENAI_API_KEY=sk-your-actual-key-here
GEMINI_API_KEY=your-gemini-key-here
```

**Note**: You can add one or both. If using Ollama, you don't need any API keys!

### 4. (Optional) Set Up Local Ollama

If you prefer privacy, use local models instead:

```bash
# Install Ollama from https://ollama.com/
# Then in terminal, run a model (e.g., llama2):
ollama run llama2
# Keep this terminal running while using the app
```

---

## 🚀 Running the App

```bash
streamlit run app.py
```

The app will automatically open in your browser at `http://localhost:8501`

**Troubleshooting**: 
- If browser doesn't open, manually visit `http://localhost:8501`
- If port 8501 is busy, Streamlit will use 8502, 8503, etc.

---

## 📖 How to Use

1. **Fill in Your Health Profile**
   - Enter personal information (name, age, height, weight)
   - List any medical conditions
   - Specify dietary preferences and fitness goals

2. **Select AI Provider** (from sidebar)
   - Choose OpenAI, Gemini, or Ollama
   - If using Ollama, select which model to use

3. **Generate Your Plan**
   - Click "🚀 Generate My Health Plan"
   - Wait 30-60 seconds for AI to create plan

4. **Download & Save**
   - Download your personalized plan as text file
   - Follow the recommendations
   - Track your progress

---

## ✨ Features

- **🤖 Multi-AI Support**: Choose explicitly between OpenAI GPT-4, Google Gemini, or connect your local Ollama instance for privacy-focused local generation.
- **🍽️ Personalized Diet Plans**: Custom meal plans with calorie targets, macronutrient breakdowns, and portion sizes
- **🏋️‍♂️ Progressive Workout Routines**: Safe exercise schedules tailored to fitness level and medical conditions
- **🧘‍♀️ Lifestyle Adjustments**: Stress management, sleep optimization, and health monitoring tips
- **📈 Progress Tracking**: Key metrics, milestones, and tracking guidelines
- **🩺 Medical Condition Support**: Special considerations for diabetes, PCOS, hypertension, and more
- **🥗 Dietary Preferences**: Support for vegetarian, vegan, keto, Mediterranean, and other diets
- **📥 Downloadable Plans**: Export your personalized plan as a text file

## 🚀 Quick Start

### Prerequisites

- Python 3.8 or higher
- OpenAI API key ([Get one here](https://platform.openai.com/api-keys)) **OR**
- Google Gemini API key ([Get FREE key here](https://aistudio.google.com/app/apikey)) **OR**
- A local [Ollama](https://ollama.com/) instance running with pulled models (e.g., `ollama run llama3`).

### Installation

1. **Clone or download this repository**

2. **Install required packages**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up your API keys**
   
   Create a `.env` file in the project directory:
   ```bash
   cp .env.example .env
   ```
   
   Then edit `.env` and add your API key(s):
   ```
   OPENAI_API_KEY=sk-your-actual-api-key-here
   GEMINI_API_KEY=your-gemini-api-key-here
   ```
   
   **Note**: You can use either API key, or completely skip API keys if you plan to use local models via Ollama.

4. **Run the application**
   ```bash
   streamlit run app.py
   ```

5. **Open your browser**
   
   The app will automatically open at `http://localhost:8501`

## 📖 How to Use

1. **Fill in Your Health Profile**
   - Enter personal information (name, age, height, weight)
   - List any medical conditions and medications
   - Specify dietary preferences and fitness goals
   - Set your activity level and available exercise time

2. **Generate Your Plan**
   - Click "🚀 Generate My Health Plan"
   - Wait for the AI to create your personalized plan (usually 30-60 seconds)

3. **Review Your Plan**
   - Read through your customized diet plan
   - Review the workout routine
   - Note lifestyle adjustments and safety precautions

4. **Download & Track**
   - Download your plan for offline reference
   - Follow the progress tracking guidelines
   - Adjust as needed based on your results

## 💡 Example Use Cases

### Case 1: Type 1 Diabetes Management
**Profile**: 40 years old Uncle Ayush, recently diagnosed with Type 1 Diabetes, wants to lose weight

**Plan Includes**:
- Vegetarian meal guide with detailed carb counts
- Low-intensity fitness plan (walking, yoga, light strength training)
- Glucose monitoring tips and insulin coordination advice
- Progress tracking through HbA1c and weight logs

### Case 2: Weight Loss & Fitness
**Profile**: Sayani, 32 years old, sedentary lifestyle, wants to lose 10kg and improve fitness

**Plan Includes**:
- Calorie-controlled Mediterranean diet
- Progressive workout routine (cardio + strength training)
- Stress management and sleep optimization
- Weekly weight and measurement tracking

### Case 3: Muscle Gain
**Profile**: Raj, 25 years old, wants to build muscle while staying healthy

**Plan Includes**:
- High-protein diet with meal timing
- Structured strength training program
- Recovery and rest guidelines
- Progress tracking through measurements and strength gains

## ⚙️ Configuration

### AI Model Selection

The app allows selecting your preferred provider from the sidebar:
- **OpenAI**: Uses `gpt-4o`
- **Gemini**: Uses `gemini-2.5-flash`
- **Ollama**: Connects to your local instance (default `http://localhost:11434`) and lets you choose from any downloaded local models.

You can modify the default cloud models in [app.py](app.py):
```python
# OpenAI model
model="gpt-4o"  # Change to "gpt-3.5-turbo" for faster/cheaper

# Gemini model
genai.GenerativeModel('models/gemini-2.5-flash')  # Change to other Gemini models
```

### Adjusting Plan Details

Modify the prompt in the `generate_health_plan()` function to customize the output format or add specific requirements.

## 🛡️ Safety & Disclaimer

⚠️ **Important**: This application is for informational purposes only and does not provide medical advice. Always consult with qualified healthcare providers before starting any new diet or exercise program, especially if you have medical conditions.

The AI-generated plans should be reviewed by healthcare professionals, particularly for users with:
- Chronic medical conditions (diabetes, heart disease, etc.)
- Taking prescription medications
- Pregnant or nursing
- History of eating disorders
- Recent injuries or surgeries

## 🔒 Privacy & Security

- By default, user data is processed locally and sent only to AI APIs (OpenAI/Gemini).
- If using **Ollama**, no data leaves your local machine, ensuring 100% privacy!
- No user information is stored on servers.
- Your API keys should be kept confidential and never shared.
- Consider the privacy implications of sharing personal health data if using cloud providers.

## 📋 Requirements

- Python 3.8+
- streamlit 1.31.0+
- openai 1.12.0+
- google-generativeai 0.3.2+
- python-dotenv 1.0.0+
- requests 2.31.0+

## 🤝 Contributing

Contributions are welcome! Feel free to:
- Report bugs
- Suggest new features
- Improve documentation
- Submit pull requests

## 📄 License

This project is open source and available under the MIT License.

## 💬 Support

If you encounter issues:
1. Check that at least one API key (OpenAI or Gemini) is correctly set, or Ollama is running.
2. Ensure all dependencies are installed: `pip install -r requirements.txt`
3. Verify you have an active internet connection (if using Cloud Providers).
4. For Ollama: ensure it is running (`ollama serve`) and accessible at the provided URL.
5. Check API status: [OpenAI Status](https://status.openai.com/) | [Google AI Status](https://status.cloud.google.com/)

## 🙏 Acknowledgments

- Built with [Streamlit](https://streamlit.io/)
- Powered by [OpenAI GPT-4](https://openai.com/) and [Google Gemini](https://ai.google.dev/)
- Inspired by the need for accessible, personalized health guidance



**Built with ❤️ for better health and wellness from Apex Innovations**
**Intelligence at its peak, Privacy at its core**
#BuiltInPublic


Made possible by AI technology - helping people make informed health decisions with personalized guidance.
