# -*- coding: utf-8 -*-
"""Module where all interfaces, events and exceptions live."""

from quito.core import _
from plone.supermodel import model
from zope import schema

class IProject(model.Schema):
    """Schema for Conference Presenter content type.
    """

    members = schema.Tuple(
        title=_(u'Project Members'),
        description=_(u'The team members who are participating in the project'),
        value_type=schema.TextLine(),
        required=False,
        missing_value=(),
        default=(),
    )
    model.load('models/project.xml')

class IProjectlist(model.Schema):

    """Schema for Conference Presenter content type."""

    model.load('models/project_list.xml')

class ITask(model.Schema):

    """Schema for Conference Presenter content type.
    """

    members = schema.Tuple(
        title=_(u'Task Members'),
        description=_(u'Assign members to this task'),
        value_type=schema.TextLine(),
        required=False,
        missing_value=(),
        default=(),
    )

    model.load('models/task.xml')

class ITasklist(model.Schema):

    """Schema for Conference Presenter content type."""

    model.load('models/task_list.xml')

class IGroup(model.Schema):
    """Schema for Conference Presenter content type.
    """

    members = schema.Tuple(
        title=_(u'Group members'),
        description=_(u'The persons in the group'),
        value_type=schema.TextLine(),
        required=False,
        missing_value=(),
        default=(),
    )
    model.load('models/group.xml')

class IUser(model.Schema):

    """Schema for Conference Presenter content type."""

    model.load('models/user.xml')