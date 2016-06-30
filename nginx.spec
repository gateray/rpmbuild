%define NGINX_USER         www
%define NGINX_GROUP        www
%define PREFIX             /usr/local 
%define NGINX_DIR %{PREFIX}/nginx

Name:           nginx
Version:        1.8.1
Release:	1%{?dist}
Summary:        A free, open-source, high-performance HTTP server and reverse proxy	

Group:		System Environment/Daemons
License:	BSD
URL:		http://nginx.org/download/
Source0:	http://nginx.org/download/%{name}-%{version}.tar.gz

Requires:	pcre openssl jemalloc pcre-devel zlib-devel openssl-devel jemalloc-devel

%description
Nginx is a free, open-source, high-performance HTTP server and reverse proxy.

%prep
%setup -q

%build
./configure --prefix=%{NGINX_DIR} \
    --user=%{NGINX_USER} --group=%{NGINX_GROUP} \
    --with-ld-opt='-ljemalloc' \
    --with-http_ssl_module \
    --with-http_flv_module \
    --with-http_gzip_static_module \
    --with-pcre \
    --with-http_stub_status_module

make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT
install -D -m 755 -p %{_sourcedir}/nginx.init $RPM_BUILD_ROOT%{_initrddir}/%{name}
install %{_sourcedir}/nginx.conf $RPM_BUILD_ROOT%{NGINX_DIR}/conf
install %{_sourcedir}/proxy.conf $RPM_BUILD_ROOT%{NGINX_DIR}/conf
install %{_sourcedir}/upstream.conf $RPM_BUILD_ROOT%{NGINX_DIR}/conf
mkdir $RPM_BUILD_ROOT%{NGINX_DIR}/conf/vhosts

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc LICENSE CHANGES README
%{NGINX_DIR}/*
%config(noreplace) %{NGINX_DIR}/conf/*
%attr(0755,root,root) %{_initrddir}/%{name}


%pre
if [ $1 -eq 1 ]; then
  [ -z `id -u www 2>/dev/null` ] && useradd -r -M -s /sbin/nologin %{NGINX_USER} || /bin/true
fi

%post
chkconfig --add %{name}

%preun
if [ $1 -eq 0 ]; then
  service %{name} stop
  chkconfig --del %{name} 
fi

%changelog

