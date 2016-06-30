Name:	        php-imagick	
Version:	3.4.1
Release:	1%{?dist}
Summary:	Imagick is a native php extension to create and modify images using the ImageMagick API.
 
Group:		Development/Libraries
License:	GPL
URL:		http://php.net/manual/en/intro.imagick.php
Source0:	imagick-3.4.1.tgz

BuildRequires:	php
Requires:	php

%description
Imagick is a native php extension to create and modify images using the ImageMagick API.

%prep
umask 022
cd /root/rpmbuild/BUILD
LANG=C
export LANG
unset DISPLAY
rm -rf imagick-3.4.1
/bin/tar xf /root/rpmbuild/SOURCES/imagick-3.4.1.tgz -C .
cd imagick-3.4.1


%build
cd %{_builddir}/imagick-3.4.1
/usr/local/php/bin/phpize
./configure
make %{?_smp_mflags}


%install
cd %{_builddir}/imagick-3.4.1
make install EXTENSION_DIR=$RPM_BUILD_ROOT/usr/local/php/lib/php/extensions/no-debug-zts-20121212 phpincludedir=$RPM_BUILD_ROOT/usr/local/php/include/php

%files
%defattr(-,root,root,-)
/usr/local/php/*


%changelog

