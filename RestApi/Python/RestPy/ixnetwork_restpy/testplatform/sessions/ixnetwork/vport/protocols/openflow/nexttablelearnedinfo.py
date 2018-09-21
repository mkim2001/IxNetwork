from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class NextTableLearnedInfo(Base):
	"""The NextTableLearnedInfo class encapsulates a system managed nextTableLearnedInfo node in the ixnetwork hierarchy.

	An instance of the class can be obtained by accessing the NextTableLearnedInfo property from a parent instance.
	The internal properties list will be empty when the property is accessed and is populated from the server by using the find method.
	"""

	_SDM_NAME = 'nextTableLearnedInfo'

	def __init__(self, parent):
		super(NextTableLearnedInfo, self).__init__(parent)

	@property
	def ExperimenterData(self):
		"""NOT DEFINED

		Returns:
			str
		"""
		return self._get_attribute('experimenterData')

	@property
	def ExperimenterDataLength(self):
		"""NOT DEFINED

		Returns:
			number
		"""
		return self._get_attribute('experimenterDataLength')

	@property
	def ExperimenterId(self):
		"""NOT DEFINED

		Returns:
			number
		"""
		return self._get_attribute('experimenterId')

	@property
	def NextTableIds(self):
		"""NOT DEFINED

		Returns:
			str
		"""
		return self._get_attribute('nextTableIds')

	@property
	def Property(self):
		"""NOT DEFINED

		Returns:
			str
		"""
		return self._get_attribute('property')

	@property
	def SupportedField(self):
		"""NOT DEFINED

		Returns:
			str
		"""
		return self._get_attribute('supportedField')

	def find(self, ExperimenterData=None, ExperimenterDataLength=None, ExperimenterId=None, NextTableIds=None, Property=None, SupportedField=None):
		"""Finds and retrieves nextTableLearnedInfo data from the server.

		All named parameters support regex and can be used to selectively retrieve nextTableLearnedInfo data from the server.
		By default the find method takes no parameters and will retrieve all nextTableLearnedInfo data from the server.

		Args:
			ExperimenterData (str): NOT DEFINED
			ExperimenterDataLength (number): NOT DEFINED
			ExperimenterId (number): NOT DEFINED
			NextTableIds (str): NOT DEFINED
			Property (str): NOT DEFINED
			SupportedField (str): NOT DEFINED

		Returns:
			self: This instance with matching nextTableLearnedInfo data retrieved from the server available through an iterator or index

		Raises:
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._select(locals())

	def read(self, href):
		"""Retrieves a single instance of nextTableLearnedInfo data from the server.

		Args:
			href (str): An href to the instance to be retrieved

		Returns:
			self: This instance with the nextTableLearnedInfo data from the server available through an iterator or index

		Raises:
			NotFoundError: The requested resource does not exist on the server
			ServerError: The server has encountered an uncategorized error condition
		"""
		return self._read(href)
