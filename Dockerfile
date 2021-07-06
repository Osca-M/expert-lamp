FROM python:3.8-slim as base
LABEL maintainer="Osca Mwongera <oscamwongera@gmail.com>"
ENV LANG C.UTF-8
ENV LC_ALL C.UTF-8
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONFAULTHANDLER 1

FROM base AS python-deps

RUN pip install pipenv && \
  apt-get update && \
  apt-get install -y --no-install-recommends gcc python3-dev libssl-dev && \
  apt-get remove -y gcc python3-dev libssl-dev && \
  apt-get autoremove -y


COPY Pipfile .
COPY Pipfile.lock .
RUN PIPENV_VENV_IN_PROJECT=1 pipenv install --deploy
RUN pip uninstall pipenv -y

FROM base AS runtime

COPY --from=python-deps /.venv /.venv

ENV PATH="/.venv/bin:$PATH"

RUN adduser --system --group appuser

WORKDIR /home/appuser
RUN mkdir /home/appuser/staticfiles
COPY . .
RUN chown -R appuser:appuser /home/appuser
USER appuser
