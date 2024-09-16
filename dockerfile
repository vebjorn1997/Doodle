FROM ubuntu

# Install ImageMagick and Ghostscript (required for handling .ps files)
RUN apt-get update && apt-get install -y \
    ghostscript \
    imagemagick \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY . /app

ENTRYPOINT [ "convert" ]