# GitHub Actions container to support doing and build config automatically upon a push
FROM python:3.8-slim

RUN apt-get update \
    && apt-get install -y --no-install-recommends git \
    && apt-get purge -y --auto-remove \
    && rm -rf /var/lib/apt/lists/*

# installs python packages we'd want for unit testing
#RUN pip install \
#              numpy \
#              matplotlib \
#              scipy

LABEL "name"="McCoyGroup/build-site"
LABEL "maintainer"="Mark Boyer <b3m2a1uw.edu>"
LABEL "version"="0.0.1"

LABEL "com.github.actions.name"="McCoy Group Site Builder"
LABEL "com.github.actions.description"="Builds the McCoy group references website"
LABEL "com.github.actions.icon"="git"
LABEL "com.github.actions.color"="orange"

COPY /home/runner/work/References/References /home/References
COPY build_site.sh /build_site.sh

ENTRYPOINT ["sh", "/build_site.sh"]