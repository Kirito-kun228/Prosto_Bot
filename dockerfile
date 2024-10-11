FROM python:3.10-slim

WORKDIR /app

COPY . /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

RUN apt-get update && apt-get install -y supervisor

COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf

ENV TOKEN1=<7385831828:AAGNszlS1Li2akyA6P7epQxWIm9FWgJofsE>
ENV TOKEN2=<7923492157:AAERxZ22SmVCaLXISyUhp1NwplZujU8Dhko>

EXPOSE 5000

CMD ["/usr/bin/supervisord"]
