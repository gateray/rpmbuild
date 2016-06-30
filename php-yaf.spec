Name:	        php-yaf
Version:	2.3.5
Release:	1%{?dist}
Summary:        PHP Framework in PHP extension 
Group:		Development/Libraries
License:	GPL
URL:		http://pecl.php.net/get/yaf-2.3.5.tgz
Source0:	yaf-2.3.5.tgz

BuildRequires:	php
Requires:	php

%description
PHP Framework in PHP extension

%prep
umask 022
cd /root/rpmbuild/BUILD
LANG=C
export LANG
unset DISPLAY
rm -rf yaf-2.3.5
/bin/tar xf /root/rpmbuild/SOURCES/yaf-2.3.5.tgz -C .
cd yaf-2.3.5

%build
cd %{_builddir}/yaf-2.3.5
/usr/local/php/bin/phpize
./configure
make %{?_smp_mflags}


%install
cd %{_builddir}/yaf-2.3.5
make install EXTENSION_DIR=$RPM_BUILD_ROOT/usr/local/php/lib/php/extensions/no-debug-zts-20121212 phpincludedir=$RPM_BUILD_ROOT/usr/local/php/include/php

%files
%defattr(-,root,root,-)
/usr/local/php/*


%changelog

