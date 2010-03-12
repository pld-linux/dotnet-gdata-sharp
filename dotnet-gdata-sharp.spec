%include	/usr/lib/rpm/macros.mono

Summary:	gdata-sharp is a C# library that makes it easy to access data through Google Data APIs
Name:		dotnet-gdata-sharp
Version:	1.4.0.2
Release:	1
License:	Apache v2.0
Source0:	http://google-gdata.googlecode.com/files/libgoogle-data-mono-%{version}.tar.gz
# Source0-md5:	3914538201b00c6d33aa6ada0e9d1ec6
Patch0:		pkgconfig-typo-fix.patch
Group:		Development/Libraries
URL:		http://code.google.com/p/google-gdata/
BuildRequires:	mono-devel
BuildRequires:	monodoc
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The GData .NET Client Library provides a library and source code that
make it easy to access data through Google Data APIs.

%package devel
Summary:	Files required for compilation using gdata-sharp
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Files required for compilation using gdata-sharp.

%prep
%setup -q -n libgoogle-data-mono-%{version}
%patch0 -p1

%build
%{__make} \
	PREFIX=%{_prefix}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	PREFIX=%{_prefix}

%clean
rm -rf "$RPM_BUILD_ROOT"

%files
%defattr(644,root,root,755)
%{_prefix}/lib/mono/gac/Google.GData.*

%files devel
%defattr(644,root,root,755)
%dir %{_prefix}/lib/mono/GData-Sharp
%{_prefix}/lib/mono/GData-Sharp/*.dll
%{_pkgconfigdir}/gdata-sharp-*.pc
