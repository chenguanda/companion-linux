FROM python:3.7-alpine

COPY dist/*.whl /
RUN pip install /*.whl
