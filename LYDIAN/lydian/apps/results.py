#!/usr/bin/env python
# Copyright (c) 2020 VMware, Inc. All Rights Reserved.
# SPDX-License-Identifier: BSD-2 License
# The full license information can be found in LICENSE.txt
# in the root directory of this project.
'''
Generic Results app. Gives results for traffic operations.
'''
import logging

from lydian.apps.base import BaseApp, exposify
from lydian.apps.recorder import TrafficRecordDB


log = logging.getLogger(__name__)


@exposify
class Results(BaseApp):

    def traffic(self, reqid, **kwargs):
        _filter = {}
        for key, value in kwargs.items():
            if key in TrafficRecordDB.SCHEMA:
                _filter[key] = value
            else:
                log.info("Skipping invalid TrafficRecord key:%s", key)
        with TrafficRecordDB() as db:
            return db.read(tbl=db.TABLE, reqid=reqid, **_filter)
