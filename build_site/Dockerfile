# GitHub Actions container to support doing and build config automatically upon a push
FROM alpine/git:1.0.7

LABEL "name"="McCoyGroup/build-site"
LABEL "maintainer"="Mark Boyer <b3m2a1uw.edu>"
LABEL "version"="0.0.1"

LABEL "com.github.actions.name"="McCoy Group Site Builder"
LABEL "com.github.actions.description"="Builds the McCoy group references website"
LABEL "com.github.actions.icon"="git"
LABEL "com.github.actions.color"="orange"

COPY build_site.sh /build_site.sh

ENTRYPOINT ["sh", "/build_site.sh"]