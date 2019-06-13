FROM plone:5

COPY site.cfg /plone/instance/
RUN gosu plone buildout -c site.cfg