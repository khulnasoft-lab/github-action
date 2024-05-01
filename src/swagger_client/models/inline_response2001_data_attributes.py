# coding: utf-8

"""
    Kengine API

    The official OpenAPI spec for the Kengine API.  # noqa: E501

    OpenAPI spec version: 0.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six


class InlineResponse2001DataAttributes(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        "bypass_token": "str",
        "paused": "bool",
        "stopped": "bool",
        "projects": "list[InlineResponse2001DataAttributesProjects]",
        "ready": "bool",
        "name": "str",
        "processing": "bool",
        "url": "str",
    }

    attribute_map = {
        "bypass_token": "bypass_token",
        "paused": "paused",
        "stopped": "stopped",
        "projects": "projects",
        "ready": "ready",
        "name": "name",
        "processing": "processing",
        "url": "url",
    }

    def __init__(
        self,
        bypass_token=None,
        paused=None,
        stopped=None,
        projects=None,
        ready=None,
        name=None,
        processing=None,
        url=None,
    ):  # noqa: E501
        """InlineResponse2001DataAttributes - a model defined in Swagger"""  # noqa: E501
        self._bypass_token = None
        self._paused = None
        self._stopped = None
        self._projects = None
        self._ready = None
        self._name = None
        self._processing = None
        self._url = None
        self.discriminator = None
        if bypass_token is not None:
            self.bypass_token = bypass_token
        if paused is not None:
            self.paused = paused
        if stopped is not None:
            self.stopped = stopped
        if projects is not None:
            self.projects = projects
        if ready is not None:
            self.ready = ready
        if name is not None:
            self.name = name
        if processing is not None:
            self.processing = processing
        if url is not None:
            self.url = url

    @property
    def bypass_token(self):
        """Gets the bypass_token of this InlineResponse2001DataAttributes.  # noqa: E501


        :return: The bypass_token of this InlineResponse2001DataAttributes.  # noqa: E501
        :rtype: str
        """
        return self._bypass_token

    @bypass_token.setter
    def bypass_token(self, bypass_token):
        """Sets the bypass_token of this InlineResponse2001DataAttributes.


        :param bypass_token: The bypass_token of this InlineResponse2001DataAttributes.  # noqa: E501
        :type: str
        """

        self._bypass_token = bypass_token

    @property
    def paused(self):
        """Gets the paused of this InlineResponse2001DataAttributes.  # noqa: E501


        :return: The paused of this InlineResponse2001DataAttributes.  # noqa: E501
        :rtype: bool
        """
        return self._paused

    @paused.setter
    def paused(self, paused):
        """Sets the paused of this InlineResponse2001DataAttributes.


        :param paused: The paused of this InlineResponse2001DataAttributes.  # noqa: E501
        :type: bool
        """

        self._paused = paused

    @property
    def stopped(self):
        """Gets the stopped of this InlineResponse2001DataAttributes.  # noqa: E501


        :return: The stopped of this InlineResponse2001DataAttributes.  # noqa: E501
        :rtype: bool
        """
        return self._stopped

    @stopped.setter
    def stopped(self, stopped):
        """Sets the stopped of this InlineResponse2001DataAttributes.


        :param stopped: The stopped of this InlineResponse2001DataAttributes.  # noqa: E501
        :type: bool
        """

        self._stopped = stopped

    @property
    def projects(self):
        """Gets the projects of this InlineResponse2001DataAttributes.  # noqa: E501


        :return: The projects of this InlineResponse2001DataAttributes.  # noqa: E501
        :rtype: list[InlineResponse2001DataAttributesProjects]
        """
        return self._projects

    @projects.setter
    def projects(self, projects):
        """Sets the projects of this InlineResponse2001DataAttributes.


        :param projects: The projects of this InlineResponse2001DataAttributes.  # noqa: E501
        :type: list[InlineResponse2001DataAttributesProjects]
        """

        self._projects = projects

    @property
    def ready(self):
        """Gets the ready of this InlineResponse2001DataAttributes.  # noqa: E501


        :return: The ready of this InlineResponse2001DataAttributes.  # noqa: E501
        :rtype: bool
        """
        return self._ready

    @ready.setter
    def ready(self, ready):
        """Sets the ready of this InlineResponse2001DataAttributes.


        :param ready: The ready of this InlineResponse2001DataAttributes.  # noqa: E501
        :type: bool
        """

        self._ready = ready

    @property
    def name(self):
        """Gets the name of this InlineResponse2001DataAttributes.  # noqa: E501


        :return: The name of this InlineResponse2001DataAttributes.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this InlineResponse2001DataAttributes.


        :param name: The name of this InlineResponse2001DataAttributes.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def processing(self):
        """Gets the processing of this InlineResponse2001DataAttributes.  # noqa: E501


        :return: The processing of this InlineResponse2001DataAttributes.  # noqa: E501
        :rtype: bool
        """
        return self._processing

    @processing.setter
    def processing(self, processing):
        """Sets the processing of this InlineResponse2001DataAttributes.


        :param processing: The processing of this InlineResponse2001DataAttributes.  # noqa: E501
        :type: bool
        """

        self._processing = processing

    @property
    def url(self):
        """Gets the url of this InlineResponse2001DataAttributes.  # noqa: E501


        :return: The url of this InlineResponse2001DataAttributes.  # noqa: E501
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this InlineResponse2001DataAttributes.


        :param url: The url of this InlineResponse2001DataAttributes.  # noqa: E501
        :type: str
        """

        self._url = url

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(
                    map(lambda x: x.to_dict() if hasattr(x, "to_dict") else x, value)
                )
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(
                    map(
                        lambda item: (item[0], item[1].to_dict())
                        if hasattr(item[1], "to_dict")
                        else item,
                        value.items(),
                    )
                )
            else:
                result[attr] = value
        if issubclass(InlineResponse2001DataAttributes, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, InlineResponse2001DataAttributes):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other