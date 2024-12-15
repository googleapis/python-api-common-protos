# Copyright 2020 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from pathlib import Path

import synthtool as s
import synthtool.gcp as gcp
from synthtool.languages import python
from synthtool.sources import git

for library in s.get_staging_dirs():
    s.move([library / "**/*.py*"])
s.remove_staging_dirs()

# Add license headers
python.fix_pb2_headers()

LICENSE = """
# Copyright 2024 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License."""

# Add license header to *.pyi files
for pyi_file in Path(".").glob("**/*.pyi"):
    with open(pyi_file, 'r+') as f:
        content = f.read()
        f.seek(0, 0)
        f.write(f"{LICENSE}\n\n{content}")

# ----------------------------------------------------------------------------
#  Add templated files
# ----------------------------------------------------------------------------
common = gcp.CommonTemplates()
templated_files = common.py_library()
# TODO: use protoc-docs-plugin to add docstrings to protos
s.move(templated_files / ".kokoro", excludes=["docs/**/*", "publish-docs.sh"])
s.move(templated_files / "setup.cfg")
s.move(templated_files / "LICENSE")
s.move(templated_files / "MANIFEST.in")
s.move(templated_files / "renovate.json")
s.move(templated_files / ".github", excludes=["workflows"])

s.shell.run(["nox", "-s", "blacken"], hide_output=False)
