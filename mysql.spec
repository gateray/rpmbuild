%define MYSQL_USER         mysql
%define MYSQL_GROUP        mysql
%define PREFIX             /usr/local
%define MYSQL_DIR          %{PREFIX}/mysql
%define MYSQL_PASS         mysql

Name:		mysql56
Version:	5.6.29
Release:	1%{?dist}
Summary:	MySQL Server is open source RDB system.

Group:		applications/database
License:	GPL
URL:		http://downloads.mysql.com/archives/get/file/mysql-5.6.29.tar.gz
Source0:        mysql-5.6.29.tar.gz	

BuildRequires:	cmake
Requires:	gperf time bison ncurses-devel libaio-devel bison-devel
AutoReqProv:    no

%description
MySQL Server is open source RDB system.

%prep
#%setup -q
umask 022
LANG=C
CC=gcc
CXX=g++
export LANG CC CXX
unset DISPLAY
cd /root/rpmbuild/BUILD
rm -rf mysql-5.6.29
tar -zxf /root/rpmbuild/SOURCES/mysql-5.6.29.tar.gz -C .

%build
cd /root/rpmbuild/BUILD/mysql-5.6.29
cmake \
  -DCMAKE_BUILD_TYPE=RelWithDebInfo                      \
  -DINSTALL_LAYOUT=STANDALONE                            \
  -DCMAKE_INSTALL_PREFIX=%{MYSQL_DIR}                    \
  -DINSTALL_INCLUDEDIR=%{PREFIX}/include                 \
  -DINSTALL_LIBDIR=%{PREFIX}/lib                         \
  -DINSTALL_MANDIR=%{PREFIX}/share/man                   \
  -DMYSQL_DATADIR=%{MYSQL_DIR}/data                      \
  -DSYSCONFDIR=%{MYSQL_DIR}                              \
  -DDEFAULT_CHARSET=utf8                                 \
  -DDEFAULT_COLLATION=utf8_general_ci                    \
  -DENABLED_LOCAL_INFILE=ON                              \
  -DENABLED_PROFILING=ON                                 \
  -DOPTIMIZER_TRACE=ON                                   \
  -DWITH_DEBUG=OFF                                       \
  -DWITH_VALGRIND=OFF                                    \
  -DWITH_EXTRA_CHARSETS=all                              \
  -DWITH_SSL=bundled                                     \
  -DWITH_UNIT_TESTS=OFF                                  \
  -DWITH_ZLIB=bundled                                    \
  -DWITH_EXTRA_CHARSETS=all                              \
  -DWITH_EMBEDDED_SERVER=0                               \
  -DCOMMUNITY_BUILD=ON                                   \
  -DWITH_MYISAM_STORAGE_ENGINE=ON                        \
  -DWITH_MEMORY_STORAGE_ENGINE=ON                        \
  -DWITH_PARTITION_STORAGE_ENGINE=ON                     \
  -DWITH_INNOBASE_STORAGE_ENGINE=ON                      \
  -DWITH_ARCHIVE_STORAGE_ENGINE=ON                       \
  -DWITH_BLACKHOLE_STORAGE_ENGINE=ON                     \
  -DWITH_PERFSCHEMA_STORAGE_ENGINE=ON
make -j `cat /proc/cpuinfo | grep processor| wc -l`


%install
cd /root/rpmbuild/BUILD/mysql-5.6.29 
make install DESTDIR=$RPM_BUILD_ROOT
#install -m 0644 -p %{_sourcedir}/my.cnf $RPM_BUILD_ROOT%{MYSQL_DIR}/my.cnf

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,%{MYSQL_USER},%{MYSQL_GROUP},-)
%attr(755, %{MYSQL_USER},%{MYSQL_GROUP}) %{MYSQL_DIR}/*
/usr/local/include/big_endian.h
/usr/local/include/byte_order_generic.h
/usr/local/include/byte_order_generic_x86.h
/usr/local/include/byte_order_generic_x86_64.h
/usr/local/include/decimal.h
/usr/local/include/errmsg.h
/usr/local/include/keycache.h
/usr/local/include/little_endian.h
/usr/local/include/m_ctype.h
/usr/local/include/m_string.h
/usr/local/include/my_alloc.h
/usr/local/include/my_attribute.h
/usr/local/include/my_byteorder.h
/usr/local/include/my_compiler.h
/usr/local/include/my_config.h
/usr/local/include/my_dbug.h
/usr/local/include/my_dir.h
/usr/local/include/my_getopt.h
/usr/local/include/my_global.h
/usr/local/include/my_list.h
/usr/local/include/my_net.h
/usr/local/include/my_pthread.h
/usr/local/include/my_sys.h
/usr/local/include/my_xml.h
/usr/local/include/mysql.h
/usr/local/include/mysql/client_authentication.h
/usr/local/include/mysql/client_plugin.h
/usr/local/include/mysql/client_plugin.h.pp
/usr/local/include/mysql/get_password.h
/usr/local/include/mysql/innodb_priv.h
/usr/local/include/mysql/plugin.h
/usr/local/include/mysql/plugin_audit.h
/usr/local/include/mysql/plugin_audit.h.pp
/usr/local/include/mysql/plugin_auth.h
/usr/local/include/mysql/plugin_auth.h.pp
/usr/local/include/mysql/plugin_auth_common.h
/usr/local/include/mysql/plugin_ftparser.h
/usr/local/include/mysql/plugin_ftparser.h.pp
/usr/local/include/mysql/plugin_validate_password.h
/usr/local/include/mysql/psi/mysql_file.h
/usr/local/include/mysql/psi/mysql_idle.h
/usr/local/include/mysql/psi/mysql_socket.h
/usr/local/include/mysql/psi/mysql_stage.h
/usr/local/include/mysql/psi/mysql_statement.h
/usr/local/include/mysql/psi/mysql_table.h
/usr/local/include/mysql/psi/mysql_thread.h
/usr/local/include/mysql/psi/psi.h
/usr/local/include/mysql/service_my_plugin_log.h
/usr/local/include/mysql/service_my_snprintf.h
/usr/local/include/mysql/service_mysql_string.h
/usr/local/include/mysql/service_thd_alloc.h
/usr/local/include/mysql/service_thd_wait.h
/usr/local/include/mysql/service_thread_scheduler.h
/usr/local/include/mysql/services.h
/usr/local/include/mysql/thread_pool_priv.h
/usr/local/include/mysql_com.h
/usr/local/include/mysql_com_server.h
/usr/local/include/mysql_embed.h
/usr/local/include/mysql_time.h
/usr/local/include/mysql_version.h
/usr/local/include/mysqld_ername.h
/usr/local/include/mysqld_error.h
/usr/local/include/plugin.h
/usr/local/include/plugin_audit.h
/usr/local/include/plugin_ftparser.h
/usr/local/include/plugin_validate_password.h
/usr/local/include/sql_common.h
/usr/local/include/sql_state.h
/usr/local/include/sslopt-case.h
/usr/local/include/sslopt-longopts.h
/usr/local/include/sslopt-vars.h
/usr/local/include/typelib.h
/usr/local/lib/libmysqlclient.a
/usr/local/lib/libmysqlclient.so
/usr/local/lib/libmysqlclient.so.18
/usr/local/lib/libmysqlclient.so.18.1.0
/usr/local/lib/libmysqlclient_r.a
/usr/local/lib/libmysqlclient_r.so
/usr/local/lib/libmysqlclient_r.so.18
/usr/local/lib/libmysqlclient_r.so.18.1.0
/usr/local/lib/libmysqlservices.a
/usr/local/share/man/man1/comp_err.1
/usr/local/share/man/man1/innochecksum.1
/usr/local/share/man/man1/msql2mysql.1
/usr/local/share/man/man1/my_print_defaults.1
/usr/local/share/man/man1/myisam_ftdump.1
/usr/local/share/man/man1/myisamchk.1
/usr/local/share/man/man1/myisamlog.1
/usr/local/share/man/man1/myisampack.1
/usr/local/share/man/man1/mysql-stress-test.pl.1
/usr/local/share/man/man1/mysql-test-run.pl.1
/usr/local/share/man/man1/mysql.1
/usr/local/share/man/man1/mysql.server.1
/usr/local/share/man/man1/mysql_client_test.1
/usr/local/share/man/man1/mysql_client_test_embedded.1
/usr/local/share/man/man1/mysql_config.1
/usr/local/share/man/man1/mysql_config_editor.1
/usr/local/share/man/man1/mysql_convert_table_format.1
/usr/local/share/man/man1/mysql_find_rows.1
/usr/local/share/man/man1/mysql_fix_extensions.1
/usr/local/share/man/man1/mysql_install_db.1
/usr/local/share/man/man1/mysql_plugin.1
/usr/local/share/man/man1/mysql_secure_installation.1
/usr/local/share/man/man1/mysql_setpermission.1
/usr/local/share/man/man1/mysql_tzinfo_to_sql.1
/usr/local/share/man/man1/mysql_upgrade.1
/usr/local/share/man/man1/mysql_waitpid.1
/usr/local/share/man/man1/mysql_zap.1
/usr/local/share/man/man1/mysqlaccess.1
/usr/local/share/man/man1/mysqladmin.1
/usr/local/share/man/man1/mysqlbinlog.1
/usr/local/share/man/man1/mysqlbug.1
/usr/local/share/man/man1/mysqlcheck.1
/usr/local/share/man/man1/mysqld_multi.1
/usr/local/share/man/man1/mysqld_safe.1
/usr/local/share/man/man1/mysqldump.1
/usr/local/share/man/man1/mysqldumpslow.1
/usr/local/share/man/man1/mysqlhotcopy.1
/usr/local/share/man/man1/mysqlimport.1
/usr/local/share/man/man1/mysqlman.1
/usr/local/share/man/man1/mysqlshow.1
/usr/local/share/man/man1/mysqlslap.1
/usr/local/share/man/man1/mysqltest.1
/usr/local/share/man/man1/mysqltest_embedded.1
/usr/local/share/man/man1/perror.1
/usr/local/share/man/man1/replace.1
/usr/local/share/man/man1/resolve_stack_dump.1
/usr/local/share/man/man1/resolveip.1
/usr/local/share/man/man8/mysqld.8

%pre
if [ $1 -eq 1 ]; then
    [ -n "`id -u mysql 2>/dev/null`" ] || useradd -r -M -s /sbin/nologin %{MYSQL_USER}
fi

%post
cd %{MYSQL_DIR}
chown -R mysql.mysql .
if [ -z "`find data/ -name '*.ibd' 2>/dev/null`" ]; then
    ./scripts/mysql_install_db --user=%{MYSQL_USER} --force || /bin/true
    cp support-files/mysql.server /etc/init.d/mysqld
    chmod +x /etc/init.d/mysqld
    chkconfig --add mysqld
    chkconfig mysqld on
    service mysqld start
    ln -sfn %{MYSQL_DIR}/bin/* ${PREFIX}/bin
./bin/mysql_secure_installation<<EOF || /bin/true

y
%{MYSQL_PASS}
%{MYSQL_PASS}
y
y
y
y
EOF
fi
chown -R root .
chown -R mysql data

%preun
if [ $1 -eq 0 ]; then
    if [ `ps aux | grep -v 'grep' | grep -c 'mysqld'` -gt 0 ]; then
        /etc/init.d/mysqld stop 2>/dev/null || /bin/true
    fi
    chkconfig --del mysqld 2>/dev/null || /bin/true
fi

%changelog

