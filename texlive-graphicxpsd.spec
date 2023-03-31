Name:		texlive-graphicxpsd
Version:	57341
Release:	2
Summary:	Adobe Photoshop Data format (PSD) support for graphicx package
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/graphicxpsd
License:	mit
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/graphicxpsd.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/graphicxpsd.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package provides Adobe Photoshop Data format (PSD) support
for the graphicx package with the sips (Darwin/macOS) or
convert (ImageMagick) command.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/graphicxpsd
%doc %{_texmfdistdir}/doc/latex/graphicxpsd

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
