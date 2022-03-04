# coding: utf-8

"""

    认证服务后台api  # noqa: E501

    
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from swagger_client.api_client import ApiClient


class ProfileApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def update_phone_number_new_sms(self, body, x_tenant_type, x_uuid, **kwargs):  # noqa: E501
        """个人中心修改手机号step3-新手机号发送短信  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_phone_number_new_sms(body, x_tenant_type, x_uuid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param UpdatePhoneNumberNewSmsReq body: (required)
        :param str x_tenant_type:  来自哪个平台 (required)
        :param str x_uuid: (required)
        :return: EmptyResp
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.update_phone_number_new_sms_with_http_info(body, x_tenant_type, x_uuid, **kwargs)  # noqa: E501
        else:
            (data) = self.update_phone_number_new_sms_with_http_info(body, x_tenant_type, x_uuid, **kwargs)  # noqa: E501
            return data

    def update_phone_number_new_sms_with_http_info(self, body, x_tenant_type, x_uuid, **kwargs):  # noqa: E501
        """个人中心修改手机号step3-新手机号发送短信  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_phone_number_new_sms_with_http_info(body, x_tenant_type, x_uuid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param UpdatePhoneNumberNewSmsReq body: (required)
        :param str x_tenant_type:  来自哪个平台 (required)
        :param str x_uuid: (required)
        :return: EmptyResp
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body', 'x_tenant_type', 'x_uuid']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_phone_number_new_sms" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `update_phone_number_new_sms`")  # noqa: E501
        # verify the required parameter 'x_tenant_type' is set
        if ('x_tenant_type' not in params or
                params['x_tenant_type'] is None):
            raise ValueError("Missing the required parameter `x_tenant_type` when calling `update_phone_number_new_sms`")  # noqa: E501
        # verify the required parameter 'x_uuid' is set
        if ('x_uuid' not in params or
                params['x_uuid'] is None):
            raise ValueError("Missing the required parameter `x_uuid` when calling `update_phone_number_new_sms`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'x_tenant_type' in params:
            header_params['X-Tenant-Type'] = params['x_tenant_type']  # noqa: E501
        if 'x_uuid' in params:
            header_params['X-Uuid'] = params['x_uuid']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['apiKey']  # noqa: E501

        return self.api_client.call_api(
            '/sms/new_phone_number', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='EmptyResp',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def update_phone_number_old_sms(self, body, x_tenant_type, x_uuid, **kwargs):  # noqa: E501
        """个人中心修改手机号step1-旧手机号发送短信  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_phone_number_old_sms(body, x_tenant_type, x_uuid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param UpdatePhoneNumberOldSmsReq body: (required)
        :param str x_tenant_type:  来自哪个平台 (required)
        :param str x_uuid: (required)
        :return: EmptyResp
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.update_phone_number_old_sms_with_http_info(body, x_tenant_type, x_uuid, **kwargs)  # noqa: E501
        else:
            (data) = self.update_phone_number_old_sms_with_http_info(body, x_tenant_type, x_uuid, **kwargs)  # noqa: E501
            return data

    def update_phone_number_old_sms_with_http_info(self, body, x_tenant_type, x_uuid, **kwargs):  # noqa: E501
        """个人中心修改手机号step1-旧手机号发送短信  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_phone_number_old_sms_with_http_info(body, x_tenant_type, x_uuid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param UpdatePhoneNumberOldSmsReq body: (required)
        :param str x_tenant_type:  来自哪个平台 (required)
        :param str x_uuid: (required)
        :return: EmptyResp
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body', 'x_tenant_type', 'x_uuid']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_phone_number_old_sms" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `update_phone_number_old_sms`")  # noqa: E501
        # verify the required parameter 'x_tenant_type' is set
        if ('x_tenant_type' not in params or
                params['x_tenant_type'] is None):
            raise ValueError("Missing the required parameter `x_tenant_type` when calling `update_phone_number_old_sms`")  # noqa: E501
        # verify the required parameter 'x_uuid' is set
        if ('x_uuid' not in params or
                params['x_uuid'] is None):
            raise ValueError("Missing the required parameter `x_uuid` when calling `update_phone_number_old_sms`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'x_tenant_type' in params:
            header_params['X-Tenant-Type'] = params['x_tenant_type']  # noqa: E501
        if 'x_uuid' in params:
            header_params['X-Uuid'] = params['x_uuid']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['apiKey']  # noqa: E501

        return self.api_client.call_api(
            '/sms/old_phone_number', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='EmptyResp',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def update_profile(self, body, x_tenant_type, x_uuid, **kwargs):  # noqa: E501
        """设置用户名/姓名  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_profile(body, x_tenant_type, x_uuid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param UpdateProfileReq body: (required)
        :param str x_tenant_type:  来自哪个平台 (required)
        :param str x_uuid: (required)
        :return: EmptyResp
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.update_profile_with_http_info(body, x_tenant_type, x_uuid, **kwargs)  # noqa: E501
        else:
            (data) = self.update_profile_with_http_info(body, x_tenant_type, x_uuid, **kwargs)  # noqa: E501
            return data

    def update_profile_with_http_info(self, body, x_tenant_type, x_uuid, **kwargs):  # noqa: E501
        """设置用户名/姓名  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_profile_with_http_info(body, x_tenant_type, x_uuid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param UpdateProfileReq body: (required)
        :param str x_tenant_type:  来自哪个平台 (required)
        :param str x_uuid: (required)
        :return: EmptyResp
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body', 'x_tenant_type', 'x_uuid']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_profile" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `update_profile`")  # noqa: E501
        # verify the required parameter 'x_tenant_type' is set
        if ('x_tenant_type' not in params or
                params['x_tenant_type'] is None):
            raise ValueError("Missing the required parameter `x_tenant_type` when calling `update_profile`")  # noqa: E501
        # verify the required parameter 'x_uuid' is set
        if ('x_uuid' not in params or
                params['x_uuid'] is None):
            raise ValueError("Missing the required parameter `x_uuid` when calling `update_profile`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'x_tenant_type' in params:
            header_params['X-Tenant-Type'] = params['x_tenant_type']  # noqa: E501
        if 'x_uuid' in params:
            header_params['X-Uuid'] = params['x_uuid']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['apiKey']  # noqa: E501

        return self.api_client.call_api(
            '/account/profile', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='EmptyResp',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def verify_new_phone_number(self, body, x_tenant_type, x_uuid, **kwargs):  # noqa: E501
        """个人中心修改手机号step4-验证新手机号  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.verify_new_phone_number(body, x_tenant_type, x_uuid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param VerifyNewPhoneNumberReq body: (required)
        :param str x_tenant_type:  来自哪个平台 (required)
        :param str x_uuid: (required)
        :return: EmptyResp
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.verify_new_phone_number_with_http_info(body, x_tenant_type, x_uuid, **kwargs)  # noqa: E501
        else:
            (data) = self.verify_new_phone_number_with_http_info(body, x_tenant_type, x_uuid, **kwargs)  # noqa: E501
            return data

    def verify_new_phone_number_with_http_info(self, body, x_tenant_type, x_uuid, **kwargs):  # noqa: E501
        """个人中心修改手机号step4-验证新手机号  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.verify_new_phone_number_with_http_info(body, x_tenant_type, x_uuid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param VerifyNewPhoneNumberReq body: (required)
        :param str x_tenant_type:  来自哪个平台 (required)
        :param str x_uuid: (required)
        :return: EmptyResp
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body', 'x_tenant_type', 'x_uuid']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method verify_new_phone_number" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `verify_new_phone_number`")  # noqa: E501
        # verify the required parameter 'x_tenant_type' is set
        if ('x_tenant_type' not in params or
                params['x_tenant_type'] is None):
            raise ValueError("Missing the required parameter `x_tenant_type` when calling `verify_new_phone_number`")  # noqa: E501
        # verify the required parameter 'x_uuid' is set
        if ('x_uuid' not in params or
                params['x_uuid'] is None):
            raise ValueError("Missing the required parameter `x_uuid` when calling `verify_new_phone_number`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'x_tenant_type' in params:
            header_params['X-Tenant-Type'] = params['x_tenant_type']  # noqa: E501
        if 'x_uuid' in params:
            header_params['X-Uuid'] = params['x_uuid']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['apiKey']  # noqa: E501

        return self.api_client.call_api(
            '/sms/verify_new_phone_number', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='EmptyResp',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def verify_old_phone_number(self, body, x_tenant_type, x_uuid, **kwargs):  # noqa: E501
        """个人中心修改手机号step2-验证旧手机号  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.verify_old_phone_number(body, x_tenant_type, x_uuid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param VerifyOldPhoneNumberReq body: (required)
        :param str x_tenant_type:  来自哪个平台 (required)
        :param str x_uuid: (required)
        :return: VerifyOldPhoneNumberResp
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.verify_old_phone_number_with_http_info(body, x_tenant_type, x_uuid, **kwargs)  # noqa: E501
        else:
            (data) = self.verify_old_phone_number_with_http_info(body, x_tenant_type, x_uuid, **kwargs)  # noqa: E501
            return data

    def verify_old_phone_number_with_http_info(self, body, x_tenant_type, x_uuid, **kwargs):  # noqa: E501
        """个人中心修改手机号step2-验证旧手机号  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.verify_old_phone_number_with_http_info(body, x_tenant_type, x_uuid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param VerifyOldPhoneNumberReq body: (required)
        :param str x_tenant_type:  来自哪个平台 (required)
        :param str x_uuid: (required)
        :return: VerifyOldPhoneNumberResp
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body', 'x_tenant_type', 'x_uuid']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method verify_old_phone_number" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `verify_old_phone_number`")  # noqa: E501
        # verify the required parameter 'x_tenant_type' is set
        if ('x_tenant_type' not in params or
                params['x_tenant_type'] is None):
            raise ValueError("Missing the required parameter `x_tenant_type` when calling `verify_old_phone_number`")  # noqa: E501
        # verify the required parameter 'x_uuid' is set
        if ('x_uuid' not in params or
                params['x_uuid'] is None):
            raise ValueError("Missing the required parameter `x_uuid` when calling `verify_old_phone_number`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'x_tenant_type' in params:
            header_params['X-Tenant-Type'] = params['x_tenant_type']  # noqa: E501
        if 'x_uuid' in params:
            header_params['X-Uuid'] = params['x_uuid']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['apiKey']  # noqa: E501

        return self.api_client.call_api(
            '/account/verify_old_phone_number', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='VerifyOldPhoneNumberResp',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
