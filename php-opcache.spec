Name:	        php-opcache	
Version:	7.0.5
Release:	1%{?dist}
Summary:	The Zend OPcache provides faster PHP execution through opcode caching and optimization.
Group:		Development/Libraries
License:	GPL
URL:		http://pecl.php.net/package/ZendOpcache
Source0:        zendopcache-7.0.5.tgz

BuildRequires:	php
Requires:	php

%description
The Zend OPcache provides faster PHP execution through opcode caching and optimization.

%prep
umask 022
cd /root/rpmbuild/BUILD
LANG=C
export LANG
unset DISPLAY
rm -rf zendopcache-7.0.5
/bin/tar xf /root/rpmbuild/SOURCES/zendopcache-7.0.5.tgz -C .
cd zendopcache-7.0.5


%build
cd %{_builddir}/zendopcache-7.0.5
/usr/local/php/bin/phpize
./configure
make %{?_smp_mflags}


%install
cd %{_builddir}/zendopcache-7.0.5
make install EXTENSION_DIR=$RPM_BUILD_ROOT/usr/local/php/lib/php/extensions/no-debug-zts-20121212 phpincludedir=$RPM_BUILD_ROOT/usr/local/php/include/php

%files
%defattr(-,root,root,-)
/usr/local/php/*


%changelog

