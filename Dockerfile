FROM plone:5

COPY site.cfg /plone/instance/
COPY src/ /plone/instance/
RUN gosu plone buildout -c site.cfg