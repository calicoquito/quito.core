FROM plone:5.1.5

COPY docker.cfg /plone/instance/
#COPY requirements.txt /plone/instance/
#COPY buildout.cfg /plone/instance/
#COPY src/ /plone/instance/src/
COPY --chown=plone:plone  .   /plone/instance/src/quito.core
RUN gosu plone:5.1.5 buildout -c docker.cfg
