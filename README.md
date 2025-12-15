# 🏋️‍♂️ AI Health & Fitness Plan Generator

An AI-powered health and fitness planning tool that creates personalized wellness strategies using OpenAI's GPT-4 and Google's Gemini with Streamlit. This application combines tailored diet plans, safe workout routines, and lifestyle adjustments to support various health goals including blood sugar control, weight loss, muscle gain, and overall wellness.

**NEW**: Automatic fallback from OpenAI to Gemini ensures your app always works!

## ✨ Features

- **🤖 Dual AI Support**: Uses OpenAI GPT-4 first, automatically falls back to Google Gemini if needed
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
- Google Gemini API key ([Get FREE key here](https://aistudio.google.com/app/apikey))
- **Recommended**: Both API keys for automatic fallback

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
   
   **Note**: You can use either one or both. The app tries OpenAI first, then falls back to Gemini.

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
**Profile**: Maria, 32 years old, sedentary lifestyle, wants to lose 10kg and improve fitness

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

The app uses:
- **Primary**: OpenAI GPT-4 (`gpt-4o`)
- **Fallback**: Google Gemini (`gemini-2.5-flash`)

You can modify the models in [app.py](app.py):
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

- All user data is processed locally and sent only to AI APIs (OpenAI/Gemini)
- No user information is stored on servers
- Your API keys should be kept confidential and never shared
- Consider the privacy implications of sharing personal health data
- The app automatically switches between AI providers based on availability

## 📋 Requirements

- Python 3.8+
- streamlit 1.31.0+
- openai 1.12.0+
- google-generativeai 0.3.2+
- python-dotenv 1.0.0+

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
1. Check that at least one API key (OpenAI or Gemini) is correctly set
2. Ensure all dependencies are installed: `pip install -r requirements.txt`
3. Verify you have an active internet connection
4. If OpenAI fails, the app will automatically try Gemini
5. Check API status: [OpenAI Status](https://status.openai.com/) | [Google AI Status](https://status.cloud.google.com/)

## 🙏 Acknowledgments

- Built with [Streamlit](https://streamlit.io/)
- Powered by [OpenAI GPT-4](https://openai.com/) and [Google Gemini](https://ai.google.dev/)
- Inspired by the need for accessible, personalized health guidance

## 📊 Screenshots

### Main Interface
![Main Interface - User inputs health profile in sidebar and receives personalized plan]

### Generated Plan
![Sample Plan - Complete diet, workout, and lifestyle recommendations]

---

**Built with ❤️ for better health and wellness**

Made possible by AI technology - helping people make informed health decisions with personalized guidance.
