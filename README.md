This is a simple AI Chatbot built using Python, Streamlit, and the OpenAI API. The chatbot allows users to interact with an AI model to get responses in a conversational format.

Features

	•	Interactive Chat Interface: A user-friendly chat interface created with Streamlit.
	•	OpenAI API Integration: Utilizes the OpenAI API to generate responses based on user input.
	•	Real-time Communication: Immediate responses to user queries.
	•	Customizable: Easy to modify the bot’s behavior by tweaking the API settings and conversation logic.

Installation

To run this project locally, follow these steps:

	1.	Clone the repository:


	2.	Set up a virtual environment (optional but recommended):
      python -m venv venv
source venv/bin/activate   # On Windows use `venv\Scripts\activate`

	3.	Install the required packages:
 pip install -r requirements.txt

 	4.	Add your OpenAI API key:
Create a .env file in the root directory of the project and add your OpenAI API key:
OPENAI_API_KEY=your-openai-api-key

Usage

To run the chatbot locally, use the following command:
streamlit run app.py

Key Files

	•	app.py: The main application file containing the Streamlit code.
	•	Mybot.py: Contains the logic for interacting with the OpenAI API and processing user input.
	•	requirements.txt: Lists all the dependencies required to run the application.

Customization

To customize the chatbot’s behavior, you can modify the following:

	•	API Settings: In chatbot.py, you can tweak the API call parameters like temperature, max_tokens, etc., to alter the responses.
	•	UI/UX: Modify app.py to adjust the Streamlit interface to your preference.

Deployment

You can deploy this Streamlit app to platforms like Heroku, Streamlit Cloud, or any other cloud platform that supports Python applications.

Contributing

Feel free to fork this repository, make improvements, and submit a pull request. Any contributions are welcome!

License

This project is licensed under the MIT License. See the LICENSE file for more details.

Acknowledgments

	•	Special thanks to the Streamlit and OpenAI teams for providing powerful tools that make building AI applications easier.
