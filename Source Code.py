from google import genai

# Add your API key here
API_KEY = "YOUR_API_KEY"

client = genai.Client(api_key=API_KEY)


def generate_travel_guide(destination, days):
    """
    Generates a travel itinerary using Gemini model.
    """

    prompt = f"""
    Create a detailed {days}-day travel itinerary for {destination}.
    Include:
    - Morning plan
    - Afternoon plan
    - Evening plan
    - Suggested food
    - Travel tips
    """

    response = client.models.generate_content(
        model="gemini-1.5-pro",
        contents=prompt
    )

    return response.text


if __name__ == "__main__":
    print("===== AI Travel Planner =====")
    destination = input("Enter Destination: ")
    days = input("Enter Number of Days: ")

    result = generate_travel_guide(destination, days)

    print("\n===== Generated Travel Plan =====\n")
    print(result)
