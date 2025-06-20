FROM python:3.10-slim

WORKDIR /app
COPY . .

# Install kubectl (official Google Cloud method)
RUN apt-get update && \
    apt-get install -y ca-certificates curl && \
    curl -LO "https://dl.k8s.io/release/$(curl -L -s https://dl.k8s.io/release/stable.txt)/bin/linux/amd64/kubectl" && \
    install -o root -g root -m 0755 kubectl /usr/local/bin/kubectl && \
    rm kubectl && \
    # Verify installation
    kubectl version --client && \
    # Install Python dependencies
    pip install --no-cache-dir -r requirements.txt

EXPOSE 7860
CMD ["python", "app.py"]