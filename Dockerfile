FROM python

COPY . /td
RUN pip install -r /td/req.txt

CMD ["pytest", "td"]
