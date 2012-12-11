Summary: 	Vulnerability Management with OpenVAS Manager
Name:		openvas-manager
Version:	2.0.5
Release:	1
Source0:		http://wald.intevation.org/frs/download.php/561/%name-%version.tar.gz
source1:	.abf.yml
Patch0:		openvas-manager-1.0.3-fix-linkage.patch
Group:		System/Configuration/Networking
Url:		http://www.openvas.org
License:	GPLv2+
BuildRequires:	openvas-devel >= 4.0
BuildRequires:	pkgconfig(gnutls)
BuildRequires:	sqlite3-devel
BuildRequires:	pkgconfig(glib-2.0)
BuildRequires:	doxygen perl-SQL-Translator
BuildRequires:	cmake

%description
The OpenVAS Manager is a layer between the OpenVAS Scanner and various
client applications. The upcoming clients cover web, desktop and command
line technology and will replace the classic OpenVAS Client. 

%prep
%setup -qn %name-%version
%patch0 -p0

sed -i -e 's#-Werror##' `grep -rl Werror *|grep CMakeLists.txt`

%build
export LDFLAGS="-lopenvas_base -lopenvas_misc -lgnutls"
%cmake
%make

%install
%makeinstall_std -C build

%files
%defattr(-,root,root)
%config(noreplace) %_sysconfdir/openvas/openvasmd_log.conf
%_sbindir/openvasmd
%_mandir/man8/openvasmd.8*
%_datadir/openvas/openvasmd


%changelog
* Thu Sep 08 2011 Luis Daniel Lucio Quiroz <dlucio@mandriva.org> 2.0.4-1mdv2011.0
+ Revision: 698900
- 2.0.4

* Sat Apr 02 2011 Funda Wang <fwang@mandriva.org> 2.0.2-1
+ Revision: 649816
- disable Werror
- new version 2.0.2

* Mon Jan 31 2011 Funda Wang <fwang@mandriva.org> 1.0.4-1
+ Revision: 634484
- new version 1.0.4

* Sun Nov 28 2010 Funda Wang <fwang@mandriva.org> 1.0.3-1mdv2011.0
+ Revision: 602200
- import openvas-manager

