# Define required macros here
SHELL = /bin/sh

dev:
	source .env && poetry run streamlit run ./app/main.py

prod:
	poetry run streamlit run ./app/main.py