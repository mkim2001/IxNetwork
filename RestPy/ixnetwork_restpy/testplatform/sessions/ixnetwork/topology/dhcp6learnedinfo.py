from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class Dhcp6LearnedInfo(Base):
	"""The Dhcp6LearnedInfo class encapsulates a required dhcp6LearnedInfo node in the ixnetwork hierarchy.

	An instance of the class can be obtained by accessing the Dhcp6LearnedInfo property from a parent instance.
	The internal properties list will contain one and only one set of properties which is populated when the property is accessed.
	"""

	_SDM_NAME = 'dhcp6LearnedInfo'

	def __init__(self, parent):
		super(Dhcp6LearnedInfo, self).__init__(parent)

	@property
	def Count(self):
		"""Number of elements inside associated multiplier-scaled container object, e.g. number of devices inside a Device Group

		Returns:
			number
		"""
		return self._get_attribute('count')

	@property
	def DescriptiveName(self):
		"""Longer, more descriptive name for element. It's not guaranteed to be unique like -name-, but maybe offers more context

		Returns:
			str
		"""
		return self._get_attribute('descriptiveName')

	@property
	def Name(self):
		"""Name of NGPF element, guaranteed to be unique in Scenario

		Returns:
			str
		"""
		return self._get_attribute('name')
	@Name.setter
	def Name(self, value):
		self._set_attribute('name', value)

	@property
	def TabbedDiscoveredAddresses(self):
		"""The discovered IPv6 addresses.

		Returns:
			list(str)
		"""
		return self._get_attribute('tabbedDiscoveredAddresses')

	@property
	def TabbedDiscoveredGateways(self):
		"""The discovered gateway IPv6 addresses.

		Returns:
			list(str)
		"""
		return self._get_attribute('tabbedDiscoveredGateways')

	@property
	def TabbedDiscoveredPrefix(self):
		"""The discovered IPv6 prefix.

		Returns:
			list(str)
		"""
		return self._get_attribute('tabbedDiscoveredPrefix')

	@property
	def TabbedDiscoveredPrefixLength(self):
		"""The length of the discovered IPv6 prefix.

		Returns:
			list(number)
		"""
		return self._get_attribute('tabbedDiscoveredPrefixLength')
