%global tl_name graphicxpsd
%global tl_revision 78362

Name:		texlive-%{tl_name}
Epoch:		1
Version:	2.0
Release:	%{tl_revision}.1
Summary:	Adobe Photoshop Data format (PSD) support for graphicx package
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/graphicxpsd
License:	mit
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/graphicxpsd.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/graphicxpsd.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package provides Adobe Photoshop Data format (PSD) support for the
graphicx package with the sips (Darwin/macOS) or convert (ImageMagick)
command.

