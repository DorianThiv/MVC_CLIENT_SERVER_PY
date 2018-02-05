#! /usr/bin/env python3

import json
from error import JSONSerializeFormatError

class JSON:

	def serialize(data):
		"""
		 * Take params string to transform in type list
		"""
		if not isinstance(data, str):
			raise JSONSerializeFormatError("Type is not string")
		return json.loads(data)

	def deserialize(data):
		"""
		 * Take params list to transform in type string
		"""
		if not isinstance(data, list):
			raise JSONSerializeFormatError("Type is not string")
		return json.dumps(data)

