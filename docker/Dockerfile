FROM docker.io/python:3 as BUILD

ENV VIRTUAL_ENV=/opt/venv PYTHONUNBUFFERED=1

RUN python3 -m venv "$VIRTUAL_ENV"
# from now all calls to python/pip will use
# binaries from #VIRTUAL_ENV/bin
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

COPY requirements.txt .

RUN pip install -Ur requirements.txt && \
    pip install RPi.GPIO lgpio rpio pigpio

# Runner
FROM docker.io/python:3-slim

ENV VIRTUAL_ENV=/opt/venv PYTHONUNBUFFERED=1 PYTHONPATH=/app
ENV PATH="$VIRTUAL_ENV/bin:$PATH"
WORKDIR /app

COPY --from=BUILD "$VIRTUAL_ENV" "$VIRTUAL_ENV"
COPY . /app

ENTRYPOINT ["python3", "docker/run.py"]
