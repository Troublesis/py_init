# Use Alpine as the base image for a smaller footprint
FROM python:3.9-alpine as builder

# Set environment variables
ENV PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=off \
    PIP_DISABLE_PIP_VERSION_CHECK=on \
    POETRY_VERSION=1.8.3

# Install poetry and dependencies
RUN apk add --no-cache gcc musl-dev libffi-dev \
    && pip install --no-cache-dir "poetry==$POETRY_VERSION"

# Set working directory
WORKDIR /app

# Copy only dependency files
COPY pyproject.toml poetry.lock ./

# Install project dependencies
RUN poetry config virtualenvs.create false \
    && poetry install --no-dev --no-interaction --no-ansi

# Copy source code
COPY ./app /app

# Production stage
# FROM python:3.9-alpine as production
FROM python:3.9-alpine as development

# Set working directory
WORKDIR /app

# Copy only necessary files from builder
COPY --from=builder /usr/local/lib/python3.9 /usr/local/lib/python3.9
COPY --from=builder /app /app

RUN mkdir -p /app/logs && chmod -R a+w /app/logs

# Set environment variables
ENV PORT=8000

# Expose port
EXPOSE $PORT

# Create and switch to non-root user
RUN adduser -D appuser
USER appuser

# Run the application
CMD ["python", "main.py"]