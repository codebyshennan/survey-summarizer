# Define required macros here
SHELL = /bin/sh

appl:
	source .env && poetry run streamlit run ./app/app.py