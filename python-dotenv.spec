# Copyright 2022 Wong Hoi Sing Edison <hswong3i@pantarei-design.com>
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
# limitations under the License.

%global debug_package %{nil}

Name: python-dotenv
Epoch: 100
Version: 0.21.1
Release: 1%{?dist}
BuildArch: noarch
Summary: Read key-value pairs from a .env file and set them as environment variables
License: BSD-3-Clause
URL: https://github.com/theskumar/python-dotenv/tags
Source0: %{name}_%{version}.orig.tar.gz
BuildRequires: fdupes
BuildRequires: python-rpm-macros
BuildRequires: python3-devel
BuildRequires: python3-setuptools

%description
Python-dotenv reads key-value pairs from a .env file and can set them as
environment variables.

%prep
%autosetup -T -c -n %{name}_%{version}-%{release}
tar -zx -f %{S:0} --strip-components=1 -C .

%build
%py3_build

%install
%py3_install
find %{buildroot}%{python3_sitelib} -type f -name '*.pyc' -exec rm -rf {} \;
fdupes -qnrps %{buildroot}%{python3_sitelib}

%check

%if 0%{?suse_version} > 1500
%package -n python%{python3_version_nodots}-python-dotenv
Summary: Read key-value pairs from a .env file and set them as environment variables
Requires: python3
Requires: python3-click
Provides: python3-dotenv = %{epoch}:%{version}-%{release}
Provides: python3dist(dotenv) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}-dotenv = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}dist(dotenv) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}-dotenv = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}dist(dotenv) = %{epoch}:%{version}-%{release}

%description -n python%{python3_version_nodots}-python-dotenv
Python-dotenv reads key-value pairs from a .env file and can set them as
environment variables.

%files -n python%{python3_version_nodots}-python-dotenv
%license LICENSE
%{_bindir}/*
%{python3_sitelib}/*
%endif

%if 0%{?sle_version} > 150000
%package -n python3-python-dotenv
Summary: Read key-value pairs from a .env file and set them as environment variables
Requires: python3
Requires: python3-click
Provides: python3-dotenv = %{epoch}:%{version}-%{release}
Provides: python3dist(dotenv) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}-dotenv = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}dist(dotenv) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}-dotenv = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}dist(dotenv) = %{epoch}:%{version}-%{release}

%description -n python3-python-dotenv
Python-dotenv reads key-value pairs from a .env file and can set them as
environment variables.

%files -n python3-python-dotenv
%license LICENSE
%{_bindir}/*
%{python3_sitelib}/*
%endif

%if !(0%{?suse_version} > 1500) && !(0%{?sle_version} > 150000)
%package -n python3-dotenv
Summary: Read key-value pairs from a .env file and set them as environment variables
Requires: python3
Requires: python3-click
Provides: python3-dotenv = %{epoch}:%{version}-%{release}
Provides: python3dist(dotenv) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}-dotenv = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}dist(dotenv) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}-dotenv = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}dist(dotenv) = %{epoch}:%{version}-%{release}

%description -n python3-dotenv
Python-dotenv reads key-value pairs from a .env file and can set them as
environment variables.

%files -n python3-dotenv
%license LICENSE
%{_bindir}/*
%{python3_sitelib}/*
%endif

%changelog
