Name:		texlive-chinesechess
Version:	63276
Release:	2
Summary:	Typeset Chinese chess with l3draw
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/chinesechess
License:	lppl1.3c
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/chinesechess.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/chinesechess.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This LaTeX3 package based on l3draw provides macros and an
environment for Chinese chess manual writing.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/chinesechess
%doc %{_texmfdistdir}/doc/latex/chinesechess

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
