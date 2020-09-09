# coding: utf-8

"""
    KS Trade API's

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 1.0
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from openapi_client.configuration import Configuration


class InlineResponse200(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'instrumentName': 'str',
        'instrumentToken': 'int',
        'lastUpdatedTime': 'int',
        'lastTradedTime': 'int',
        'lastPrice': 'float',
        'lastTradedQuantity': 'int',
        'totalBuyQuantity': 'int',
        'totalSellQuantity': 'int',
        'averageTradedPrice': 'float',
        'openInterest': 'int',
        'netChange': 'float',
        'dprLow': 'float',
        'dprHigh': 'float',
        'ohlc': 'InlineResponse200Ohlc',
        'depth': 'InlineResponse200Depth'
    }

    attribute_map = {
        'instrumentName': 'instrumentName',
        'instrumentToken': 'instrumentToken',
        'lastUpdatedTime': 'lastUpdatedTime',
        'lastTradedTime': 'lastTradedTime',
        'lastPrice': 'lastPrice',
        'lastTradedQuantity': 'lastTradedQuantity',
        'totalBuyQuantity': 'totalBuyQuantity',
        'totalSellQuantity': 'totalSellQuantity',
        'averageTradedPrice': 'averageTradedPrice',
        'openInterest': 'openInterest',
        'netChange': 'netChange',
        'dprLow': 'dprLow',
        'dprHigh': 'dprHigh',
        'ohlc': 'ohlc',
        'depth': 'depth'
    }

    def __init__(self, instrumentName=None, instrumentToken=None, lastUpdatedTime=None, lastTradedTime=None, lastPrice=None, lastTradedQuantity=None, totalBuyQuantity=None, totalSellQuantity=None, averageTradedPrice=None, openInterest=None, netChange=None, dprLow=None, dprHigh=None, ohlc=None, depth=None, local_vars_configuration=None):  # noqa: E501
        """InlineResponse200 - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._instrumentName = None
        self._instrumentToken = None
        self._lastUpdatedTime = None
        self._lastTradedTime = None
        self._lastPrice = None
        self._lastTradedQuantity = None
        self._totalBuyQuantity = None
        self._totalSellQuantity = None
        self._averageTradedPrice = None
        self._openInterest = None
        self._netChange = None
        self._dprLow = None
        self._dprHigh = None
        self._ohlc = None
        self._depth = None
        self.discriminator = None

        if instrumentName is not None:
            self.instrumentName = instrumentName
        if instrumentToken is not None:
            self.instrumentToken = instrumentToken
        if lastUpdatedTime is not None:
            self.lastUpdatedTime = lastUpdatedTime
        if lastTradedTime is not None:
            self.lastTradedTime = lastTradedTime
        if lastPrice is not None:
            self.lastPrice = lastPrice
        if lastTradedQuantity is not None:
            self.lastTradedQuantity = lastTradedQuantity
        if totalBuyQuantity is not None:
            self.totalBuyQuantity = totalBuyQuantity
        if totalSellQuantity is not None:
            self.totalSellQuantity = totalSellQuantity
        if averageTradedPrice is not None:
            self.averageTradedPrice = averageTradedPrice
        if openInterest is not None:
            self.openInterest = openInterest
        if netChange is not None:
            self.netChange = netChange
        if dprLow is not None:
            self.dprLow = dprLow
        if dprHigh is not None:
            self.dprHigh = dprHigh
        if ohlc is not None:
            self.ohlc = ohlc
        if depth is not None:
            self.depth = depth

    @property
    def instrumentName(self):
        """Gets the instrumentName of this InlineResponse200.  # noqa: E501

        Name of the instrument  # noqa: E501

        :return: The instrumentName of this InlineResponse200.  # noqa: E501
        :rtype: str
        """
        return self._instrumentName

    @instrumentName.setter
    def instrumentName(self, instrumentName):
        """Sets the instrumentName of this InlineResponse200.

        Name of the instrument  # noqa: E501

        :param instrumentName: The instrumentName of this InlineResponse200.  # noqa: E501
        :type instrumentName: str
        """

        self._instrumentName = instrumentName

    @property
    def instrumentToken(self):
        """Gets the instrumentToken of this InlineResponse200.  # noqa: E501


        :return: The instrumentToken of this InlineResponse200.  # noqa: E501
        :rtype: int
        """
        return self._instrumentToken

    @instrumentToken.setter
    def instrumentToken(self, instrumentToken):
        """Sets the instrumentToken of this InlineResponse200.


        :param instrumentToken: The instrumentToken of this InlineResponse200.  # noqa: E501
        :type instrumentToken: int
        """

        self._instrumentToken = instrumentToken

    @property
    def lastUpdatedTime(self):
        """Gets the lastUpdatedTime of this InlineResponse200.  # noqa: E501

        Last time in epoch format when this data was updated  # noqa: E501

        :return: The lastUpdatedTime of this InlineResponse200.  # noqa: E501
        :rtype: int
        """
        return self._lastUpdatedTime

    @lastUpdatedTime.setter
    def lastUpdatedTime(self, lastUpdatedTime):
        """Sets the lastUpdatedTime of this InlineResponse200.

        Last time in epoch format when this data was updated  # noqa: E501

        :param lastUpdatedTime: The lastUpdatedTime of this InlineResponse200.  # noqa: E501
        :type lastUpdatedTime: int
        """

        self._lastUpdatedTime = lastUpdatedTime

    @property
    def lastTradedTime(self):
        """Gets the lastTradedTime of this InlineResponse200.  # noqa: E501

        Last time in epoch format when this scrip was traded  # noqa: E501

        :return: The lastTradedTime of this InlineResponse200.  # noqa: E501
        :rtype: int
        """
        return self._lastTradedTime

    @lastTradedTime.setter
    def lastTradedTime(self, lastTradedTime):
        """Sets the lastTradedTime of this InlineResponse200.

        Last time in epoch format when this scrip was traded  # noqa: E501

        :param lastTradedTime: The lastTradedTime of this InlineResponse200.  # noqa: E501
        :type lastTradedTime: int
        """

        self._lastTradedTime = lastTradedTime

    @property
    def lastPrice(self):
        """Gets the lastPrice of this InlineResponse200.  # noqa: E501

        Last traded price  # noqa: E501

        :return: The lastPrice of this InlineResponse200.  # noqa: E501
        :rtype: float
        """
        return self._lastPrice

    @lastPrice.setter
    def lastPrice(self, lastPrice):
        """Sets the lastPrice of this InlineResponse200.

        Last traded price  # noqa: E501

        :param lastPrice: The lastPrice of this InlineResponse200.  # noqa: E501
        :type lastPrice: float
        """

        self._lastPrice = lastPrice

    @property
    def lastTradedQuantity(self):
        """Gets the lastTradedQuantity of this InlineResponse200.  # noqa: E501

        Last traded quantity  # noqa: E501

        :return: The lastTradedQuantity of this InlineResponse200.  # noqa: E501
        :rtype: int
        """
        return self._lastTradedQuantity

    @lastTradedQuantity.setter
    def lastTradedQuantity(self, lastTradedQuantity):
        """Sets the lastTradedQuantity of this InlineResponse200.

        Last traded quantity  # noqa: E501

        :param lastTradedQuantity: The lastTradedQuantity of this InlineResponse200.  # noqa: E501
        :type lastTradedQuantity: int
        """

        self._lastTradedQuantity = lastTradedQuantity

    @property
    def totalBuyQuantity(self):
        """Gets the totalBuyQuantity of this InlineResponse200.  # noqa: E501

        Total bid quantity  # noqa: E501

        :return: The totalBuyQuantity of this InlineResponse200.  # noqa: E501
        :rtype: int
        """
        return self._totalBuyQuantity

    @totalBuyQuantity.setter
    def totalBuyQuantity(self, totalBuyQuantity):
        """Sets the totalBuyQuantity of this InlineResponse200.

        Total bid quantity  # noqa: E501

        :param totalBuyQuantity: The totalBuyQuantity of this InlineResponse200.  # noqa: E501
        :type totalBuyQuantity: int
        """

        self._totalBuyQuantity = totalBuyQuantity

    @property
    def totalSellQuantity(self):
        """Gets the totalSellQuantity of this InlineResponse200.  # noqa: E501

        Total ask quantity  # noqa: E501

        :return: The totalSellQuantity of this InlineResponse200.  # noqa: E501
        :rtype: int
        """
        return self._totalSellQuantity

    @totalSellQuantity.setter
    def totalSellQuantity(self, totalSellQuantity):
        """Sets the totalSellQuantity of this InlineResponse200.

        Total ask quantity  # noqa: E501

        :param totalSellQuantity: The totalSellQuantity of this InlineResponse200.  # noqa: E501
        :type totalSellQuantity: int
        """

        self._totalSellQuantity = totalSellQuantity

    @property
    def averageTradedPrice(self):
        """Gets the averageTradedPrice of this InlineResponse200.  # noqa: E501

        Average traded price for the day  # noqa: E501

        :return: The averageTradedPrice of this InlineResponse200.  # noqa: E501
        :rtype: float
        """
        return self._averageTradedPrice

    @averageTradedPrice.setter
    def averageTradedPrice(self, averageTradedPrice):
        """Sets the averageTradedPrice of this InlineResponse200.

        Average traded price for the day  # noqa: E501

        :param averageTradedPrice: The averageTradedPrice of this InlineResponse200.  # noqa: E501
        :type averageTradedPrice: float
        """

        self._averageTradedPrice = averageTradedPrice

    @property
    def openInterest(self):
        """Gets the openInterest of this InlineResponse200.  # noqa: E501

        Open interest in case of derivateive contracts  # noqa: E501

        :return: The openInterest of this InlineResponse200.  # noqa: E501
        :rtype: int
        """
        return self._openInterest

    @openInterest.setter
    def openInterest(self, openInterest):
        """Sets the openInterest of this InlineResponse200.

        Open interest in case of derivateive contracts  # noqa: E501

        :param openInterest: The openInterest of this InlineResponse200.  # noqa: E501
        :type openInterest: int
        """

        self._openInterest = openInterest

    @property
    def netChange(self):
        """Gets the netChange of this InlineResponse200.  # noqa: E501

        Absolute change in price from previous day close  # noqa: E501

        :return: The netChange of this InlineResponse200.  # noqa: E501
        :rtype: float
        """
        return self._netChange

    @netChange.setter
    def netChange(self, netChange):
        """Sets the netChange of this InlineResponse200.

        Absolute change in price from previous day close  # noqa: E501

        :param netChange: The netChange of this InlineResponse200.  # noqa: E501
        :type netChange: float
        """

        self._netChange = netChange

    @property
    def dprLow(self):
        """Gets the dprLow of this InlineResponse200.  # noqa: E501

        Lower value of daily price range  # noqa: E501

        :return: The dprLow of this InlineResponse200.  # noqa: E501
        :rtype: float
        """
        return self._dprLow

    @dprLow.setter
    def dprLow(self, dprLow):
        """Sets the dprLow of this InlineResponse200.

        Lower value of daily price range  # noqa: E501

        :param dprLow: The dprLow of this InlineResponse200.  # noqa: E501
        :type dprLow: float
        """

        self._dprLow = dprLow

    @property
    def dprHigh(self):
        """Gets the dprHigh of this InlineResponse200.  # noqa: E501

        Higher value of daily price range  # noqa: E501

        :return: The dprHigh of this InlineResponse200.  # noqa: E501
        :rtype: float
        """
        return self._dprHigh

    @dprHigh.setter
    def dprHigh(self, dprHigh):
        """Sets the dprHigh of this InlineResponse200.

        Higher value of daily price range  # noqa: E501

        :param dprHigh: The dprHigh of this InlineResponse200.  # noqa: E501
        :type dprHigh: float
        """

        self._dprHigh = dprHigh

    @property
    def ohlc(self):
        """Gets the ohlc of this InlineResponse200.  # noqa: E501


        :return: The ohlc of this InlineResponse200.  # noqa: E501
        :rtype: InlineResponse200Ohlc
        """
        return self._ohlc

    @ohlc.setter
    def ohlc(self, ohlc):
        """Sets the ohlc of this InlineResponse200.


        :param ohlc: The ohlc of this InlineResponse200.  # noqa: E501
        :type ohlc: InlineResponse200Ohlc
        """

        self._ohlc = ohlc

    @property
    def depth(self):
        """Gets the depth of this InlineResponse200.  # noqa: E501


        :return: The depth of this InlineResponse200.  # noqa: E501
        :rtype: InlineResponse200Depth
        """
        return self._depth

    @depth.setter
    def depth(self, depth):
        """Sets the depth of this InlineResponse200.


        :param depth: The depth of this InlineResponse200.  # noqa: E501
        :type depth: InlineResponse200Depth
        """

        self._depth = depth

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, InlineResponse200):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, InlineResponse200):
            return True

        return self.to_dict() != other.to_dict()