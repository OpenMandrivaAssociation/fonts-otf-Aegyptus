%define fontname	Aegyptus
%define name		fonts-otf-%{fontname}
%define version		3.11
%define release		4

%define fontdir		%{_datadir}/fonts/OTF/%{fontname}
%define fontconfdir	%{_sysconfdir}/X11/fontpath.d

Summary:	Unicode Aegyptus fonts
Name:		%{name}
Version:	%{version}
Release:	%{release}
Source0:	http://users.teilar.gr/~g1951d/%{fontname}311.zip
Source1:	http://users.teilar.gr/~g1951d/Gardiner311.zip
License:	Public Domain
Group:		System/Fonts/True type
Url:		https://users.teilar.gr/~g1951d/
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildArch:	noarch
BuildRequires: fontconfig
BuildRequires:	mkfontscale, mkfontdir

%description
Ars longa, vita brevis; this is the final version of Aegyptus. The
font encodes some 7100 Egyptian Hieroglyphs, all with a graphical
representation. The main sources of glyphs are Hieroglyphica and the
work of Alan Gardiner. Egyptian Hieroglyphs are allocated in the
Supplementary Private Use Plane 15, for the lack of a standard. The
font also covers Basic Latin, Egyptian Transliteration characters,
Meroitic, some Punctuation and other Symbols and the Gardiner set of
Egyptian Hieroglyphs supported by The Unicode Standard 5.2 (13000 -
1342F).

The Gardiner set is also available in the small font Gardiner (regular
and bold).

%prep
%setup -q -c %{name}-%{version}
unzip -o %SOURCE1

%install
%__rm -rf %{buildroot}

%__install -m 0755 -d %{buildroot}%{fontdir}
%__install -m 0644 *.otf %{buildroot}%{fontdir}
mkfontscale %{buildroot}%{fontdir}
mkfontdir %{buildroot}%{fontdir}

%__install -m 0755 -d %{buildroot}%{fontconfdir}
ln -s ../../../%{fontdir} %{buildroot}%{fontconfdir}/otf-%{fontname}:pri=50

%clean
%__rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc *.txt
%{fontconfdir}/otf*
%{fontdir}/*.otf
%{fontdir}/fonts.*



%changelog
* Tue May 17 2011 Funda Wang <fwang@mandriva.org> 3.11-3mdv2011.0
+ Revision: 675501
- br fontconfig for fc-query used in new rpm-setup-build

* Sun Dec 05 2010 Oden Eriksson <oeriksson@mandriva.com> 3.11-2mdv2011.0
+ Revision: 610720
- rebuild

* Wed Mar 03 2010 Lev Givon <lev@mandriva.org> 3.11-1mdv2010.1
+ Revision: 513931
- import fonts-otf-Aegyptus

