Summary: Library to drive several graphical LC-displays
Name: serdisplib
Version: 1.97.9
Release: 1
License: GPL
Group: System Environment/Libraries
URL: http://serdisplib.sourceforge.net/

Packager: Wolfgang Astleitner <mrwastl@users.sf.net>
Source: http://prdownloads.sourceforge.net/serdisplib/serdisplib-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

# conditional dependencies: default values are --with-libusb --without-libSDL
# e.g:  to build RPMs with support for libSDL:
#       rpmbuild --with libSDL --rebuild serdisplib-x.y-1.src.rpm
%{!?_with_libusb: %{!?_without_libusb: %define _with_libusb --with-libusb}}
%{!?_with_libSDL: %{!?_without_libSDL: %define _without_libSDL --without-libSDL}}

#AutoReqProv: no
#%{?_with_libusb:Requires: libusb >= 0.1.8}
#%{?_with_libSDL:Requires: SDL >= 1.2.0}

BuildRequires: autoconf >= 2.5 gd-devel >= 2
%{?_with_libusb:BuildRequires: libusb-devel >= 0.1.8}
%{?_with_libSDL:BuildRequires: SDL-devel >= 1.2.0}

%description
serdisplib is a library to drive graphical LC-displays

%package devel
#AutoReqProv: no
Requires: serdisplib = %{version}-%{release}
Summary:  The development libraries and header files for serdisplib
Group:    Development/Libraries

%description devel
The development libraries and header files for serdisplib, a library to drive several graphical LC-displays


%package tools
#AutoReqProv: no
Requires: serdisplib = %{version}-%{release}
Requires: gd >= 2
Summary:  Serdisplib Tools (testserdisp, multidisplay)
Group:    Applications/Multimedia

%description tools
Tools for serdisplib, a library to drive several graphical LC-displays. Included tools are: testserdisp, multidisplay.



%prep 
%setup
%configure %{?_with_libusb:--enable-libusb} %{?_with_libSDL:--enable-libSDL}

#%patch


%build
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
#%makeinstall
#{
#    cd %{buildroot}/%{_libdir}
#    ln -sf ./libserdisp.so.%{version} ./libserdisp.so
#}


%clean
%{__rm} -rf %{buildroot}


%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig


%files
%defattr(-, root, root, 0755)
%doc AUTHORS BUGS COPYING HISTORY INSTALL PINOUTS README TODO
%{_libdir}/*.so*
#%doc %{_mandir}/man?/*


%files devel
%defattr(-, root, root, 0755)
%{_libdir}/*.a
%{_includedir}/serdisplib/*

%files tools
%defattr(-, root, root, 0755)
%{_bindir}/*




%changelog
* Sun Feb 13 2010 Wolfgang Astleitner <mrwastl@users.sf.net> - 1.97.9-1
- conditional dependencies libusb (--with-libusb, default: yes) and libSDL (--with-libSDL, default: no)
* Sun Feb 22 2007 Wolfgang Astleitner <mrwastl@users.sf.net> - 1.97.4-1
- dependency libusb -> libusb-devel
* Sun Feb 11 2007 Wolfgang Astleitner <mrwastl@users.sf.net> - 1.97.3-1
- Fixed some building and release-version problems
* Sun Oct 02 2005 Wolfgang Astleitner <mrwastl@users.sf.net> - 1.96-1
- Release version
* Sun Jun 12 2005 Wolfgang Astleitner <mrwastl@users.sf.net> - 1.96-0
- Initial package. (dvdauthor .spec-file taken as template)
