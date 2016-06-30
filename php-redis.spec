Name:	        php-redis	
Version:	2.2.7
Release:	1%{?dist}
Summary:        PHP extension for interfacing with redis	
Group:		Development/Libraries
License:	GPL
URL:		http://pecl.php.net/get/redis-2.2.7.tgz
Source0:	redis-2.2.7.tgz

BuildRequires:	php
Requires:	php

%description
PHP extension for interfacing with redis

%prep
umask 022
cd /root/rpmbuild/BUILD
LANG=C
export LANG
unset DISPLAY
rm -rf redis-2.2.7
/bin/tar xf /root/rpmbuild/SOURCES/redis-2.2.7.tgz -C .
cd redis-2.2.7

%build
cd %{_builddir}/redis-2.2.7
/usr/local/php/bin/phpize
./configure
make %{?_smp_mflags}


%install
cd %{_builddir}/redis-2.2.7
make install EXTENSION_DIR=$RPM_BUILD_ROOT/usr/local/php/lib/php/extensions/no-debug-zts-20121212 phpincludedir=$RPM_BUILD_ROOT/usr/local/php/include/php

%files
%defattr(-,root,root,-)
/usr/local/php/*


%changelog

