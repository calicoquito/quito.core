# -*- coding: utf-8 -*-
from plone import api
from plone.restapi.interfaces import IExpandableElement
from plone.restapi.services import Service
from plone.restapi.interfaces import ISerializeToJson
from zope.component import adapter
from zope.interface import Interface
from zope.interface import implementer
from zope.component import queryMultiAdapter
import os, pdb

error = -1
identifier_name = "data"
enabledDatatype = ["Folder", "Plone Site", "project_list", "project"]

# Restful Api GET JSON get function for content manipulation
def getContentJson(context, request):
    serializer = queryMultiAdapter((context, request),ISerializeToJson)
    if serializer is None:
        request.response.setStatus(501)
        return dict(error=dict(message='No serializer available.'))
    return serializer(version=request.get('version')) 

# Plone object for a specific of site 
# for the context of the getContentJson method
def getContentContext(context, url):
    try:
        return context[os.path.basename(os.path.normpath(url))]
    except Exception:
        return error


@implementer(IExpandableElement)
@adapter(Interface, Interface)
class FullContent(object):
    def __init__(self, context, request):
        self.context = context.aq_explicit
        self.request = request

    def __call__(self, expand=False):
        result = {
            'full_content': {
                '@id': '{}/@full_content'.format(
                    self.context.absolute_url(),
                ),
            },
        }
        if not expand:
            return result

        # === Your custom code comes here ===
        #pdb.set_trace()
        main_data = getContentJson(self.context, self.request)
        if(main_data["@type"] in enabledDatatype):
            main_data.pop('@components', None)
            root_context = self.context
            for index, item in enumerate(main_data["items"]):
                if(item["@type"] == "project" or item["@type"] == "group" or item["@type"] == "task"):
                    primary_context = getContentContext(root_context, item["@id"])
                    primary_request = self.request
                    primary_request["ACTUAL_URL"] = item["@id"]
                    primary_data = getContentJson(primary_context, primary_request)
                    primary_data.pop('@components', None)
                    for index2, item2 in enumerate(primary_data["items"]):
                        secondary_context = getContentContext(primary_context, item2["@id"])
                        secondary_request = self.request
                        secondary_request["ACTUAL_URL"] = item2["@id"]
                        secondary_data = getContentJson(secondary_context, secondary_request)
                        secondary_data.pop('@components', None)
                        if(item2["@type"] == "task_list"):
                            for index3, item3 in enumerate(secondary_data["items"]):
                                if(item3["@type"] == "task" or item["@type"] == "group"):
                                    teritiary_context = getContentContext(secondary_context, item3["@id"])
                                    teritiary_request = self.request
                                    teritiary_request["ACTUAL_URL"] = item3["@id"]
                                    teritiary_data = getContentJson(teritiary_context, teritiary_request)
                                    teritiary_data.pop('@components', None)
                                    secondary_data["items"][index3][identifier_name] = teritiary_data
                        primary_data["items"][index2][identifier_name] = secondary_data
                    main_data["items"][index][identifier_name] = primary_data
            result['full_content'][identifier_name] = main_data
            return result 
        return error
        # === End of cutom code ======

class FullContentGet(Service):

    def reply(self):
        try:
            service_factory = FullContent(self.context, self.request)
            if service_factory == error:
                self.request.response.setStatus(403)
                return dict(error=dict(message='Not a folder'))
            return service_factory(expand=True)['full_content']
        except Exception:
            self.request.response.setStatus(501)
            return dict(error=dict(message='Something went wrong'))
