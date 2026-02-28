import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def generate_morning_script(calendar_data, news_data, weather_data):
    """Uses Llama 3.1 to write the morning script."""
    
    prompt = f"""آپ ایک پروفیشنل مارننگ اسسٹنٹ ہیں۔ مُزمل کے لیے نیچے دیے گئے ڈیٹا کی بنیاد پر ایک مختصر اور جامع اردو بریفنگ تیار کریں:

    ڈیٹا:
        Weather: {weather_data}
        Schedule: {calendar_data}
        News: {news_data}

    ہدایات:
        آغاز: 'گڈ مارننگ مُزمل' سے کریں۔
        ترتیب: پہلے موسم، پھر شیڈول، اور آخر میں خبریں۔
        نیوز سیکشن: خبروں کی تفصیل میں جانے کے بجائے صرف ایک لائن میں اہم ترین خبروں کا خلاصہ (Summary) بتائیں۔
        زبان و انداز: سادہ روزمرہ کی اردو (Urdu Script)۔ کوئی فالتو جملہ یا خوشامد نہ ہو۔
        حد: کل الفاظ 130 سے کم رکھیں تاکہ بریفنگ تیز اور ٹو دی پوائنٹ رہے۔
        اختتام: آخر میں ایک مختصر انگلش موٹیویشنل جملہ لکھیں۔
        شروع کریں: 'گڈ مارننگ مُزمل،"""
    try:
        completion = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=[
                {"role": "system", "content": "You are a helpful and poetic morning assistant."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.7,
            max_tokens=300
        )
        return completion.choices[0].message.content
    except Exception as e:
        return f"Error generating script: {str(e)}"