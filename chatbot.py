from dotenv import load_dotenv
import os
import httpx
import pickle
import time
load_dotenv()


API_URL = "https://router.huggingface.co/hf-inference/models/deepset/roberta-base-squad2"

hf_token = os.getenv("HF_TOKEN")

if not hf_token:
    hf_token = input("Enter HuggingFace API Token: ")


headers = {
    "Authorization": f"Bearer {hf_token}"
}


with open("data_store.pkl", "rb") as file:
    stored_data = pickle.load(file)

website_context = stored_data.get("context", "")

# Function to ask question
def ask_question(question, context):

    payload = {
        "inputs": {
            "question": question,
            "context": context[:5000]
        }
    }

    response = httpx.post(
        API_URL,
        headers=headers,
        json=payload,
        timeout=60
    )

    return response.json()

print("\n" + "=" * 50)
print("ChatBOT READY")
print("=" * 50)

while True:

    user_question = input("\nAsk Question: ")

    if user_question.lower() == "exit":
        print("\nExiting chatbot...")
        break

    try:

        output = ask_question(
            user_question,
            website_context
        )

        if "estimated_time" in output:

            print(f"\nModel loading... Please wait {output['estimated_time']} seconds")

            time.sleep(output["estimated_time"])

            output = ask_question(
                user_question,
                website_context
            )

        answer = output.get("answer", "No answer found.")


        print(f"\nAnswer: {answer}")

        print("\n" + "=" * 50)

    except Exception as e:

        print("Error:", e)
