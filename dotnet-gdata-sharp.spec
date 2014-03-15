#
%include	/usr/lib/rpm/macros.mono
#
Summary:	gdata-sharp - C# library that makes it easy to access data through Google Data APIs
Summary(pl.UTF-8):	gdata-sharp - biblioteka C# ułatwiająca dostęp do danych poprzez API Google Data
Name:		dotnet-gdata-sharp
Version:	2.2.0.0
Release:	1
License:	Apache v2.0
Group:		Libraries
#Source0Download: https://code.google.com/p/google-gdata/downloads/list
Source0:	http://google-gdata.googlecode.com/files/libgoogle-data-mono-%{version}.tar.gz
# Source0-md5:	d748a5ae2b349b9832e303e95c18ce79
Patch0:		%{name}-update.patch
URL:		http://code.google.com/p/google-gdata/
BuildRequires:	dos2unix
BuildRequires:	dotnet-newtonsoft-json-devel
BuildRequires:	mono-csharp
BuildRequires:	mono-devel
BuildRequires:	rpmbuild(monoautodeps)
Requires:	dotnet-newtonsoft-json
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The GData .NET Client Library provides a library and source code that
make it easy to access data through Google Data APIs.

%description -l pl.UTF-8
Biblioteka kliencka .NET GData ma na celu ułatwienie dostępu do danych
poprzez API Google Data.

%package devel
Summary:	Files required for compilation using gdata-sharp
Summary(pl.UTF-8):	Pliki wymagane do kompilacji z użyciem gdata-sharp
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	dotnet-newtonsoft-json-devel

%description devel
Files required for compilation using gdata-sharp.

%description devel -l pl.UTF-8
Pliki wymagane do kompilacji z użyciem gdata-sharp.

%prep
%setup -q -n libgoogle-data-mono-%{version}
%patch0 -p1
dos2unix misc/*.pc.in

%build
%{__make} \
	PREFIX=%{_prefix}

# alternative (but with no functional install target)
#xbuild "src/Google Data API SDK.sln"

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
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_prefix}/lib/mono/gac/Google.GData.AccessControl
%{_prefix}/lib/mono/gac/Google.GData.Analytics
%{_prefix}/lib/mono/gac/Google.GData.Apps
%{_prefix}/lib/mono/gac/Google.GData.Blogger
%{_prefix}/lib/mono/gac/Google.GData.Calendar
%{_prefix}/lib/mono/gac/Google.GData.Client
%{_prefix}/lib/mono/gac/Google.GData.Contacts
%{_prefix}/lib/mono/gac/Google.GData.Documents
%{_prefix}/lib/mono/gac/Google.GData.Extensions
%{_prefix}/lib/mono/gac/Google.GData.Photos
%{_prefix}/lib/mono/gac/Google.GData.Spreadsheets
%{_prefix}/lib/mono/gac/Google.GData.YouTube

%files devel
%defattr(644,root,root,755)
%dir %{_prefix}/lib/mono/GData-Sharp
%{_prefix}/lib/mono/GData-Sharp/Google.GData.AccessControl.dll
%{_prefix}/lib/mono/GData-Sharp/Google.GData.Analytics.dll
%{_prefix}/lib/mono/GData-Sharp/Google.GData.Apps.dll
%{_prefix}/lib/mono/GData-Sharp/Google.GData.Blogger.dll
%{_prefix}/lib/mono/GData-Sharp/Google.GData.Calendar.dll
%{_prefix}/lib/mono/GData-Sharp/Google.GData.Client.dll
%{_prefix}/lib/mono/GData-Sharp/Google.GData.Contacts.dll
%{_prefix}/lib/mono/GData-Sharp/Google.GData.Documents.dll
%{_prefix}/lib/mono/GData-Sharp/Google.GData.Extensions.dll
%{_prefix}/lib/mono/GData-Sharp/Google.GData.Photos.dll
%{_prefix}/lib/mono/GData-Sharp/Google.GData.Spreadsheets.dll
%{_prefix}/lib/mono/GData-Sharp/Google.GData.YouTube.dll
%{_pkgconfigdir}/gdata-sharp-acl.pc
%{_pkgconfigdir}/gdata-sharp-analytics.pc
%{_pkgconfigdir}/gdata-sharp-apps.pc
%{_pkgconfigdir}/gdata-sharp-blogger.pc
%{_pkgconfigdir}/gdata-sharp-calendar.pc
%{_pkgconfigdir}/gdata-sharp-contacts.pc
%{_pkgconfigdir}/gdata-sharp-core.pc
%{_pkgconfigdir}/gdata-sharp-documents.pc
%{_pkgconfigdir}/gdata-sharp-photos.pc
%{_pkgconfigdir}/gdata-sharp-spreadsheets.pc
%{_pkgconfigdir}/gdata-sharp-youtube.pc
