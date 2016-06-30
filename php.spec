%define FPM_USER         www
%define FPM_GROUP        www
%define PREFIX           /usr/local
%define FPM_DIR          %{PREFIX}/php

Name:	        php	
Version:	5.5.35
Release:	2%{?dist}
Summary:	PHP FPM Server is open source php's webapp server.

Group:		System Environment/Daemons
License:	GPL
URL:		http://cn2.php.net/get/php-5.5.35.tar.gz/from/this/mirror
Source0:        php-5.5.35.tar.gz	

BuildRequires:	cmake gcc gcc-c++ libxml2 libxml2-devel autoconf libjpeg libjpeg-devel libpng libpng-devel gd bzip2 bzip2-devel curl curl-devel freetype freetype-devel zlib zlib-devel glibc glibc-devel glib2 glib2-devel libXpm libXpm-devel libmcrypt libmcrypt-devel mcrypt libc-client-devel automake
Requires:	libxml2 libxml2-devel autoconf libjpeg libjpeg-devel libpng libpng-devel gd bzip2 bzip2-devel curl curl-devel freetype freetype-devel zlib zlib-devel glibc glibc-devel glib2 glib2-devel libXpm libXpm-devel libmcrypt libmcrypt-devel mcrypt libc-client-devel automake libsphinxclient-devel libsphinxclient ImageMagick-devel
AutoReqProv:    no

%description
PHP FPM Server is open source php's webapp server.

%prep
%setup -q

%build
ln -snf /usr/lib64/libc-client.so /usr/lib/libc-client.so
./configure --prefix=%{FPM_DIR} --with-mysql=/usr --with-mysqli=/usr/bin/mysql_config --with-pdo-mysql=/usr --enable-fpm --with-config-file-path=%{FPM_DIR}/etc/ --with-iconv --with-jpeg-dir --with-png-dir --with-freetype-dir --with-xpm-dir --with-zlib --with-libxml-dir --disable-rpath --enable-bcmath --enable-shmop --enable-sysvsem --enable-inline-optimization --with-curl --with-pcre-regex --enable-mbstring --with-mcrypt --enable-ftp --with-gd --enable-gd-native-ttf --with-openssl --with-mhash --enable-pcntl --enable-sockets --with-xmlrpc --enable-zip --enable-soap --with-gettext --disable-fileinfo --enable-wddx --enable-exif --with-pcre-dir --disable-short-tags --with-openssl-dir --with-zend-vm=CALL --enable-maintainer-zts --enable-zend-signals --enable-mbregex  --with-imap --with-imap-ssl --with-kerberos

make -j `cat /proc/cpuinfo | grep processor| wc -l`


%install
make install DESTDIR=$RPM_BUILD_ROOT
tar czf - /usr/local/php --exclude='/usr/local/php/lib/php/extensions/no-debug-zts-20121212/*' | tar xzf - -C $RPM_BUILD_ROOT
install -D -m 0644 -p %{_sourcedir}/php.ini $RPM_BUILD_ROOT%{FPM_DIR}/etc/php.ini
install -D -m 0644 -p %{_sourcedir}/php-fpm.conf $RPM_BUILD_ROOT%{FPM_DIR}/etc/php-fpm.conf
install -D -m 755 -p %{_sourcedir}/php-fpm.init $RPM_BUILD_ROOT%{_initrddir}/php-fpm

%clean
#rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%attr(755, root,root) %{FPM_DIR}/*
#%attr(755, root,root) %{_initrddir}/php-fpm
/etc/rc.d/init.d/php-fpm

%pre
if [ $1 -eq 1 ]; then
    [ -n "`id -u %{FPM_USER} 2>/dev/null`" ] || useradd -r -M -s /sbin/nologin %{FPM_USER}
    ln -snf /usr/lib64/libc-client.so /usr/lib/libc-client.so
fi

%post
chkconfig --add php-fpm
chkconfig php-fpm on
ln -snf /usr/local/php/bin/* /usr/local/bin/ 

%preun
if [ $1 -eq 0 ]; then
    if [ `ps aux | grep -v 'grep' | grep -c 'php-fpm'` -gt 0 ]; then
        /etc/init.d/php-fpm stop 2>/dev/null || /bin/true
    fi
    chkconfig --del php-fpm 2>/dev/null || /bin/true
fi

%changelog

