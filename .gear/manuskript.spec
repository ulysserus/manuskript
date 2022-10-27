Name: manuskript
Version: 0.14.0
Release: alt1

Summary: Manuskript open source tool for writers
License: GPLv3+
Group: Editors

Url: http://www.theologeek.ch/manuskript/
Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3

BuildArch: noarch

%description
Manuskript is an open source tool for writers.  It provides
a rich environment to help writers create their first draft
and then further refine and edit their masterpiece.

%prep
%setup

%build

%install
#installing folder with package and assets
mkdir -p %buildroot%python3_sitelibdir/%name
cp -at %buildroot%python3_sitelibdir/%name -- \
	CHANGELOG.md COPYING CREDITS i18n icons libs %name \
	README.md resources sample-projects

#installing executable with correct path to package folder
sed -i 's,/usr/share,%python3_sitelibdir,' package/create_deb/%name
install -pDm755 package/create_deb/%name %buildroot%_bindir/%name

%files
%_bindir/*
%python3_sitelibdir/*

%changelog
* Thu Oct 27 2022 Ivan G <lordvivec@mail.ru> 0.14.0-alt1
- built for ALT Linux
