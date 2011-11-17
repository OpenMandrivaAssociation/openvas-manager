Summary: 	Vulnerability Management with OpenVAS Manager
Name:		openvas-manager
Version:	2.0.4
Release:	%mkrel 2
License:	GPLv2+
Group:		System/Configuration/Networking
URL:		http://www.openvas.org
Source:		http://wald.intevation.org/frs/download.php/561/%name-%version.tar.gz
Patch0:		openvas-manager-1.0.3-fix-linkage.patch
BuildRequires:	openvas-devel >= 4.0
BuildRequires:	gnutls-devel
BuildRequires:	sqlite3-devel
BuildRequires:	glib2-devel
BuildRequires:	doxygen perl-SQL-Translator
BuildRequires:	cmake
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

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
rm -rf %{buildroot}

%makeinstall_std -C build

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%config(noreplace) %_sysconfdir/openvas/openvasmd_log.conf
%_sbindir/openvasmd
%_mandir/man8/openvasmd.8*
%_datadir/openvas/openvasmd
