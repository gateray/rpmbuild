Name:	        php-memcache	
Version:	2.2.7
Release:	1%{?dist}
Summary:	Memcache module provides handy procedural and object oriented interface to memcached, highly effective caching daemon, which was especially designed to decrease database load in dynamic web applications.
 
Group:		Development/Libraries
License:	GPL
URL:		http://pecl.php.net/get/memcache-2.2.7.tgz
Source0:	memcache-2.2.7.tgz

BuildRequires:	php
Requires:	php

%description
Memcache module provides handy procedural and object oriented interface to memcached, highly effective caching daemon, which was especially designed to decrease database load in dynamic web applications.

%prep
umask 022
cd /root/rpmbuild/BUILD
LANG=C
export LANG
unset DISPLAY
rm -rf memcache-2.2.7
/bin/tar xf /root/rpmbuild/SOURCES/memcache-2.2.7.tgz -C .
cd memcache-2.2.7


%build
cd %{_builddir}/memcache-2.2.7
/usr/local/php/bin/phpize
./configure
make %{?_smp_mflags}


%install
cd %{_builddir}/memcache-2.2.7
make install EXTENSION_DIR=$RPM_BUILD_ROOT/usr/local/php/lib/php/extensions/no-debug-zts-20121212 phpincludedir=$RPM_BUILD_ROOT/usr/local/php/include/php

%files
%defattr(-,root,root,-)
/usr/local/php/*


%changelog

