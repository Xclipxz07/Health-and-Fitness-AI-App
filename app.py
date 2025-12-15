import streamlit as st
import os
from openai import OpenAI
from datetime import datetime
import json
from dotenv import load_dotenv
import google.generativeai as genai

# Load environment variables from .env file
load_dotenv()

# Page configuration
st.set_page_config(
    page_title="AI Health & Fitness Plan Generator",
    page_icon="🏋️‍♂️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for better styling
st.markdown("""
    <style>
    .main-header {
        font-size: 2.5rem;
        font-weight: bold;
        color: #1E88E5;
        text-align: center;
        margin-bottom: 1rem;
    }
    .sub-header {
        font-size: 1.2rem;
        text-align: center;
        color: #666;
        margin-bottom: 2rem;
    }
    .section-header {
        background: linear-gradient(90deg, #1E88E5 0%, #42A5F5 100%);
        color: white;
        padding: 1rem;
        border-radius: 10px;
        margin-top: 1rem;
        margin-bottom: 1rem;
    }
    .info-box {
        background-color: #E3F2FD;
        padding: 1rem;
        border-radius: 10px;
        border-left: 5px solid #1E88E5;
        margin: 1rem 0;
    }
    .stButton>button {
        background-color: #1E88E5;
        color: white;
        font-size: 1.1rem;
        padding: 0.5rem 2rem;
        border-radius: 10px;
        border: none;
        width: 100%;
    }
    .stButton>button:hover {
        background-color: #1565C0;
    }
    </style>
""", unsafe_allow_html=True)

# Initialize OpenAI client
def initialize_openai():
    api_key = os.getenv("OPENAI_API_KEY")
    if api_key:
        return OpenAI(api_key=api_key)
    return None

# Initialize Gemini client
def initialize_gemini():
    api_key = os.getenv("GEMINI_API_KEY")
    if api_key:
        genai.configure(api_key=api_key)
        return genai.GenerativeModel('models/gemini-2.5-flash')
    return None

# Generate personalized health plan
def generate_health_plan(user_profile):
    # Try OpenAI first
    openai_client = initialize_openai()
    gemini_client = initialize_gemini()
    
    if not openai_client and not gemini_client:
        st.error("⚠️ No AI API keys found. Please set OPENAI_API_KEY or GEMINI_API_KEY in your .env file.")
        return None
    
    prompt = f"""
You are an expert AI health and fitness consultant. Generate a comprehensive, personalized health and fitness plan based on the following user profile:

**Personal Information:**
- Name: {user_profile['name']}
- Age: {user_profile['age']}
- Gender: {user_profile['gender']}
- Height: {user_profile['height']} cm
- Current Weight: {user_profile['weight']} kg
- Target Weight: {user_profile['target_weight']} kg

**Health Status:**
- Medical Conditions: {user_profile['conditions']}
- Medications: {user_profile['medications']}
- Allergies: {user_profile['allergies']}

**Lifestyle & Preferences:**
- Dietary Preference: {user_profile['diet_preference']}
- Activity Level: {user_profile['activity_level']}
- Fitness Goals: {user_profile['fitness_goals']}
- Available Time for Exercise: {user_profile['exercise_time']} minutes/day
- Stress Level: {user_profile['stress_level']}

**Additional Notes:**
{user_profile['additional_notes']}

Please provide a detailed, structured plan including:

1. **DIET PLAN** (Tailored to dietary preference and medical conditions)
   - Daily calorie target
   - Macronutrient breakdown
   - Sample meal plan (breakfast, lunch, dinner, snacks)
   - Carb counts and portion sizes (especially if diabetic)
   - Foods to prioritize and avoid
   - Hydration guidelines

2. **WORKOUT ROUTINE** (Safe and progressive)
   - Weekly exercise schedule
   - Specific exercises with sets/reps/duration
   - Warm-up and cool-down routines
   - Progression plan
   - Safety considerations based on medical conditions

3. **LIFESTYLE ADJUSTMENTS**
   - Sleep recommendations
   - Stress management techniques
   - Blood sugar monitoring tips (if diabetic)
   - Medication coordination advice
   - Daily habits to adopt

4. **PROGRESS TRACKING**
   - Key metrics to monitor
   - Recommended tracking frequency
   - Milestones and goals (weekly/monthly)
   - When to adjust the plan

5. **SAFETY PRECAUTIONS & WARNINGS**
   - Important considerations for their specific conditions
   - When to consult healthcare providers
   - Warning signs to watch for

Format the response in clear sections with headers, bullet points, and easy-to-follow instructions. Be specific, practical, and encouraging.
"""

    # Try OpenAI first
    if openai_client:
        try:
            with st.spinner("🤖 AI (OpenAI) is creating your personalized health plan... This may take a moment..."):
                response = openai_client.chat.completions.create(
                    model="gpt-4o",
                    messages=[
                        {"role": "system", "content": "You are an expert health and fitness consultant who creates personalized, safe, and effective health plans. Always prioritize user safety and recommend consulting healthcare professionals for medical conditions."},
                        {"role": "user", "content": prompt}
                    ],
                    temperature=0.7,
                    max_tokens=4000
                )
                return response.choices[0].message.content
        except Exception as e:
            st.warning(f"⚠️ OpenAI failed: {str(e)}. Trying Gemini...")
    
    # Fallback to Gemini
    if gemini_client:
        try:
            with st.spinner("🤖 AI (Gemini) is creating your personalized health plan... This may take a moment..."):
                system_instruction = "You are an expert health and fitness consultant who creates personalized, safe, and effective health plans. Always prioritize user safety and recommend consulting healthcare professionals for medical conditions."
                full_prompt = system_instruction + "\n\n" + prompt
                response = gemini_client.generate_content(full_prompt)
                return response.text
        except Exception as e:
            st.error(f"❌ Gemini also failed: {str(e)}")
            return None
    
    st.error("❌ Both AI services failed. Please check your API keys and try again.")
    return None

# Main app
def main():
    # Header
    st.markdown('<div class="main-header">🏋️‍♂️ AI Health & Fitness Plan Generator</div>', unsafe_allow_html=True)
    st.markdown('<div class="sub-header">Your Personal AI Health & Wellness Assistant</div>', unsafe_allow_html=True)
    
    # Introduction
    st.markdown("""
    <div class="info-box">
    <strong>Welcome!</strong> This AI-powered tool creates personalized health strategies combining:
    <ul>
        <li>✅ Tailored diet plans</li>
        <li>✅ Safe and progressive workout routines</li>
        <li>✅ Lifestyle adjustments for blood sugar control, weight loss & more</li>
        <li>✅ Progress tracking and monitoring guidelines</li>
    </ul>
    </div>
    """, unsafe_allow_html=True)
    
    # Sidebar for user input
    with st.sidebar:
        st.header("📋 Your Health Profile")
        st.write("Fill in your information to get started")
        
        with st.form("health_profile_form"):
            # Personal Information
            st.subheader("Personal Information")
            name = st.text_input("Name", placeholder="Enter your name")
            col1, col2 = st.columns(2)
            with col1:
                age = st.number_input("Age", min_value=10, max_value=100, value=30)
                gender = st.selectbox("Gender", ["Male", "Female", "Other"])
            with col2:
                height = st.number_input("Height (cm)", min_value=100, max_value=250, value=170)
            
            col3, col4 = st.columns(2)
            with col3:
                weight = st.number_input("Current Weight (kg)", min_value=30.0, max_value=300.0, value=70.0, step=0.5)
            with col4:
                target_weight = st.number_input("Target Weight (kg)", min_value=30.0, max_value=300.0, value=65.0, step=0.5)
            
            # Health Status
            st.subheader("Health Status")
            conditions = st.text_area(
                "Medical Conditions",
                placeholder="E.g., Type 1 Diabetes, Hypertension, PCOS, etc.",
                help="List any medical conditions you have"
            )
            medications = st.text_area(
                "Current Medications",
                placeholder="E.g., Insulin, Metformin, etc.",
                help="List any medications you're currently taking"
            )
            allergies = st.text_input(
                "Allergies",
                placeholder="E.g., Peanuts, Shellfish, etc."
            )
            
            # Lifestyle & Preferences
            st.subheader("Lifestyle & Preferences")
            diet_preference = st.selectbox(
                "Dietary Preference",
                ["Vegetarian", "Vegan", "Non-Vegetarian", "Pescatarian", "Keto", "Mediterranean", "No Preference"]
            )
            activity_level = st.select_slider(
                "Current Activity Level",
                options=["Sedentary", "Lightly Active", "Moderately Active", "Very Active", "Extremely Active"]
            )
            fitness_goals = st.multiselect(
                "Fitness Goals",
                ["Weight Loss", "Muscle Gain", "Improve Endurance", "Better Blood Sugar Control", 
                 "Increase Flexibility", "Reduce Stress", "General Health"]
            )
            exercise_time = st.slider(
                "Available Time for Exercise (minutes/day)",
                min_value=0, max_value=180, value=30, step=15
            )
            stress_level = st.select_slider(
                "Stress Level",
                options=["Very Low", "Low", "Moderate", "High", "Very High"]
            )
            
            # Additional Notes
            st.subheader("Additional Information")
            additional_notes = st.text_area(
                "Any other information",
                placeholder="E.g., I work night shifts, I have knee pain, I prefer morning workouts...",
                help="Share any additional information that might help customize your plan"
            )
            
            # Submit button
            submitted = st.form_submit_button("🚀 Generate My Health Plan")
    
    # Main content area
    if submitted:
        # Validate required fields
        if not name:
            st.error("❌ Please enter your name")
            return
        if not conditions and not fitness_goals:
            st.warning("⚠️ Please specify at least your medical conditions or fitness goals")
            return
        
        # Create user profile
        user_profile = {
            'name': name,
            'age': age,
            'gender': gender,
            'height': height,
            'weight': weight,
            'target_weight': target_weight,
            'conditions': conditions if conditions else "None",
            'medications': medications if medications else "None",
            'allergies': allergies if allergies else "None",
            'diet_preference': diet_preference,
            'activity_level': activity_level,
            'fitness_goals': ", ".join(fitness_goals) if fitness_goals else "General Health",
            'exercise_time': exercise_time,
            'stress_level': stress_level,
            'additional_notes': additional_notes if additional_notes else "None"
        }
        
        # Generate plan
        plan = generate_health_plan(user_profile)
        
        if plan:
            # Display success message
            st.success("✅ Your personalized health plan is ready!")
            
            # Display plan
            st.markdown('<div class="section-header"><h2>📋 Your Personalized Health & Fitness Plan</h2></div>', unsafe_allow_html=True)
            
            # Profile summary
            with st.expander("👤 Your Profile Summary", expanded=False):
                col1, col2, col3 = st.columns(3)
                with col1:
                    st.metric("Current Weight", f"{weight} kg")
                    st.metric("Height", f"{height} cm")
                with col2:
                    st.metric("Target Weight", f"{target_weight} kg")
                    st.metric("Weight Goal", f"{weight - target_weight:+.1f} kg")
                with col3:
                    bmi = weight / ((height/100) ** 2)
                    st.metric("Current BMI", f"{bmi:.1f}")
                    st.metric("Age", f"{age} years")
            
            # Display the AI-generated plan
            st.markdown(plan)
            
            # Download option
            st.markdown("---")
            col1, col2, col3 = st.columns([1, 2, 1])
            with col2:
                timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
                filename = f"health_plan_{name.replace(' ', '_')}_{timestamp}.txt"
                st.download_button(
                    label="📥 Download Your Plan",
                    data=plan,
                    file_name=filename,
                    mime="text/plain"
                )
            
            # Important disclaimer
            st.markdown("""
            <div class="info-box" style="background-color: #FFF3E0; border-left: 5px solid #FF9800;">
            <strong>⚠️ Important Disclaimer:</strong><br>
            This plan is generated by AI and is for informational purposes only. It is not a substitute for professional medical advice, diagnosis, or treatment. 
            Always consult with qualified healthcare providers before starting any new diet or exercise program, especially if you have medical conditions.
            </div>
            """, unsafe_allow_html=True)
    
    else:
        # Show instructions when no plan is generated
        st.markdown("---")
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.markdown("### 📝 Step 1")
            st.write("Fill in your health profile in the sidebar")
        
        with col2:
            st.markdown("### 🤖 Step 2")
            st.write("Click 'Generate My Health Plan'")
        
        with col3:
            st.markdown("### 📊 Step 3")
            st.write("Get your personalized plan & track progress")
        
        # Example use case
        st.markdown("---")
        st.markdown("### 💡 Example Use Case")
        st.markdown("""
        <div class="info-box">
        <strong>Meet Jethalal:</strong> Recently diagnosed with Type 1 Diabetes, aiming for weight loss.<br><br>
        <strong>What he got:</strong>
        <ul>
            <li>🍽️ A vegetarian meal guide with carb counts and portion sizes</li>
            <li>🏋️‍♂️ A low-intensity fitness plan with walking, yoga & light strength training</li>
            <li>🧘‍♀️ Stress reduction, glucose monitoring tips, insulin coordination advice</li>
            <li>📈 Progress tracking through HbA1c, weight logs & exercise history</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()
