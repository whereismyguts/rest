FROM python:3.6

ADD . /project

RUN chmod a+x /project/app/run.sh
EXPOSE 8000
CMD ["/project/app/run.sh"]