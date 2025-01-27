#  Copyright (c) ZenML GmbH 2022. All Rights Reserved.
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at:
#
#       https://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express
#  or implied. See the License for the specific language governing
#  permissions and limitations under the License.
"""Alerters allow you to send alerts from within your pipeline.

This is useful to immediately get notified when failures happen,
and also for general monitoring / reporting.
"""

from zenml.alerter.alerter_step import alerter_ask_step, alerter_post_step
from zenml.alerter.base_alerter import BaseAlerter

__all__ = [
    "BaseAlerter",
    "alerter_post_step",
    "alerter_ask_step",
]
