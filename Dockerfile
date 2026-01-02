FROM python:3.11-slim

# Install system dependencies
# libsndfile1 is required for soundfile
# ffmpeg is often required for audio processing
# git is required if installing from git repositories
RUN apt-get update && apt-get install -y \
    libsndfile1 \
    ffmpeg \
    git \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Copy requirements first to leverage cache
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Patch TTS/utils/io.py to fix "Weights only load failed" error
# We force weights_only=False in torch.load calls
RUN SITE_PACKAGES=$(python -c "import site; print(site.getsitepackages()[0])") && \
    sed -i 's/return torch.load(f, map_location=map_location, \*\*kwargs)/return torch.load(f, map_location=map_location, weights_only=False, \*\*kwargs)/g' $SITE_PACKAGES/TTS/utils/io.py

# Copy the rest of the application
COPY . .

# Create necessary directories
RUN mkdir -p samples output

# Default command
CMD ["python", "interactive_tts.py"]
