# Assignment for 370.062 OSESM by Julius Bergmann

Copyright 2022 Julius Bergmann

[![License](https://img.shields.io/badge/License-Apache_2.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.

## Description
Illustrative repository for 370.062 Open Source Energy Systems Modelling at TU Wien

The functions are used to calculate the minimum distance between multiple rows of pv-panels,
so that the front panels don't throw shaddow on the panels on the back.

The function calculate_module_height(length, angle) is used to get the maximum height of the construction

The function calculate_row_gap(height, angle_sun) is used to calculate the length of the shadow, at a specific sun angle
