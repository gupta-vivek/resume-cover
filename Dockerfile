ARG PYTHON_VERSION=3.11.5
FROM python:${PYTHON_VERSION}-slim as base

WORKDIR /app

# Copy the source code into the container.
COPY . .

RUN pip install -r requirements.txt

# Expose the port that the application listens on.
EXPOSE 8501

# Run the application.
#CMD streamlit run app.py --server.port=8501 --server.address=0.0.0.0
ENTRYPOINT ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]
