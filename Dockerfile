FROM python:3.11-slim

# Install system dependencies
RUN apt-get update && apt-get install -y     libsndfile1     ffmpeg     git     && rm -rf /var/lib/apt/lists/*

# Create a non-root user for HF Spaces
RUN useradd -m -u 1000 user
USER user
ENV HOME=/home/user     PATH=/home/user/.local/bin:$PATH

WORKDIR /home/user/app

# Copy requirements first
COPY --chown=user requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Patch TTS/utils/io.py to fix "Weights only load failed" error
# Try patching user site-packages first, then system if needed (though we are user now)
RUN SITE_PACKAGES=$(python -c "import site; print(site.getusersitepackages())") &&     if [ -f "$SITE_PACKAGES/TTS/utils/io.py" ]; then         sed -i 's/return torch.load(f, map_location=map_location, \*\*kwargs)/return torch.load(f, map_location=map_location, weights_only=False, \*\*kwargs)/g' "$SITE_PACKAGES/TTS/utils/io.py";     else         echo "Warning: Could not find TTS in user site-packages, checking system...";     fi

# Copy the rest of the application
COPY --chown=user . .

# Create necessary directories
RUN mkdir -p samples output

# Agree to Coqui TOS
ENV COQUI_TOS_AGREED=1

# Expose Gradio port
EXPOSE 7860

# Run the Gradio app
CMD ["python", "app.py"]
