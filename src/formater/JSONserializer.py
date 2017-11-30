#! /usr/bin/env python3

import json

class JSON:

	def serialize(data):
		"""
		 * Take params string to transform in type list
		"""
		return json.loads(data)
	
	def deserialize(data):
		"""
		 * Take params list to transform in type string
		"""
		return json.dumps(data)

