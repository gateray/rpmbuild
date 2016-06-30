Name:	        php-sphinx
Version:	1.3.3
Release:	1%{?dist}
Summary:        Client extension for sphinx - opensource SQL full-text search engine 
Group:		Development/Libraries
License:	GPL
URL:		http://pecl.php.net/get/sphinx-1.3.3.tgz
Source0:	sphinx-1.3.3.tgz

BuildRequires:	php libsphinxclient-devel libsphinxclient
Requires:	php libsphinxclient-devel libsphinxclient

%description
Client extension for sphinx - opensource SQL full-text search engine

%prep
umask 022
cd /root/rpmbuild/BUILD
LANG=C
export LANG
unset DISPLAY
rm -rf sphinx-1.3.3
/bin/tar xf /root/rpmbuild/SOURCES/sphinx-1.3.3.tgz -C .
cd sphinx-1.3.3

%build
cd %{_builddir}/sphinx-1.3.3
/usr/local/php/bin/phpize
./configure
make %{?_smp_mflags}


%install
cd %{_builddir}/sphinx-1.3.3
make install EXTENSION_DIR=$RPM_BUILD_ROOT/usr/local/php/lib/php/extensions/no-debug-zts-20121212 phpincludedir=$RPM_BUILD_ROOT/usr/local/php/include/php

%files
%defattr(-,root,root,-)
/usr/local/php/*


%changelog

