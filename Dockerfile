FROM plone:5

COPY docker.cfg /plone/instance/
#COPY src/ /plone/instance/src/
COPY --chown=plone:plone  .   /plone/instance/src/quito.core
RUN gosu plone buildout -c docker.cfg
