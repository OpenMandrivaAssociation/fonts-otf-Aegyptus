%define fontname	Aegyptus
%define name		fonts-otf-%{fontname}
%define version		3.11
%define release		%mkrel 2

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
Url:		http://users.teilar.gr/~g1951d/
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

