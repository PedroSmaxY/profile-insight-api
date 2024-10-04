FROM python:3.12-slim

WORKDIR /app

# Update and install essential packages
RUN apt-get update && \
    apt-get install -y \
    git \
    wget \
    build-essential \
    libffi-dev \
    libssl-dev \
    zlib1g-dev \
    cmake \
    ninja-build \
    texinfo \
    docbook-xsl \
    && rm -rf /var/lib/apt/lists/*

# Add sources.list if not present or incorrect
RUN echo "deb https://deb.debian.org/debian/ bullseye main" > /etc/apt/sources.list && \
    echo "deb-src https://deb.debian.org/debian/ bullseye main" >> /etc/apt/sources.list

# Update and install build dependencies for SWI-Prolog
RUN apt-get update && \
    apt-get build-dep -y swi-prolog

# Clone SWI-Prolog source code, checkout the specific commit, and initialize submodules
RUN git clone https://github.com/SWI-Prolog/swipl-devel.git && \
    cd swipl-devel && \
    git checkout 7b085198f1df07f848c304e284835ac9dddf3183 && \
    git submodule update --init --recursive

# Build and install SWI-Prolog
RUN cd swipl-devel && \
    mkdir build && \
    cd build && \
    cmake -DCMAKE_INSTALL_PREFIX=/usr/local -DCMAKE_BUILD_TYPE=Release -G Ninja .. && \
    ninja && \
    ctest -j $(nproc) --output-on-failure && \
    ninja install

# Copy application code
COPY . /app

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
