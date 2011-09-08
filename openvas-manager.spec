Summary: 	Vulnerability Management with OpenVAS Manager
Name:		openvas-manager
Version:	2.0.4
Release:	%mkrel 1
Source:		http://wald.intevation.org/frs/download.php/561/%name-%version.tar.gz
Patch0:		openvas-manager-1.0.3-fix-linkage.patch
Group:		System/Configuration/Networking
Url:		http://www.openvas.org
License:	GPLv2+
BuildRoot:	%{_tmppath}/%name-%{version}-root
BuildRequires:	openvas-devel >= 4.0
BuildRequires:	gnutls-devel
BuildRequires:	sqlite3-devel
BuildRequires:	glib2-devel
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
%cmake
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std -C build

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%config(noreplace) %_sysconfdir/openvas/openvasmd_log.conf
%_sbindir/openvasmd
%_mandir/man8/openvasmd.8*
%_datadir/openvas/openvasmd
