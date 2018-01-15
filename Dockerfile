FROM python:2.7
MAINTAINER SCoRe Labs <http://www.scorelab.org/>
ARG BUILD_DATE
ARG VCS_REF
WORKDIR /home/BellyDynamic
COPY . .
RUN chmod +x setup.sh; sync; ./setup.sh; ./install-snap-python.sh;
RUN pip install pandas;
LABEL multi.org.label-schema.name="BellyDynamic" \
      multi.org.label-schema.description="Framework for handling Graphs" \
      multi.org.label-schema.url="https://github.com/scorelab/BellyDynamic/wiki" \
      multi.org.label-schema.vcs-url="https://github.com/scorelab/BellyDynamic" \
      multi.org.label-schema.vcs-ref=$VCS_REF \
      multi.org.label-schema.build-date=$BUILD_DATE \
      multi.org.label-schema.vendor="SCoRe" \
      multi.org.label-schema.version="1.0" \
multi.org.label-schema.schema-version="1.0"
