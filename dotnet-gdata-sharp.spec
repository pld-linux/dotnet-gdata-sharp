#
%include	/usr/lib/rpm/macros.mono
#
Summary:	gdata-sharp is a C# library that makes it easy to access data through Google Data APIs
Name:		dotnet-gdata-sharp
Version:	1.7.0.1
Release:	1
License:	Apache v2.0
Group:		Development/Libraries
Source0:	http://google-gdata.googlecode.com/files/libgoogle-data-mono-%{version}.tar.gz
# Source0-md5:	ba4f57eb5ed597d2e5d16f5deb69d411
URL:		http://code.google.com/p/google-gdata/
BuildRequires:	dos2unix
BuildRequires:	mono-csharp
BuildRequires:	mono-devel
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
dos2unix misc/*.pc.in

%build
%{__make} \
	PREFIX=%{_prefix}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	PREFIX=%{_prefix}

if [ "%{_lib}" != "lib" ]; then
	install -d $RPM_BUILD_ROOT%{_prefix}/%{_lib}
	mv $RPM_BUILD_ROOT%{_prefix}/{lib,%{_lib}}/pkgconfig
fi

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
