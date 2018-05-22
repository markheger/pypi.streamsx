# coding=utf-8
# Licensed Materials - Property of IBM
# Copyright IBM Corp. 2017
from typing import Any, List
from streamsx.rest_primitives import Domain, Instance, RestResource

class StreamsConnection:
    def __init__(self, username: Any=None, password: Any=None, resource_url: Any=None) -> None: ...
    def resource_url(self) -> str: ...
    def get_domains(self) -> List[Domain]: ...
    def get_domain(self, id: str) -> Domain: ...
    def get_instances(self) -> List[Instance]: ...
    def get_instance(self, id: str) -> Instance: ...
    def get_installations(self) -> Any: ...
    def get_resources(self) -> List[RestResource]: ...

class StreamingAnalyticsConnection(StreamsConnection):
    def __init__(self, vcap_services: Any=None, service_name: str=None) -> None: ...
    def resource_url(self) -> str: ...
    def get_streaming_analytics(self) -> Any: ...
