Name:	        scws
Version:	1.2.3
Release:	1%{?dist}
Summary:        Simple Chinese Word Segmentation
Group:		Development/Libraries
License:	GPL
URL:	        http://www.xunsearch.com/scws/index.php	
Source0:	scws-1.2.3.tar.bz2

BuildRequires:	php
Requires:	php

%description
Simple Chinese Word Segmentation

%prep
umask 022
cd /root/rpmbuild/BUILD
LANG=C
export LANG
unset DISPLAY
rm -rf scws-1.2.3
/bin/tar xf /root/rpmbuild/SOURCES/scws-1.2.3.tar.bz2 -C .
cd scws-1.2.3

%build
cd %{_builddir}/scws-1.2.3
./configure --prefix=/usr/local/scws
make %{?_smp_mflags}

%install
cd %{_builddir}/scws-1.2.3
make install DESTDIR=$RPM_BUILD_ROOT
cp /root/rpmbuild/SOURCES/scws-dict-chs-gbk.tar.bz2 $RPM_BUILD_ROOT/usr/local/scws/etc
cp /root/rpmbuild/SOURCES/scws-dict-chs-utf8.tar.bz2 $RPM_BUILD_ROOT/usr/local/scws/etc
cd $RPM_BUILD_ROOT/usr/local/scws/etc
/bin/tar xf scws-dict-chs-gbk.tar.bz2
/bin/tar xf scws-dict-chs-utf8.tar.bz2

%files
%defattr(-,root,root,-)
/usr
/usr/local
/usr/local/scws
/usr/local/scws/lib
/usr/local/scws/lib/libscws.so.1.1.0
/usr/local/scws/lib/libscws.so.1
/usr/local/scws/lib/libscws.so
/usr/local/scws/lib/libscws.la
/usr/local/scws/include
/usr/local/scws/include/scws
/usr/local/scws/include/scws/charset.h
/usr/local/scws/include/scws/crc32.h
/usr/local/scws/include/scws/pool.h
/usr/local/scws/include/scws/scws.h
/usr/local/scws/include/scws/xdict.h
/usr/local/scws/include/scws/darray.h
/usr/local/scws/include/scws/rule.h
/usr/local/scws/include/scws/xdb.h
/usr/local/scws/include/scws/xtree.h
/usr/local/scws/include/scws/version.h
/usr/local/scws/bin
/usr/local/scws/bin/scws
/usr/local/scws/bin/scws-gen-dict
/usr/local/scws/etc
/usr/local/scws/etc/rules.ini
/usr/local/scws/etc/rules.utf8.ini
/usr/local/scws/etc/rules_cht.utf8.ini
/usr/local/scws/etc/scws-dict-chs-gbk.tar.bz2
/usr/local/scws/etc/scws-dict-chs-utf8.tar.bz2
/usr/local/scws/etc/dict.xdb
/usr/local/scws/etc/dict.utf8.xdb


%changelog

