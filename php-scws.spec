Name:	        php-scws
Version:	1.2.3
Release:	1%{?dist}
Summary:        scws in PHP extension 
Group:		Development/Libraries
License:	GPL
URL:		http://www.xunsearch.com/scws/index.php
Source0:	scws-1.2.3.tar.bz2

BuildRequires:	php scws
Requires:	php scws

%description
scws in PHP extension

%prep
umask 022
cd /root/rpmbuild/BUILD
LANG=C
export LANG
unset DISPLAY
rm -rf scws-1.2.3
/bin/tar xf /root/rpmbuild/SOURCES/scws-1.2.3.tar.bz2 -C .

%build
cd %{_builddir}/scws-1.2.3/phpext
/usr/local/php/bin/phpize
./configure
make %{?_smp_mflags}


%install
cd %{_builddir}/scws-1.2.3/phpext
make install EXTENSION_DIR=$RPM_BUILD_ROOT/usr/local/php/lib/php/extensions/no-debug-zts-20121212 phpincludedir=$RPM_BUILD_ROOT/usr/local/php/include/php

%files
%defattr(-,root,root,-)
/usr/local/php/*


%changelog

