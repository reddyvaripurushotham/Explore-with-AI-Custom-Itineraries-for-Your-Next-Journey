import google.generativeai as genai

genai.configure(api_key=("AIzaSyCJkeZgZteVWeimEor_nWwAPcMoCab8sUI")

model = genai.GenerativeModel("gemini-pro")

response = model.generate_content("Plan a 3 day trip to Goa")

print(response.text)