Name:	        php-mongo	
Version:	1.6.13
Release:	1%{?dist}
Summary:	The MongoDB PHP driver should work on nearly any system: Windows, Mac OS X, Unix, and Linux 
Group:		Development/Libraries
License:	GPL
URL:		http://pecl.php.net/get/mongo-1.6.13.tgz
Source0:	mongo-1.6.13.tgz

BuildRequires:	php
Requires:	php

%description
The MongoDB PHP driver should work on nearly any system: Windows, Mac OS X, Unix, and Linux

%prep
umask 022
cd /root/rpmbuild/BUILD
LANG=C
export LANG
unset DISPLAY
rm -rf mongo-1.6.13
/bin/tar xf /root/rpmbuild/SOURCES/mongo-1.6.13.tgz -C .
cd mongo-1.6.13


%build
cd %{_builddir}/mongo-1.6.13
/usr/local/php/bin/phpize
./configure
make %{?_smp_mflags}


%install
cd %{_builddir}/mongo-1.6.13
make install EXTENSION_DIR=$RPM_BUILD_ROOT/usr/local/php/lib/php/extensions/no-debug-zts-20121212 phpincludedir=$RPM_BUILD_ROOT/usr/local/php/include/php

%files
%defattr(-,root,root,-)
/usr/local/php/*


%changelog

