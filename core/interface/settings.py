#!/usr/bin/env python
"""
	BlackSheep -- Penetration testing framework
	by Romain Gaucher <r@rgaucher.info> - http://rgaucher.info

	Copyright (c) 2008-2010 Romain Gaucher <r@rgaucher.info>

	Licensed under the Apache License, Version 2.0 (the "License");
	you may not use this file except in compliance with the License.
	You may obtain a copy of the License at

		http://www.apache.org/licenses/LICENSE-2.0

	Unless required by applicable law or agreed to in writing, software
	distributed under the License is distributed on an "AS IS" BASIS,
	WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
	See the License for the specific language governing permissions and
	limitations under the License.
"""
from PyQt4.QtCore import *
from PyQt4.QtGui import *

class Settings(QWidget):
	"""the settings interface; user settings, general settings"""
	def __init__(self, parent = None):
		QWidget.__init__(self, parent)
		"""
		URL : {
			- user: username, password, privilege in {root, admin, registered, anonymous, robot-crawler}
			- database: where to save the SQLITE3 database
			- preferences:
				- automated discovery
				- auto-tampering (based on some criteria... regexp?)
		}
		"""
