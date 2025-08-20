import google.generativeai as genai

genai.configure(api_key="AIzaSyCqjd0KE18CQRf9qRs3Hqj5SkyS7q9Tk-A")

model = genai.GenerativeModel("gemini-1.5-flash")

response = model.generate_content("Write a poem about the ocean.")
print(response.text)
