FROM plone:5

COPY site.cfg /plone/instance/
COPY src/
RUN gosu plone buildout -c site.cfg