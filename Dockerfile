FROM python:3.13.1-bookworm

# Install Poetry
RUN pip install poetry

WORKDIR /app

# Copy poetry config and lock files first (for caching dependencies)
COPY pyproject.toml poetry.lock /app/

# Install dependencies without dev packages
RUN poetry config virtualenvs.create false \
    && poetry install --no-root --no-interaction --no-ansi

# Copy rest of the code
COPY . /app

CMD ["poetry", "run", "python", "main.py"]
